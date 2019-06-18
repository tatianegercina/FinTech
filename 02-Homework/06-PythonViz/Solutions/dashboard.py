import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import param
import holoviews as hv
from holoviews import opts
import panel as pn
import plotly_express as px
from pathlib import Path

pn.extension("plotly")
hv.extension("bokeh", logo=False)

# Define datasets
sfo_data_path = Path("../Data/sfo_neighborhoods_census_data.csv")
map_data_path = Path("../Data/map_info.csv")
sfo_data = pd.read_csv(sfo_data_path, index_col=0)
map_data = pd.read_csv(map_data_path)

# Define dashboard creation class
class PythonicMonopoly:

    df = sfo_data
    map_data = map_data
    expensive_data = None

    def housing_units_bar(self):
        df_housing_units = self.df["housing_units"].groupby(self.df.index).mean()
        housing_units_std = df_housing_units.std()
        housing_units_min = min(df_housing_units)
        housing_units_max = max(df_housing_units)

        fig_housing_units = plt.figure(figsize=(7, 6))
        ax = fig_housing_units.add_subplot(df_housing_units.plot(kind="bar"))
        ax.set_xlabel("Year")
        ax.set_ylabel("Housing Units")
        ax.set_title("Housing Units")
        ax.set_ylim(
            housing_units_min - housing_units_std, housing_units_max + housing_units_std
        )
        plt.close(fig_housing_units)
        return pn.pane.Matplotlib(fig_housing_units)

    def costs_lines(self):
        df_avg_costs = (
            self.df[["sale_price_sqr_foot", "gross_rent"]].groupby(self.df.index).mean()
        )
        df_avg_costs.reset_index(inplace=True)
        df_avg_costs.rename(columns={"index": "year"}, inplace=True)
        fig_sale_price = hv.Curve(
            df_avg_costs,
            ("year", "Year"),
            ("sale_price_sqr_foot", "Average Cost"),
            label="Sale Price",
        )
        fig_gross_rent = hv.Curve(
            df_avg_costs,
            ("year", "Year"),
            ("gross_rent", "Average Cost"),
            label="Gross Rent",
        )
        fig_costs = fig_sale_price * fig_gross_rent
        fig_costs = fig_costs.opts(
            width=550,
            height=400,
            legend_position="left",
            tools=["hover"],
            title="Avg. Gross Rent Vs. Price per Sqr Foot",
        )
        return fig_costs

    def mean_sale_price(self):
        df_costs = self.df.groupby([self.df.index, "neighborhood"]).mean()
        df_costs.reset_index(inplace=True)
        df_costs.rename(columns={"level_0": "year"}, inplace=True)
        costs = hv.Dataset(df_costs, ["year", "neighborhood"])
        costs = costs.redim.label(
            year="Year",
            neighborhood="Neighborhood",
            sale_price_sqr_foot="Sale Price per Square Foot",
        )
        sale_price_curve = costs.to(
            hv.Curve, "year", "sale_price_sqr_foot", groupby="neighborhood"
        )
        sale_price_curve = sale_price_curve.opts(width=600, tools=["hover"])
        return sale_price_curve

    def top_expensive_bar(self):
        self.expensive_data = self.df.groupby(by="neighborhood").mean()
        self.expensive_data = self.expensive_data.sort_values(
            by="sale_price_sqr_foot", ascending=False
        ).head(10)
        self.expensive_data = self.expensive_data.reset_index()
        expensive_neighborhoods = hv.Bars(
            self.expensive_data,
            ("neighborhood", "Neighborhood"),
            ("sale_price_sqr_foot", "Sale Price per Square Foot"),
        )
        expensive_neighborhoods = expensive_neighborhoods.options(
            width=600,
            height=400,
            tools=["hover"],
            title="Top 10 Expensive Neighborhoods in SFO",
            xrotation=90,
        )
        return expensive_neighborhoods

    def plot_paralell_coord(self):
        expensive_plot = px.parallel_coordinates(
            self.expensive_data,
            color="sale_price_sqr_foot",
            color_continuous_scale=px.colors.sequential.Inferno,
        )
        return expensive_plot

    def plot_paralell_cat(self):
        expensive_plot = px.parallel_categories(
            self.expensive_data,
            color="sale_price_sqr_foot",
            color_continuous_scale=px.colors.sequential.Inferno,
        )
        return expensive_plot

    def plot_map(self):
        px.set_mapbox_access_token(open("mapbox_token").read())
        return px.scatter_mapbox(
            self.map_data,
            lat="Lat",
            lon="Lon",
            size="sale_price_sqr_foot",
            color="gross_rent",
            color_continuous_scale=px.colors.cyclical.IceFire,
            size_max=15,
            zoom=11,
            hover_name="Neighborhood",
            title="Sale Price Per Square Foot and Gross Rent",
        )


# panel creation

dashboard = PythonicMonopoly()


# Logo license info: https://www.iconfinder.com/icons/56262/building_office_icon
logo = """<img src="https://cdn0.iconfinder.com/data/icons/free-business-desktop-icons/256/Company.png"
            width=150 height=127 align="left" margin=20px>"""
title = "<h2>Real State Analysis from San Francisco</h2>"

desc = pn.pane.HTML(
    """This dashboard presents an analysis of historical prices of house units,
    sale price per square foot and gross rent in San Francisco, California from
    2010 to 2016.""",
    width=450,
)

panel = pn.Row(
    pn.Column(logo, title, desc),
    pn.Column(
        pn.Row(dashboard.housing_units_bar(), pn.Row(dashboard.costs_lines())),
        pn.Row(dashboard.mean_sale_price()),
        pn.Row(dashboard.top_expensive_bar()),
        pn.Row(dashboard.plot_paralell_coord(), dashboard.plot_paralell_cat()),
        pn.Row(dashboard.plot_map()),
    ),
)
panel.servable()

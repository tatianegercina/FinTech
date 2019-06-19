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
expensive_data = sfo_data.groupby(by="neighborhood").mean()
expensive_data = expensive_data.sort_values(
    by="sale_price_sqr_foot", ascending=False
).head(10)
expensive_data = expensive_data.reset_index()

# Define dashboard creation functions
def housing_units_bar():
    df_housing_units = sfo_data["housing_units"].groupby(sfo_data.index).mean()
    housing_units_std = df_housing_units.std()
    housing_units_min = min(df_housing_units)
    housing_units_max = max(df_housing_units)

    fig_housing_units = plt.figure(figsize=(7, 6))
    plot_housing_units = df_housing_units.plot.bar()
    plot_housing_units.set_xlabel("Year", fontsize=12)
    plot_housing_units.set_ylabel("Housing Units", fontsize=12)
    plot_housing_units.set_title("Housing Units in San Francisco from 2010 to 2016", fontsize=14, fontweight='bold')
    plot_housing_units.set_ylim(
        housing_units_min - housing_units_std, housing_units_max + housing_units_std
    )
    plt.close(fig_housing_units)
    return pn.pane.Matplotlib(fig_housing_units)

def costs_lines():
    df_avg_costs = (
        sfo_data[["sale_price_sqr_foot", "gross_rent"]].groupby(sfo_data.index).mean()
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

def mean_sale_price():
    df_costs = sfo_data.groupby([sfo_data.index, "neighborhood"]).mean()
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

def top_expensive_bar():
    
    expensive_neighborhoods = hv.Bars(
        expensive_data,
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

def plot_paralell_coord():
    expensive_plot = px.parallel_coordinates(
        expensive_data,
        color="sale_price_sqr_foot",
        color_continuous_scale=px.colors.sequential.Inferno,
    )
    return expensive_plot

def plot_paralell_cat():
    expensive_plot = px.parallel_categories(
        expensive_data,
        color="sale_price_sqr_foot",
        color_continuous_scale=px.colors.sequential.Inferno,
    )
    return expensive_plot

def plot_map():
    px.set_mapbox_access_token(open("mapbox_token").read())
    return px.scatter_mapbox(
        map_data,
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
# panel creation
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

text = pn.pane.Markdown("""
    ![Logo](https://cdn0.iconfinder.com/data/icons/free-business-desktop-icons/256/Company.png)
    
    # Real State Analysis from San Francisco
    
    This dashboard presents an analysis of historical prices of house units,
    sale price per square foot and gross rent in San Francisco, California from
    2010 to 2016.
""")

panel = pn.Column(
    text,
    pn.Row(housing_units_bar(), costs_lines()),
    plot_map(),
    mean_sale_price(),
    top_expensive_bar(),
    pn.Row(plot_paralell_coord(), plot_paralell_cat()),
    width=800
)

panel.servable()

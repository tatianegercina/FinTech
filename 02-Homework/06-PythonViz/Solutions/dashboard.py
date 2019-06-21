# initial imports
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import hvplot.pandas
import panel as pn
import plotly_express as px
from pathlib import Path

pn.extension("plotly")

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
df_avg_costs = (
    sfo_data[["sale_price_sqr_foot", "gross_rent"]].groupby(sfo_data.index).mean()
)

# Define dashboard creation functions
def housing_units_bar():
    df_housing_units = sfo_data["housing_units"].groupby(sfo_data.index).mean()
    housing_units_std = df_housing_units.std()
    housing_units_min = min(df_housing_units)
    housing_units_max = max(df_housing_units)

    fig_housing_units = plt.figure()
    plot_housing_units = df_housing_units.plot.bar()
    plot_housing_units.set_xlabel("Year", fontsize=12)
    plot_housing_units.set_ylabel("Housing Units", fontsize=12)
    plot_housing_units.set_title("Housing Units", fontsize=14, fontweight="bold")
    plot_housing_units.set_ylim(
        housing_units_min - housing_units_std, housing_units_max + housing_units_std
    )
    plt.close(fig_housing_units)
    return pn.pane.Matplotlib(fig_housing_units, tight=True)


def gross_rent():
    fig_avg_gross_rent = plt.figure()
    plot_avg_gross_rent = df_avg_costs["gross_rent"].plot()
    plot_avg_gross_rent.set_xlabel("Year", fontsize=12)
    plot_avg_gross_rent.set_ylabel("Gross Rent", fontsize=12)
    plot_avg_gross_rent.set_title("Average Gross Rent", fontsize=14, fontweight="bold")
    plt.close(fig_avg_gross_rent)
    return pn.pane.Matplotlib(fig_avg_gross_rent, tight=True)


def sale_price():
    fig_avg_sale_price = plt.figure()
    plot_avg_sale_price = df_avg_costs["sale_price_sqr_foot"].plot()
    plot_avg_sale_price.set_xlabel("Year", fontsize=12)
    plot_avg_sale_price.set_ylabel("Avg. Sale Price", fontsize=12)
    plot_avg_sale_price.set_title(
        "Average Sale Price per Square Foot", fontsize=14, fontweight="bold"
    )
    plt.close(fig_avg_sale_price)
    return pn.pane.Matplotlib(fig_avg_sale_price, tight=True)


def mean_sale_price():
    df_costs = sfo_data.groupby([sfo_data.index, "neighborhood"]).mean()
    df_costs.reset_index(inplace=True)
    df_costs.rename(columns={"level_0": "year"}, inplace=True)
    sale_price_curve = df_costs.hvplot.line(
        "year",
        "sale_price_sqr_foot",
        xlabel="Year",
        ylabel="Avg. Sale Price per Square Foot",
        groupby="neighborhood",
    )
    return sale_price_curve


def top_expensive_bar():

    expensive_neighborhoods = expensive_data.hvplot.bar(
        "neighborhood",
        "sale_price_sqr_foot",
        title="Top 10 Expensive Neighborhoods in SFO",
        xlabel="Neighborhood",
        ylabel="Avg. Sale Price per Square Foot",
        height=400,
        rot=90,
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
    plotly_map = px.scatter_mapbox(
        map_data,
        lat="Lat",
        lon="Lon",
        size="sale_price_sqr_foot",
        color="gross_rent",
        color_continuous_scale=px.colors.cyclical.IceFire,
        size_max=15,
        zoom=11,
        hover_name="Neighborhood",
        title="Averange Sale Price Per Square Foot and Gross Rent Analysis",
        width=1000,
        height=700,
    )
    plotly_panel = pn.pane.Plotly(plotly_map)
    plotly_panel._updates = True
    return plotly_panel


# panel creation
# Tabbed panel dashboard
title = pn.pane.Markdown(
    """
# Real Estate Analysis of San Francisco from 2010 to 2016
""",
    width=800,
)

welcome = pn.pane.Markdown(
    """
This dashboard presents a visual analysis of historical prices of house units,
sale price per square foot and gross rent in San Francisco, California
from 2010 to 2016.
You can navigate through the tabs above to explore
more details about the evolution of the real estate market on
The Golden City across these years.
"""
)

tabs = pn.Tabs(
    ("Welcome", pn.Column(welcome, plot_map())),
    ("Yearly Market Analysis", pn.Row(housing_units_bar(), gross_rent(), sale_price())),
    ("Neighborhood Analysis", pn.Column(mean_sale_price(), top_expensive_bar())),
    (
        "Parallel Plots Analysis",
        pn.Row(plot_paralell_coord(), plot_paralell_cat(), width=900),
    ),
)

panel = pn.Column(pn.Row(title), tabs, width=900)

# Panel launch
panel.servable()

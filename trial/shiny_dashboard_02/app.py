# https://shiny.posit.co/py/docs/overview.html#templates

from pathlib import Path
from plotnine import ggplot, aes, geom_histogram, geom_vline
from faicons import icon_svg
from palmerpenguins import load_penguins
from shiny import reactive
from shiny.express import input, render, ui

df = load_penguins()
app_dir = Path(__file__).parent

ui.page_opts(title="Penguins histogram", fillable=True)

with ui.sidebar(title="Filter controls"):
    ui.input_checkbox_group(
        "species",
        "Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
    )
    ui.input_checkbox_group(
        "island",
        "Island",
        ["Biscoe", "Dream", "Torgersen"],
        selected=["Biscoe", "Dream", "Torgersen"],
    )

with ui.layout_column_wrap(fill=False):
    with ui.value_box(showcase=icon_svg("earlybirds")):
        "Number of penguins"

        @render.text
        def count():
            return filtered_df().shape[0]

    with ui.value_box(showcase=icon_svg("ruler-horizontal")):
        "Average bill length"

        @render.text
        def bill_length():
            return f"{filtered_df()['bill_length_mm'].mean():.1f} mm"

    with ui.value_box(showcase=icon_svg("ruler-vertical")):
        "Average bill depth"

        @render.text
        def bill_depth():
            return f"{filtered_df()['bill_depth_mm'].mean():.1f} mm"


with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Bill length")

        @render.plot
        def length():
            return (
                ggplot(filtered_df(), aes(x="bill_length_mm"))
                + geom_histogram()
                + geom_vline(
                    xintercept=filtered_df()["bill_length_mm"].mean(),
                    color="green",
                    linetype="dashed",
                )
            )


@reactive.calc
def filtered_df():
    filt_df = df[df["species"].isin(input.species())]
    filt_df = filt_df[filt_df["island"].isin(input.island())]
    return filt_df
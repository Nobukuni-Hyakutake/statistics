# https://shiny.posit.co/py/templates/basic-app-plot/
from plotnine import ggplot, aes, geom_histogram

# Import data from shared.py
from shared import df
from shiny.express import input, render, ui

# Page title (with some additional top padding)
ui.page_opts(title=ui.h2("Basic Shiny app", class_="pt-5"))


# Render a histogram of the selected variable (input.var())
@render.plot
def hist():
    p = ggplot(df, aes(x=input.var())) + geom_histogram()
    return p


# Select input for choosing the variable to plot
ui.input_select("var", "Select variable", choices=["bill_length_mm", "body_mass_g"])

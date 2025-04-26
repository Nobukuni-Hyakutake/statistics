import matplotlib.pyplot as plt
from shiny.express import input, render, ui
from plotnine import *
from palmerpenguins import load_penguins
import pandas as pd
import math

ui.input_slider("n", "Number of bins", 0, 100, 20)

ui.input_select(  
    "select",  
    "Select an option below:",  
    {"Adelie": "Adelie", "Chinstrap": "Chinstrap"},  
)  

@render.plot(alt="A histogram")  
def plot():  
    df = load_penguins()
    df=df.loc(df["species"]==str(input.select()))
    mass = df["body_mass_g"]

    fig, ax = plt.subplots()
    ax.hist(mass, input.n(), density=True)
    ax.set_title("Palmer Penguin Masses")
    ax.set_xlabel("Mass (g)")
    ax.set_ylabel("Density")

    return fig  
  

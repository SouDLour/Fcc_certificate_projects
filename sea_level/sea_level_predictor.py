import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file

    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot('CSIRO Adjusted Sea Level', 'Year','scatter', title='Sea level Plot')

    # Create first line of best fit


    # Create second line of best fits


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
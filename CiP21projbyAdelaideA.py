"""Standford Code in Place 2021 - Final Project:
Creating a heatmap visualization with seaborn 
submission by Adelaide Atakora


To run a demo of this program, ensure you have the following packages installed: pandas, seaborn, and matplotlib."""


# Imports the following packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Creates a heatmap from a pandas pivot table with seaborn
def create_heatmap(df):
    # Creates a pandas pivot table to hold the data for the heatmap
    heatmap_data = pd.pivot_table(
        df, index='continent', columns='year', values='lifeExp')
    # Prints the heatmap table as an output
    print(heatmap_data)

    # Creates the heatmap from the pivot table data
    sns.heatmap(heatmap_data)


# Creates the heatmap with matlablib.pyplot
def plot_heatmap_image():
    # Plots the title of the heatmap
    plt.title("Heatmap of Life Expectancy Over the Years by Continent")

    # Saves an image of the heatmap
    plt.show()


# Calls all the relevant code pieces to be executed in main
def main():
    # Reads csv data from file located in the specified path
    df = pd.read_csv(
        r'https://raw.githubusercontent.com/Adela7/StanfordCodeinPlace21Project/main/LifeExpectancybyCountry.csv')
    # prints DataFrame to output
    print(df)

    # Calls the create_heatmap() funtion to creates a heatmap using the DataFrame above
    create_heatmap(df)

    # Calls the plot_heatmap_image() funtion to plot and save an image of the heatmap in project folder
    plot_heatmap_image()


if __name__ == '__main__':
    main()

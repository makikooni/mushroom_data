""" source: https://www.kaggle.com/datasets/uciml/mushroom-classification """
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("mushroom_data.csv")
print(df.head())

def plot_graphs(df):
    output_directory = "/Users/makikooni/Github/mushroom_data/Figures"
    columns = df.columns.tolist()
    for column in columns:
        sns.countplot(data=df, x=column)
        output_filename = os.path.join(output_directory, f"{column}_countplot.png")
        plt.savefig(output_filename)
        #plt.show()
        plt.close()

def find_modes(df,column_choice):
    total_rows = len(df)
    modes = df.mode()

    mode_values = {}  # Create a dictionary to store mode values

    for column in df.columns:
        mode_value = modes.loc[0, column]
        mode_count = (df[column] == mode_value).sum()
        mode_percentage = (mode_count / total_rows) * 100
        mode_values[column] = (mode_value, mode_percentage)
        
        if column == column_choice:
            print(f"Mode of the column {column} is: {mode_value}, Percentage: {mode_percentage:.2f}%")
    
    return mode_values

find_modes(df,'Habitat')
#python3 /Users/makikooni/Github/mushroom_data/source.py
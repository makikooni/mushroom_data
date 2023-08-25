""" source: https://www.kaggle.com/datasets/uciml/mushroom-classification """
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("mushroom_data.csv")

output_directory = "/Users/makikooni/Github/mushroom_data/Figures"

columns = df.columns.tolist()
for column in columns:
    sns.countplot(data=df, x=column)
    output_filename = os.path.join(output_directory, f"{column}_countplot.png")
    plt.savefig(output_filename)
    
    plt.close()


#  python3 /Users/makikooni/Github/mushroom_data/source.py
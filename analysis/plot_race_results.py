import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from etl.fetch_f1_data import get_race_results

def plot_results(df):
    # Sort by position to get the correct order
    df['position'] = df['position'].astype(int)
    df = df.sort_values(by="position")

    # Create the plot
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='driver', y='position', palette="viridis")
    plt.title('Race Results')
    plt.xlabel('Driver')
    plt.ylabel('Position')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save the plot
    plt.savefig('race_results.png')
    plt.close()

if __name__ == "__main__":
    # Get race results using the get_race_results function
    df = get_race_results(year=2023, round_num=1)
    
    if not df.empty:
        plot_results(df)
        print("Race results plot saved as 'race_results.png'")
    else:
        print("No race results found!")

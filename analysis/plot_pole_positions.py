import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from etl.fetch_f1_data import get_race_results

def plot_pole_positions(pole_counts):
    # Create the plot
    plt.figure(figsize=(12, 6))
    sns.barplot(x=pole_counts.index, y=pole_counts.values, palette="Blues_d")
    plt.title('Pole Positions per Driver (2023 Season)')
    plt.xlabel('Driver')
    plt.ylabel('Number of Pole Positions')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save the plot
    plt.savefig('pole_positions_2023.png')
    plt.close()

def get_pole_positions_for_year(year=2023):
    # Create an empty DataFrame to hold all race results for the year
    all_results = pd.DataFrame()

    # Iterate over all possible rounds (you can adjust this if needed)
    for round_num in range(1, 25):  # Assuming there are 24 rounds in 2023
        print(f"Fetching race results for round {round_num} of {year}...")
        df = get_race_results(year=year, round_num=round_num)
        
        # If the DataFrame is not empty, append it to the results
        if not df.empty:
            all_results = pd.concat([all_results, df], ignore_index=True)

    # Filter to only include pole positions (1st place)
    pole_positions = all_results[all_results['position'] == 1]
    
    # Count how many times each driver has finished in pole position
    pole_counts = pole_positions['driver'].value_counts()

    return pole_counts

if __name__ == "__main__":
    # Get pole position counts for the 2023 season
    pole_counts = get_pole_positions_for_year(year=2023)
    
    if not pole_counts.empty:
        plot_pole_positions(pole_counts)
        print("Pole positions plot for 2023 season saved as 'pole_positions_2023.png'")
    else:
        print("No race results found for 2023!")

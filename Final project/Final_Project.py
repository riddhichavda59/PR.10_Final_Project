import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD DATASET FROM THE EXTERNAL CSV FILE
csv_filename = "covid_data.csv"
try:
    df = pd.read_csv(csv_filename)
    print(f"Successfully loaded dataset from '{csv_filename}'.")
except FileNotFoundError:
    print(f"Error: The file '{csv_filename}' was not found.")
    print("Please ensure both 'covid_data.csv' and this script are in the same directory.")
    exit()

# Convert the date column to a proper datetime format
df['date'] = pd.to_datetime(df['date'])

# Display initial data inspection structures
print("\n--- Initial Dataset Overview ---")
print(df.head())

# Set a beautiful, clean theme for all static plots
sns.set_theme(style="whitegrid")

# Chart 1: Total Cases Trend Over Time (Line Plot)
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='date', y='total_cases', hue='location', marker="o", linewidth=2.5)
plt.title('COVID-19 Total Cases Over Time by Country', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Total Confirmed Cases')
plt.legend(title='Country')
plt.tight_layout()
plt.savefig('total_cases_trend.png')  # Saves chart as an image
plt.show()

# Chart 2: Total Cases vs Total Deaths Breakdown (Scatter Plot)
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='total_cases', y='total_deaths', hue='location', s=150, alpha=0.8)
plt.title('Relationship Matrix: Total Cases vs Total Deaths', fontsize=14, fontweight='bold')
plt.xlabel('Total Confirmed Cases')
plt.ylabel('Total Reported Deaths')
plt.legend(title='Country')
plt.tight_layout()
plt.savefig('cases_vs_deaths.png')
plt.show()

# Chart 3: Daily New Cases Comparison (Bar Plot)
plt.figure(figsize=(10, 5))
# Using the latest date entries for a clean bar comparison chart
latest_date = df['date'].max()
latest_df = df[df['date'] == latest_date]

sns.barplot(data=latest_df, x='location', y='new_cases', hue='location', palette='muted', legend=False)
plt.title(f'Daily New Cases Comparison (As of {latest_date.strftime("%Y-%m-%d")})', fontsize=14, fontweight='bold')
plt.xlabel('Country')
plt.ylabel('New Registered Cases')
plt.tight_layout()
plt.savefig('new_cases_comparison.png')
plt.show()

print("\nProject process complete! All target data structures successfully visualized using Matplotlib and Seaborn.")

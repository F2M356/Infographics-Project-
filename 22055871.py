import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("globalterrorismdb_0718dist.csv", encoding='ISO-8859-1')

# Data Processing
# Focus on relevant columns for analysis
df = df[['iyear', 'country_txt', 'attacktype1_txt', 'nkill']]

# Handle missing values
df.fillna({'nkill': 0}, inplace=True)

# Summary statistics
total_attacks = df['iyear'].value_counts().sort_index()
total_deaths = df.groupby('iyear')['nkill'].sum()

# Aggregating data for other plots
top_countries = df['country_txt'].value_counts().head(10)
attack_types = df['attacktype1_txt'].value_counts().head(10)

# Plot 1: Number of Attacks per Year (Line Plot)
plt.figure(figsize=(12, 6))
sns.lineplot(x=total_attacks.index, y=total_attacks.values)
plt.title("Number of Terrorist Attacks per Year")
plt.xlabel("Year")
plt.ylabel("Number of Attacks")
plt.grid(True)
plt.text(1975, max(total_attacks.values)*0.9, "Increase in attacks over the years", fontsize=12, color='blue')
plt.tight_layout()
plt.savefig("22055871_attacks_per_year.png", dpi=300)

# Plot 2: Number of Deaths per Year (Bar Plot)
plt.figure(figsize=(12, 6))
sns.barplot(x=total_deaths.index, y=total_deaths.values, color='red')
plt.title("Number of Deaths due to Terrorist Attacks per Year")
plt.xlabel("Year")
plt.ylabel("Number of Deaths")
plt.xticks(rotation=45)
plt.grid(True)
plt.text(1975, max(total_deaths.values)*0.9, "High fatalities in peak years", fontsize=12, color='red')
plt.tight_layout()
plt.savefig("22055871_deaths_per_year.png", dpi=300)

# Plot 3: Top 10 Countries by Number of Attacks (Horizontal Bar Plot)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='muted')
plt.title("Top 10 Countries by Number of Terrorist Attacks")
plt.xlabel("Number of Attacks")
plt.ylabel("Country")
plt.grid(True, axis='x')
plt.text(max(top_countries.values)*0.5, 8, "Most attacks in a few countries", fontsize=12, color='blue')
plt.tight_layout()
plt.savefig("22055871_top_countries.png", dpi=300)

# Plot 4: Top 10 Attack Types (Pie Chart)
plt.figure(figsize=(12, 6))
colors = sns.color_palette('muted')
wedges, texts, autotexts = plt.pie(attack_types.values, colors=colors, startangle=140, autopct='%1.1f%%', textprops=dict(color="w"))
plt.legend(wedges, attack_types.index, title="Attack Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Top 10 Attack Types")
plt.tight_layout()
plt.savefig("22055871_attack_types.png", dpi=300)

# Compile the infographic
fig, axes = plt.subplots(2, 2, figsize=(20, 15))

# Subplot 1
sns.lineplot(x=total_attacks.index, y=total_attacks.values, ax=axes[0, 0])
axes[0, 0].set_title("Number of Terrorist Attacks per Year")
axes[0, 0].set_xlabel("Year")
axes[0, 0].set_ylabel("Number of Attacks")
axes[0, 0].grid(True)
axes[0, 0].text(1975, max(total_attacks.values)*0.9, "Increase in attacks over the years", fontsize=12, color='blue')

# Subplot 2
sns.barplot(x=total_deaths.index, y=total_deaths.values, color='red', ax=axes[0, 1])
axes[0, 1].set_title("Number of Deaths due to Terrorist Attacks per Year")
axes[0, 1].set_xlabel("Year")
axes[0, 1].set_ylabel("Number of Deaths")
axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].grid(True)
axes[0, 1].text(1975, max(total_deaths.values)*0.9, "High fatalities in peak years", fontsize=12, color='red')

# Subplot 3
sns.barplot(x=top_countries.values, y=top_countries.index, palette='muted', ax=axes[1, 0])
axes[1, 0].set_title("Top 10 Countries by Number of Terrorist Attacks")
axes[1, 0].set_xlabel("Number of Attacks")
axes[1, 0].set_ylabel("Country")
axes[1, 0].grid(True, axis='x')
axes[1, 0].text(max(top_countries.values)*0.5, 8, "Most attacks in a few countries", fontsize=12, color='blue')

# Subplot 4
wedges, texts, autotexts = axes[1, 1].pie(attack_types.values, colors=colors, startangle=140, autopct='%1.1f%%', textprops=dict(color="w"))
axes[1, 1].legend(wedges, attack_types.index, title="Attack Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
axes[1, 1].set_title("Top 10 Attack Types")

fig.suptitle("Global Terrorism Analysis\nKhadiza Mahdin, Student ID: 22055871", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("22055871.png", dpi=300)

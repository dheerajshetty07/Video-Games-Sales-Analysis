
#Dheeraj Shetty
# Video Game Sales Analysis
# 21 Februrary 2025

#Import Libraries 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('vgsales.csv')

# Basic data cleaning
# Drop rows with missing critical values (e.g., Year, Genre)
df = df.dropna(subset=['Year', 'Genre'])

# Convert Year to integer
df.loc[:, 'Year'] = df['Year'].astype(int)

# Remove rows with Year > 2025 (outliers or errors)
df = df[df['Year'] <= 2025]

# Analysis 1: Top Genres by Global Sales 
top_genres = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).head(5)

print("Top 5 Genres by Global Sales (in millions):")

print(top_genres)

# Analysis 2: Regional Sales for Top Genres
top_genre_list = top_genres.index.tolist()

regional_sales = df[df['Genre'].isin(top_genre_list)].groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()

# Analysis 3: Top Platforms for Top Genres
platform_sales = df[df['Genre'].isin(top_genre_list)].groupby(['Genre', 'Platform'])['Global_Sales'].sum().unstack().fillna(0)

top_platforms = platform_sales.loc[top_genre_list].idxmax(axis=1)

print("\nTop Platform for Each Top Genre:")

print(top_platforms)

# Analysis 4: Sales Trends Over Time by Genre 
yearly_sales = df[df['Genre'].isin(top_genre_list)].groupby(['Year', 'Genre'])['Global_Sales'].sum().unstack().fillna(0)

#Analysis 5: Get top 10 games by Global_Sales

top_10_games = df.nlargest(10, 'Global_Sales')[['Name', 'Platform', 'Year', 'Genre', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']]
print("Top 10 Selling Video Games:")
print(top_10_games[['Name', 'Platform', 'Year', 'Genre', 'Global_Sales']].to_string(index=False))


# Visualization 1: Bar Plot of Top Genres by Global Sales
plt.figure(figsize=(10, 6))  
sns.barplot(x=top_genres.index, y=top_genres.values, palette='viridis')
plt.title('Top 5 Genres by Global Sales', fontsize=12)  
plt.xlabel('Genre', fontsize=10)  
plt.ylabel('Global Sales (Millions)', fontsize=10)
plt.xticks(rotation=0, fontsize=9)  
plt.yticks(fontsize=9)  
plt.tight_layout(pad=1.0)  
plt.savefig('top_genres_sales.png', dpi=300)  
plt.show()

# Visualization 2: Stacked Bar Plot of Regional Sales
plt.figure(figsize=(14, 8))  
regional_sales.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Regional Sales Distribution for Top Genres', fontsize=14)
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Sales (Millions)', fontsize=12)
plt.xticks(rotation=45, fontsize=10) 
plt.yticks(fontsize=10)
plt.legend(title='Region', fontsize=10, title_fontsize=12)  
plt.tight_layout(pad=1.5)  
plt.savefig('regional_sales.png', dpi=300)
plt.show()

# Visualization 3: Line Plot of Sales Trends Over Time
plt.figure(figsize=(16, 9))  
yearly_sales.plot(linewidth=2)
plt.title('Sales Trends by Genre (2000-2020)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Global Sales (Millions)', fontsize=12)
plt.xticks(fontsize=10)  
plt.yticks(fontsize=10)
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10, title_fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout(pad=1.5)  
plt.savefig('sales_trends.png', dpi=300)
plt.show()


# Visualization 4: Filter for top 5 genres and compute correlation matrix
top_genre_list = top_genres.index.tolist()
regional_corr = df[df['Genre'].isin(top_genre_list)].groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum().corr()

plt.figure(figsize=(10, 8))
sns.heatmap(regional_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, fmt='.2f')
plt.title('Correlation of Regional Sales for Top Genres', fontsize=14)
plt.tight_layout(pad=1.5)
plt.savefig('regional_corr_heatmap.png', dpi=300)
plt.show()


# Visualization 5 Boxplot of Sales Distribution by Genre (Top 5)
plt.figure(figsize=(12, 8))
sns.boxplot(x='Genre', y='Global_Sales', data=df[df['Genre'].isin(top_genre_list)], palette='Set3')
plt.title('Sales Distribution by Genre (Top 5)', fontsize=14)
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Global Sales (Millions)', fontsize=12)
plt.xticks(rotation=0, fontsize=10)
plt.yscale('log')  # Log scale to handle outliers better
plt.tight_layout(pad=1.5)
plt.savefig('sales_distribution_boxplot.png', dpi=300)
plt.show()

# Visualization 6 AreaPlot of Cumulative Sales by Genre Over Time

plt.figure(figsize=(14, 8))
yearly_sales.cumsum().plot(kind='area', alpha=0.5, colormap='viridis')
plt.title('Cumulative Sales by Genre Over Time', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Cumulative Global Sales (Millions)', fontsize=12)
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout(pad=1.5)
plt.savefig('cumulative_sales_area.png', dpi=300)
plt.show()


# Visualization 7: Horizontal Bar Plot of Global Sales 

plt.figure(figsize=(12, 8))

colors = ['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4', '#9467bd',
          '#90EE90', '#e377c2', '#800080', '#FFFF00', '#17becf']

top_10_games_reversed = top_10_games.iloc[::-1]

plt.barh(top_10_games_reversed['Name'], top_10_games_reversed['Global_Sales'], color=colors[::-1])  # Reverse colors too

for i, (name, platform, sales) in enumerate(zip(top_10_games_reversed['Name'], 
                                                top_10_games_reversed['Platform'], 
                                                top_10_games_reversed['Global_Sales'])):
    plt.text(0, i, f" ({platform})", va='center', ha='left', fontsize=10, color='black', alpha=0.7)
    plt.text(sales + 0.5, i, f'{sales:.1f}', va='center', fontsize=10)

plt.title('Top 10 Best-Selling Video Games by Global Sales', fontsize=14)
plt.xlabel('Global Sales (Millions)', fontsize=12)
plt.ylabel('Game Title', fontsize=12)
plt.tight_layout(pad=1.5)
plt.savefig('top_10_games_global.png', dpi=300)
plt.show()

#Clustering: Group Games by Sales Patterns

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns

# Prepare data (regional sales for top genres)
cluster_data = df[df['Genre'].isin(top_genre_list)][['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].dropna()

# Scale data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(cluster_data)

# --- Elbow Method to Determine Optimal Clusters ---
inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertias.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), inertias, marker='o')
plt.xlabel('Number of Clusters', fontsize=12)
plt.ylabel('Inertia', fontsize=12)
plt.title('Elbow Method for Optimal Clusters', fontsize=14)
plt.tight_layout()
plt.savefig('elbow_method.png', dpi=300)
plt.show()

# Apply K-Means with 3 clusters (based on elbow or prior analysis)
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_data)
cluster_data['Cluster'] = clusters

# Visualize with PCA (2D projection)
pca = PCA(n_components=2)
pca_data = pd.DataFrame(pca.fit_transform(scaled_data), columns=['PC1', 'PC2'])
pca_data['Cluster'] = clusters

plt.figure(figsize=(10, 8))
sns.scatterplot(x='PC1', y='PC2', hue='Cluster', data=pca_data, palette='deep')
plt.title('Game Clusters by Regional Sales Patterns', fontsize=14)
plt.xlabel('PC1: Sales Magnitude', fontsize=12)  # Interpret PC1 as overall sales
plt.ylabel('PC2: Regional Balance', fontsize=12)  # Interpret PC2 as regional distribution
plt.legend(title='Cluster', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
plt.tight_layout()
plt.savefig('sales_clusters_revised.png', dpi=300)
plt.show()

# Analyze clusters
print("Cluster Means (Average Regional Sales in Millions):")
print(cluster_data.groupby('Cluster').mean())

print("\nCluster Sizes:")
print(cluster_data['Cluster'].value_counts())

print("\nCluster Variability (Standard Deviation):")
print(cluster_data.groupby('Cluster').std())

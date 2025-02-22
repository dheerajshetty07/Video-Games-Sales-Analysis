# Video Games Sales Analysis: Insights and Trends (2025)

## Project Overview
This project analyzes the global video game sales dataset (vgsales.csv) to uncover trends, patterns, and insights that can guide game developers, publishers, and marketers. Using Python, Pandas, Matplotlib, Seaborn, and scikit-learn, I conducted a comprehensive descriptive analysis, visualized key findings, and applied advanced clustering to segment games by regional sales patterns. This repository contains the code, datasets, and visualizations for a portfolio-ready data analytics project, demonstrating skills in data cleaning, visualization, and unsupervised learning.

## Project Structure

- The project is organized into the following components:

**vgsales.csv**: The raw dataset from Kaggle, containing video game sales data (e.g., name, platform, genre, regional sales, global sales, year).

**VideoGamesSalesAnalysis.p**y: The main Python script performing all analyses and generating visualizations.

**Graphs**: High-resolution PNG files saved in the repository, showcasing visualizations of key insights (e.g., top_genres_sales.png, sales_clusters.png).

## Key Insights

## 1. Top Genres by Global Sales

Insight: Action and Sports genres dominate global sales, with Action leading at approximately 450 million units and Sports at 300 million units historically.

Visualization: This bar plot of Top 5 Genres by Global Sales highlights the most profitable genres for game developers.

![Image alt](https://github.com/dheerajshetty07/Video-Games-Sales-Analysis/blob/e34395ff96c83ebd9a24a1564153c94210e3c1a6/Graphs/top_genres_sales.png)


## 2. Regional Sales Distribution

Insight: North America (NA) and Europe (EU) drive the majority of sales for top genres, while Japan (JP) shows a preference for Role-Playing games. Other regions contribute modestly but consistently.

Visualization: This stacked bar plot of Regional Sales Distribution for Top Genres reveals regional market dominance.

![Image alt](https://github.com/dheerajshetty07/Video-Games-Sales-Analysis/blob/e34395ff96c83ebd9a24a1564153c94210e3c1a6/Graphs/regional_sales.png)

## 3. Sales Trends Over Time

Insight: Action genres maintain steady sales from 2000–2020, while Role-Playing shows growth potential, particularly post-2010, indicating emerging opportunities for developers.

Visualization: This line plot Sales Trends by Genre (2000-2020) tracks genre performance over time.

![Image alt](https://github.com/dheerajshetty07/Video-Games-Sales-Analysis/blob/e34395ff96c83ebd9a24a1564153c94210e3c1a6/Graphs/sales_trends.png)

## 4. Top 10 Best-Selling Video Games

Insight: Blockbusters like Wii Sports (82.74M global sales) and Super Mario Bros. (40.24M) dominate, primarily on the Wii and NES platforms, with NA and EU leading regional sales.

Visualization: This horizontal bar plot of Top 10 Best-Selling Video Games by Global Sales showcases individual game performance.

![Image alt](https://github.com/dheerajshetty07/Video-Games-Sales-Analysis/blob/e34395ff96c83ebd9a24a1564153c94210e3c1a6/Graphs/top_10_games_global.png)

## 5. Sales Distribution by Genre
Insight: Top genres like Action and Sports have wide sales distributions, with outliers (e.g., blockbusters) driving high variance, while Platform and Role-Playing show more consistent but lower sales.

Visualization: This box plot Sales Distribution by Genre (Top 5) illustrates variability and outliers.

![Image alt](https://github.com/dheerajshetty07/Video-Games-Sales-Analysis/blob/e34395ff96c83ebd9a24a1564153c94210e3c1a6/Graphs/sales_distribution_boxplot.png)

## 6. Cumulative Sales Growth
Insight: Cumulative sales for Action and Sports genres grow steadily, reinforcing their market dominance, while Role-Playing shows accelerating growth in recent years.

Visualization: This area plot of Cumulative Sales by Genre Over Time emphasizes long-term trends.

![Image alt](https://github.com/dheerajshetty07/Video-Games-Sales-Analysis/blob/e34395ff96c83ebd9a24a1564153c94210e3c1a6/Graphs/cumulative_sales_area.png)

## 7. Regional Sales Correlations
Insight: Strong positive correlations exist between NA and EU sales for top genres, but JP sales often correlate weakly, indicating distinct market preferences.

Visualization: The heatmap of Correlation of Regional Sales for Top Genres reveals regional interdependencies.

![Image alt](https://github.com/dheerajshetty07/Video-Games-Sales-Analysis/blob/e34395ff96c83ebd9a24a1564153c94210e3c1a6/Graphs/regional_corr_heatmap.png)

## 8. Game Clusters by Regional Sales Patterns
This analysis employs K-Means clustering to reveal three distinct market segments in video game regional sales, offering transformative insights for game developers and publishers. The largest cluster, visualized in blue (Cluster 0), comprises the majority of games with negligible sales across all regions, densely clustered near the origin on PC1 (Sales Magnitude) and PC2 (Regional Balance). 

These “Low-Selling” titles, typically niche or underperforming, represent the long tail of the industry, with average regional sales below 0.25 million units each. A second cluster, shown in orange (Cluster 1), spreads across positive PC1 values, indicating moderately successful games with strong sales in North America (NA) and Europe (EU), averaging around 4.33M in NA and 2.83M in EU, but limited sales in Japan (JP) and other regions—likely driven by platforms like Wii or PS2. Most notably, a single green point (Cluster 2) stands out far to the right on PC1, representing an extreme outlier—a blockbuster like Wii Sports—with massive sales dominated by NA (41.49M) and EU (29.02M), reflecting its global dominance on the Wii platform. This segmentation illuminates market opportunities, highlights the impact of blockbuster outliers, and underscores the diverse sales dynamics across regions, making it a cornerstone for strategic decision-making.

Game Clusters by Regional Sales Patterns (scatter plot): A PCA-reduced visualization (using PC1: Sales Magnitude and PC2: Regional Balance) displays three clusters—low sellers (dense blue cluster near origin), moderate sellers (spread orange cluster), and a blockbuster outlier (isolated green point)—colored vividly with a deep palette. This plot exemplifies the power of unsupervised learning to identify natural groupings in complex sales data.

![Image alt](https://github.com/dheerajshetty07/Video-Games-Sales-Analysis/blob/e34395ff96c83ebd9a24a1564153c94210e3c1a6/Graphs/sales_clusters.png)

Elbow Method for Optimal Clusters (line plot): A rigorous elbow curve justifies the choice of 3 clusters by plotting inertia against the number of clusters (1–10), showcasing a methodical approach to model selection and enhancing the analysis’s credibility.

![Image alt](https://github.com/dheerajshetty07/Video-Games-Sales-Analysis/blob/e34395ff96c83ebd9a24a1564153c94210e3c1a6/Graphs/elbow_method.png)

## Results and Insights
**Key findings from the analysis include:**

- **Genre Dominance:** Action and Sports genres lead global sales, with Action at approximately 450 million units and Sports at 300 million units, offering clear opportunities for developers.

- **Regional Trends:** North America and Europe drive the majority of sales for top genres, while Japan favors Role-Playing games, as shown in regional sales distributions.

- **Sales Trends:** Action maintains steady sales from 2000–2020, while Role-Playing shows growth potential post-2010, indicating emerging market opportunities.

- **Top Performers:** Blockbusters like Wii Sports (82.74M global sales) and Super Mario Bros. (40.24M) dominate, primarily on Wii and NES platforms, with NA and EU leading regional sales.

- **Sales Distribution:** Top genres exhibit wide sales variability, with outliers like Wii Sports driving high variance, as visualized in box plots.

- **Cumulative Growth:** Cumulative sales for Action and Sports grow steadily, reinforcing their market leadership, while Role-Playing accelerates in recent years.

- **Regional Correlations:** Strong positive correlations exist between NA and EU sales for top genres, but JP sales often correlate weakly, highlighting distinct market preferences.

- **Market Segmentation:** K-Means clustering identifies three groups—low-selling games (majority, negligible sales), moderately successful games (strong in NA/EU), and a blockbuster outlier (Wii Sports, dominating NA/EU sales)—providing strategic insights for market targeting and risk management.


## Repository Structure
```
Video-Games-Sales-Analysis/
├── graphs/                  # Visualizations generated during analysis (e.g., top_genres_sales.png, sales_clusters_revised.png)
├── scripts/                 # Python scripts for analyses and visualizations (e.g., video_game_sales_analysis.py)
├── README.md                # Project overview and instructions
└── data/                    # Contains the raw dataset (vgsales.csv)
```

## Requirements

- **Python: Version 3.8 or higher (recommended).**
- **Required libraries:**
- pandas
- matplotlib
- seaborn
- scikit-learn

## Usage

**Clone the repository:**

```bash
git clone https://github.com/dheerajshetty07/Video-Games-Sales-Analysis.git
```

For detailed insights, refer to the printed output and visualizations in the 'graphs/' directory.

**Data Source:** The data used in this project is sourced from the [Video Game Sales Dataset on Kaggle](https://www.kaggle.com/datasets/gregorut/videogamesales)

**Contributions:** Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or improvements.


For any questions, please contact [Dheeraj Shetty](https://github.com/dheerajshetty07)

# OpenFoodFacts Data Analysis

This project analyzes a large dataset of food products from [OpenFoodFacts](https://world.openfoodfacts.org/data). It includes data processing, simple analysis, and visualization.

This is my own application i created based on AI. All the code and the web is done myself.

## Features

- Downloads `.csv.gz` data from OpenFoodFacts
- Extracts and parses product categories
- Stores data in a local SQLite database
- Analyzes the top 5 most common product categories
- Visualizes results with an interactive bar chart (Plotly)
- Does **not require numpy or pandas**

## Project Structure and Steps

Tools & Technologies

- Python 3
- `urllib`, `gzip`, `csv`, `sqlite3`
- [`plotly`](https://plotly.com/python/) (for charting)

Sample Output

![Top 5 Categories](chart.png)  
*Or you can open `chart.html` for interactive chart*

How to Run

1. Clone or download this repo
2. Install requirements:
   ```bash
   pip install plotly
3. Run food_analysis.py to download, retrieve, collect data into SQLite and Excel 
4. Run food_chart.py to create model (Bar chart)

Please check the output in:
+) chart.html (final charts collected top 20 foods)
+) top_categories.txt (the top 5 categories)

This project uses data from OpenFoodFacts under the Open Database License (ODbL).
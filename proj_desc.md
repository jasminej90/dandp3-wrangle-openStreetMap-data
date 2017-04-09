# Udacity DAND P3: Wrangle OpenStreetMap Data with SQL
Data Analyst Nanodegree Project 3


In this project I use data munging techniques, such as assessing the quality of the data for validity, accuracy, completeness, consistency and uniformity, to clean a selected part of OpenStreetMap data (Riyadh, Saudi Arabia) using SQL.


## Files
* `quizes/` : python scripts for "Case Study: OpenStreetMap Data" exercises
* `riyadh_saudiArabia_map_sample.osm`: sample data of the OSM file
* `README.md` : md version of the whole data wrangling process
* `mapparser.py` : parse OSM file to count unique tags
* `tags.py` : categorize tags in the OSM file
* `audit.py` : audit street addresses, and update their names
* `data.py` : build CSV files from XML OSM data to insert them into SQL db, as well as clean and shape the data
* `database.py` : create an SQL database from CSV files

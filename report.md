
# OpenStreetMap Data Case Study

### Map Area
Riyadh, Kingdom of Saudi Arabia

- [OpenStreetMap URL](https://www.openstreetmap.org/export#map=10/24.7050/46.9061)
- [MapZen Sample URL](https://mapzen.com/data/metro-extracts/metro/riyadh_saudi-arabia/)

This map is of the capital city of my home country, Saudi Arabia. The capital, Riyadh, is near from my hometown.


## 1. Data Auditing
After downloading a subset of my OSM dataset, I started by auditing the data broadly. I looked at all the tags in the XML file and classified the.

### map parser
Here, I'm getting a feeling on how much of which data we have in the downloaded OSM dataset. `mapparser.py` file is used to count the total number of every unique tag in the OSM file, using ElementTree iterative parsing.
 
```
    {'bounds': 1,
     'member': 652,
     'meta': 1,
     'nd': 513971,
     'node': 366975,
     'note': 1,
     'osm': 1,
     'relation': 133,
     'tag': 150654,
     'way': 78723}

```

### Tag types
For all the elements that contain tags, I decided to check the `"k"` value for each and see if there are any potential problems by defining the below five tag categories as regular expressions in `tags.py` file.

tag category | count | desc.
--- | --- | ---
`lower` |  144723 | for tags that contain only lowercase alphanumeric letters and are valid.
`lower_colon` | 5911 | for otherwise valid alphanumeric tags with a colon in their names.
`upper` | 6 | for otherwise valid upper case letters tags.
`problemchars` | 1 | for tags with problematic characters
`other` | 13 | for other tags that do not fall into the other three categories

I've noticed one tag with a problematic character, thirteen that don't belong to any of the above categories. When I printed some of them, here's what I found
```
Transport
Fixme:de
اللويمي
addr:country:SA
ISO3166-1
ISO3166-1:alpha2
```
They either mix upper with lowercase letters and numeric, include more than one colon, or written in Arabic.

## 2. Problems Encountered in the Map

To narrow it down, I decided to audit the street names only in my OSM dataset. `audit.py` is used to check for any inconsistencies. I've noticed that the street names are written in two languages, Arabic and English, and so I've detected the following main problems in the dataset:

- Inconsistent Street Naming Languages:
  - `Arabic` -> `شارع معاوية بن أبي سفيان`
  - `English` -> `Imam Saud Street`
 
 ### Problems with Arabic Street Names:
  - Written from right to left
    - `شارع معاوية بن أبي سفيان`
  - Missing keywords `street/road` before the name:
    - `{{'عبد': {'عبد العزيز بن مساعد بن جلوي'}`
    
### Problems with English Street Names:
  - Abbreviations:
    - `St. , St` -> `Street`
    - `Pr.` -> `Prince`
  - Lower case:
    - `street` -> `Street`
    - `road` -> `Road`
  - St/Rd keywords are in the middle of the street name:
    - `Uthman Ibn Affan Branch Rd, At Taawun, Riyadh 12478`
  - Inconsistent lower and upper letter cases:
    - `Al kharj road`  `Al Jazi Valley`
  - Inconsistent spelling for the same word:
    - `Abdulaziz`  `Abdul Aziz`
  - Missing keywords `street/road` at the end of the name:
    - `Ibn Shamil`
  - Incorrect street names:
    - `No. 6` -> `6th Street`

## 3. Data Cleaning
In this section, `data.py` file is used to convert XML map file to CSV. Parsing, cleaning, and shaping the dataset is also occuring while converting the data format. Then, the clean dataset is imported into an SQL database using a specificed schema.

## 4. Data Overview
This section includes general stats about the dataset, and the SQL queries used to collect the data.

### File sizes
```
```

### Number of
#### a) nodes
```
```

#### b) ways
```
```

#### c) relations
```
```

### Number of unique users
```
```

### Top 10 contributing users
```
```

### Number of users appearing only once (having 1 post)
```
```


## 5. Additional Exploration

### Top 10 ammenities
```
```

### Biggest religion
```
```

### Most popular cuisines
```
```


## 6. Conclusion

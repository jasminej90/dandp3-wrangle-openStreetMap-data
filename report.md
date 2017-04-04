
# OpenStreetMap Data Case Study

### Map Area
Riyadh, Kingdom of Saudi Arabia

- [OpenStreetMap URL](https://www.openstreetmap.org/export#map=18/26.30400/50.19602)
- 

This map is of the capital city of my home country, Saudi Arabia. The capital, Riyadh, is near from my hometown.


## 1. Data Auditing

### map parser
To get a feeling on how much of which data we have in the downloaded OSM dataset, using ElementTree iterative parsing, the total number of every unique tag is counted using `mapparser.py` file.
 
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
Then, for all of the above tags, I check the `"k"` value for each and see if there are any potential problems by defining the below four tag categories, using `tags.py` file.

tag category | count | desc.
--- | --- | ---
`lower` |  144720 | for tags that contain only lowercase letters and are valid.
`lower_colon` | 5310 | for otherwise valid tags with a colon in their names
`problemchars` | 1 | for tags with problematic characters
`other` | 623 | for other tags that do not fall into the other three categories

## 2. Problems Encountered in the Map

- Arabic Names:
    - `شارع` -> `Street`
    - `طريق` -> `Road`
- Abbreviations:
    - `St.` -> `Street`
    - `Rd` -> `Road`

## 3. Data Overview
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


## 4. Additional Ideas

### Top 10 ammenities
```
```

### Biggest religion
```
```

### Most popular cuisines
```
```


## 5. Conclusion

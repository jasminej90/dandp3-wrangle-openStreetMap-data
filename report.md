
# OpenStreetMap Data Case Study

### Map Area
Riyadh, Kingdom of Saudi Arabia

- [OpenStreetMap URL](https://www.openstreetmap.org/export#map=10/24.7050/46.9061)
- [MapZen Sample URL](https://mapzen.com/data/metro-extracts/metro/riyadh_saudi-arabia/)

This map is of the capital city of my home country, Saudi Arabia. The capital, Riyadh, is near from my hometown.


## 1. Data Auditing | Closer Look

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
Then, for all of the above tags, I check the `"k"` value for each and see if there are any potential problems by defining the below four tag categories as regular expressions in `tags.py` file.

tag category | count | desc.
--- | --- | ---
`lower` |  144720 | for tags that contain only lowercase letters and are valid.
`lower_colon` | 5310 | for otherwise valid tags with a colon in their names
`problemchars` | 1 | for tags with problematic characters
`other` | 623 | for other tags that do not fall into the other three categories


## 2. Problems Encountered in the Map
As I noticed that there is one problematic character and more than 500 tags that do not fall into any category, I printed them to understand what is going on.

- Problem chars:
```
name 12/30
```

- Undefined tags (other category):

```
name:ar1
name:be-tarask
fuel:octane_91
fuel:octane_95
fuel:octane_92
Transport
Fixme
Fixme:de
amenity_1
اللويمي
addr:country:SA
name:en1
website_1
par_1
name 12/30
البلدية
ISO3166-1
ISO3166-1:alpha2
ISO3166-1:alpha3
ISO3166-1:numeric
name:bat-smg
name:fiu-vro
name:roa-rup
name:roa-tara
name:zh-classical
name:zh-min-nan
name:zh-yue
ISO3166-2
ISO3166-2
```

Inconsistencies
`audit.py`

- Arabic Names:
    - `شارع` -> `Street`
    - `طريق` -> `Road`
- Abbreviations:
    - `St.` -> `Street`
    - `Rd` -> `Road`

## 3. Data Cleaning

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

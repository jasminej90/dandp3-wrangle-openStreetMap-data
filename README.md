
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

### Handling Street Names
    
```python
street_type_re = re.compile(r'\b[a-zA-Z]+\.?$', re.IGNORECASE)
street_type_ar_re = re.compile(r'([\u0621-\u06FF]+)')
```
Using regular expressions, I was able to parse each street name language seperately. However, the task turned out to be very costly and beyond the scope of this exercise. Hence, I decided to focus only on the english street names.

```python
def update_name(name, mapping):

	if name in mapping:
		name = mapping[name]

	else:
	    name = name.split(' ')

	    for i in range(len(name)):
	        if name[i] in mapping:
	        	name[i] = mapping[name[i]]
	        	name[i] = string_case(name[i])
	        else:
	            name[i] = string_case(name[i])

	    # Does it contain street keyword?
	    if (name[len(name) - 1] not in expected) & ('Road' not in ' '.join(name)):
	    	name = ' '.join(name) + " Street"
	    else:
	    	name = ' '.join(name)

	return name
 ```
 Using the above update function, I updated all the bad street names either by mapping them to better written names, capitalizing the first letters, or attaching street keyword at the end.

## 3. Data Cleaning
In this section, `data.py` file is used to convert XML map file to CSV files. Parsing, cleaning, and shaping the XML OSM data into python dictionaries using a specificed schema is also occuring while converting the data format. Then, the clean dataset is imported into an SQL database using `database.py` file.

## 4. Data Overview
This section includes general stats about the dataset, and the SQL queries used to collect the data.

### File sizes
```
riyadh_saudiArabia_map.osm ......... 87 MB
riyadh.db .......... 127.7 MB
nodes.csv ............. 30.6 MB
nodes_tags.csv ........ 906 KB
ways.csv .............. 4.7 MB
ways_tags.csv ......... 4.6 MB
ways_nodes.cv ......... 12.4 MB
```

### Number of nodes
```sql
sqlite> SELECT COUNT(*) FROM nodes;
```
1100925

#### Number of ways
```sql
sqlite> SELECT COUNT(*) FROM ways;
```
78723

### Number of unique users
```sql
sqlite> SELECT COUNT(DISTINCT(e.uid))          
FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e;
```
736

### Top 10 contributing users
```sql
sqlite> SELECT e.user, COUNT(*) as num
FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e
GROUP BY e.user
ORDER BY num DESC
LIMIT 10;
```
```sql
Seandebasti|452129
mustafakamil|182980
Rub21|101079
bauma|86351
Cicerone|66423
Dugoon|28606
Khaled AlOtaibi|27109
keepright! ler|23822
derden|19269
t_woelk|16987
```

### Number of users appearing only once (having 1 post)
```sql
sqlite> SELECT COUNT(*) 
FROM
    (SELECT e.user, COUNT(*) as num
     FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e
     GROUP BY e.user
     HAVING num=1)  u;
```
39

## 5. Additional Exploration
This section includes more SQL queries for further exploration of the city.

### Top 10 ammenities
```sql
sqlite> SELECT value, COUNT(*) as num
FROM nodes_tags
WHERE key='amenity'
GROUP BY value
ORDER BY num DESC
LIMIT 10;
```
```sql
place_of_worship|434
fuel|259
restaurant|231
parking|203
school|88
embassy|75
bank|71
atm|67
cafe|67
fast_food|64
```

### Biggest religion
```sql
sqlite> SELECT nodes_tags.value, COUNT(*) as num
FROM nodes_tags 
    JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value='place_of_worship') i
    ON nodes_tags.id=i.id
WHERE nodes_tags.key='religion'
GROUP BY nodes_tags.value
ORDER BY num DESC
LIMIT 1;
```
```sql
muslim|421
```

### Most popular cuisines
```sql
sqlite> SELECT nodes_tags.value, COUNT(*) as num
FROM nodes_tags 
    JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value='restaurant') i
    ON nodes_tags.id=i.id
WHERE nodes_tags.key='cuisine'
GROUP BY nodes_tags.value
ORDER BY num DESC;
```
```sql
regional|50
pizza|13
chicken|5
sandwich|4
burger|3
italian|3
arabic|2
indian|2
kebab|2
BurgerFuel|1
Grilled_&_Barbecue|1
Malabari_Cuisine|1
american|1
arab|1
arab;persian|1
arab;sandwich;tea;coffee_shop|1
buffet|1
chinese|1
coffee_shop|1
french|1
friture|1
friture;burger;sandwich|1
ice_cream|1
indonesian|1
international|1
italian_pizza|1
lebanese|1
lebanon|1
local|1
oriental;arab;local|1
seafood|1
```

## 6. Additional Ideas
- Since the language was a challenge in this exercise, I suggest either forcing rules on the contributers to ensure including the english street name. Otherwise, upgrade OpenStreetMap code to include a seamless translation to english once a street name is inputted in a different language.

- The other way to deal with different languages in OpenStreetMap data is to import translation service from Google Translate API. In fact, I succeeded in doing so, it was very straight forward 

Installation
------------

::
   pip install translate

Or, you can download the source and

::
   python setup.py install


Command-Line Usage
------------------

In your command-line:

::
   yasmin$ translate -t eng -f ar "شارع معاوية ابن أبي سفيان"

Output

::
   yasmin$ translate -t eng -f ar "شارع معاوية ابن أبي سفيان"

However, this might introduce another type of problems. For example, in the case of wrong or missing translations, that will lead to misinterpreted data in the database. One possible solution is to apply regular expression checks after translation to ensure that the street name is in proper format.


## 7. Conclusion
Dealing with Riyadh dataset was challenging due to the inconsistent language usage in naming the streets. Arabic street names are written from right to left, any special treatments that apply to them will not work on the english names. and so for the sake of handling this project's scope, I decided to discard the arabic names. In addiation, there were a lot of inconsistencies in terms of street naming. However, the chosen dataset was cleaned properly for this exerciese, but there is a huge area left for improvement. In the future, I was considering importing a translation service from Google Translate API to translate all arabic street names.


## 8. References
- [1] https://github.com/terryyin/google-translate-python

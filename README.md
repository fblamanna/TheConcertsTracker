# The Concerts / Setlists Tracker

## The Concerts Tracker

### Get concerts information from setlist.fm database

***TheConcertsTracker.py*** script returns a .csv file with all information about the concerts for a single band or artist, available on the [setlist.fm](http://www.setlist.fm/) website. You need to apply for a **setlist.fm API key** to download data and use them; they are free for non-commercial projects. You can get it [here](https://api.setlist.fm/docs/1.0/index.html). Please read the [API Terms of Use](http://www.setlist.fm/help/terms) carefully.

#### Input

The script takes as input the artist name (just for naming the output file) and the [Musicbrainz MBID](https://musicbrainz.org/doc/MusicBrainz_Database) code, which is an identifiable code for each artist or band in the database. I'm now working on an automatic call artist name - code. In the meantime you have to manually add the code available on the Musicbrainz website.

##### Parameters:
artistname: name of the artist or band (string)  
artistcode: Musicbrainz MBID (string)  
API_KEY: Setlist.fm valid API Key
 
#### Output

The algorithm returns a csv file with column names, **the value separator is a semicolon ";"**. The fields are the following:

1. **ID** ID of the concert
2. **artist** artist / band name
3. **eventdate** datetime object of the event
4. **tourname** name of the Tour
5. **venue** name of the venue of the show
6. **venue_id** ID of the venue
7. **city** City where the show is located
8. **city_id** ID of the city
9. **city_lat** Latitude of the city
10. **city_lon** Longitude of the city
11. **state** State name
12. **state_id** ID of the State
13. **country** Country name
14. **country_id** ID of the country

If a field information is missing, the code returns None for that value.

#### Execution

The script now runs on Python 3.x only. You can run the code using the command:  
```$ python TheConcertsTracker.py 'artistcode' 'artistname' 'API_KEY'```

#### Sample Output
```python TheConcertsTracker.py '5441c29d-3602-4898-b1a1-b77fa23b8e50' 'David Bowie' 'API_KEY'```

```
eventID;artist;eventdate;tourname;venue;venue_id;city;city_id;city_lat;city_lon;state;state_id;country;country_id
3bd5f8b0;David Bowie;25-06-2004;A Reality Tour;Eichenring;33d6c80d;Scheeßel;2840070;53.1666667;9.4833333;Lower Saxony;06;Germany;DE
13d2d1e1;David Bowie;23-06-2004;A Reality Tour;T-Mobile Arena;43d62b7f;Prague;3067696;50.0878367932108;14.4241322001241;Hlavní Mesto Praha;52;Czech Republic;CZ
bd2d1e2;David Bowie;20-06-2004;A Reality Tour;Törnävä;2bd6d4ba;Seinäjoki;642149;62.5666667;23.0666667;Western Finland;15;Finland;FI
3d2d1e3;David Bowie;18-06-2004;A Reality Tour;Frognerbadet;2bd628ce;Oslo;6942479;59.912697157616;10.7413673400879;Oslo;12;Norway;NO
1bd2d1ec;David Bowie;17-06-2004;A Reality Tour;Ole Bergen Festival;43d64f17;Bergen;3161732;60.3931603404213;5.3242814540863;Hordaland;07;Norway;NO
bd7250e;David Bowie;11-06-2004;A Reality tour;ArenA;5bd6379c;Amsterdam;2759794;52.373;4.9;North Holland;07;Netherlands;NL
...
```

#### Version History
22.07.2016 - Version 0.1  
27.12.2016 - Version 0.2 - Fixing bugs while reading .json  
31.08.2017 - Version 0.3 - Adding Compatibility with Setlist.fm API 1.0
26.05.2018 - Version 0.4 - Handle missing json fields - Drop Python 2 support

## The Setlists Tracker

### Get information about songs played in concerts from setlist.fm database

***TheSetlistsTracker.py*** script script returns a .csv file with all information about the songs played in a concert for a single band or artist, available on the [setlist.fm](http://www.setlist.fm/) website. You need to apply for a **setlist.fm API key** to download data and use them; they are free for non-commercial projects. You can get it [here](https://api.setlist.fm/docs/1.0/index.html). Please read the [API Terms of Use](http://www.setlist.fm/help/terms) carefully.

#### Input

The script takes as input the artist name (just for naming the output file) and the [Musicbrainz MBID](https://musicbrainz.org/doc/MusicBrainz_Database) code, which is an identifiable code for each artist or band in the database. I'm now working on an automatic call artist name - code. In the meantime you have to manually add the code available on the Musicbrainz website.

##### Parameters:
artistname: name of the artist or band (string)  
artistcode: Musicbrainz MBID (string)  
API_KEY: Setlist.fm valid API Key

#### Output
A .csv file with the following fields:

1. **eventID** ID of the event
2. **song** song played
3. **set** type of set: 0 - Main Set; 1,2,3 etc. - Encore Number

If a field information is missing, the code returns None for that value.

#### Execution

You can run the code using the command:  
```$ python TheSetlistsTracker.py 'artistcode' 'artistname' 'API_KEY'```

#### Sample Output
```python TheSetlistsTracker.py '8538e728-ca0b-4321-b7e5-cff6565dd4c0' 'Depeche Mode' 'API_KEY'```

```
eventID;song;set
73d7da3d;In Chains;0
73d7da3d;Wrong;0
73d7da3d;Hole to Feed;0
73d7da3d;Walking in My Shoes;0
73d7da3d;It's No Good;0
73d7da3d;A Question of Time;0
73d7da3d;Precious;0
73d7da3d;Fly on the Windscreen;0
73d7da3d;Home;0
73d7da3d;Come Back;0
73d7da3d;Peace;0
73d7da3d;In Your Room;0
73d7da3d;I Feel You;0
73d7da3d;Enjoy the Silence;0
73d7da3d;Never Let Me Down Again;0
73d7da3d;Stripped;1
73d7da3d;Personal Jesus;1
...
```

## Questions / Issues
Contacts and Info: [www.fabiolamanna.it](http://www.fabiolamanna.it)

##
Copyright (c) 2017 Fabio Lamanna. Code under License GPLv3.



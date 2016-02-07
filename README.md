# Get concerts information for artists and bands from setlist.fm database

This Python script returns a .csv file with all information about the concerts for a single band or artist, available on the [setlist.fm](http://www.setlist.fm/) website. You need to apply for a **setlist.fm API key** to download data and use them; they are free for non-commercial projects. You can get it [here](http://api.setlist.fm/docs/index.html). Please read the [API Terms of Use](http://www.setlist.fm/help/terms) carefully.

## Input

The algorithm takes as input the artist name (just for naming the output file) and the [Musicbrainz MBID](https://musicbrainz.org/doc/MusicBrainz_Database) code, which is an identifiable code for each artist or band in the database. I'm now working on an automatic call artist name - code. In the meantime you have to manually add the code available on the Musicbrainz website.

## Parameters

artistname = name of the artist or band (in quotation marks)  
artistcode = Musicbrainz MBID (in quotation marks)  
 
## Output

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

## Execution

You can run the code using the command:  
*python ConcertsTimeline.py 'artistcode' 'artistname'*  

## Sample Output
```python ConcertsTimeline.py '5441c29d-3602-4898-b1a1-b77fa23b8e50' 'David Bowie'```

```
ID,artist,eventdate,tourname,venue,venue_id,city,city_id,city_lat,city_lon,state,state_id,country,country_id
3bd5f8b0,David Bowie,25-06-2004,A Reality Tour,Eichenring,33d6c80d,Scheeßel,2840070,53.1666667,9.4833333,Lower Saxony,06,Germany,DE
13d2d1e1,David Bowie,23-06-2004,A Reality Tour,T-Mobile Arena,43d62b7f,Prague,3067696,50.0878367932108,14.4241322001241,Hlavní Mesto Praha,52,Czech Republic,CZ
bd2d1e2,David Bowie,20-06-2004,A Reality Tour,Törnävä,2bd6d4ba,Seinäjoki,642149,62.5666667,23.0666667,Western Finland,15,Finland,FI
3d2d1e3,David Bowie,18-06-2004,A Reality Tour,Frognerbadet,2bd628ce,Oslo,6942479,59.912697157616,10.7413673400879,Oslo,12,Norway,NO
1bd2d1ec,David Bowie,17-06-2004,A Reality Tour,Ole Bergen Festival,43d64f17,Bergen,3161732,60.3931603404213,5.3242814540863,Hordaland,07,Norway,NO
bd7250e,David Bowie,11-06-2004,A Reality tour,ArenA,5bd6379c,Amsterdam,2759794,52.373,4.9,North Holland,07,Netherlands,NL
```

## Citation

## References

## Questions / Issues
Contacts and Info: [www.fabiolamanna.it](http://www.fabiolamanna.it)

##
Copyright (c) 2016 Fabio Lamanna. Code under License GPLv3.



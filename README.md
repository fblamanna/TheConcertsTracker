# Get concerts information for artists and bands from setlist.fm database
=========================================================================

This Python script returns a .csv file with all information about the concerts for a single band or artist, available on the [setlist.fm](http://www.setlist.fm/) website. You need to apply for a **setlist.fm API key** to download data and use them; they are free for non-commercial projects. You can get it [here](http://api.setlist.fm/docs/index.html). Please read the [API Terms of Use](http://www.setlist.fm/help/terms) carefully.

## Input

The algorithm takes as input the artist name (just for naming the output file) and the Musicbrainz MBID (https://musicbrainz.org/doc/MusicBrainz_Database) code, which is an identifiable code for each artist or band in the database. I'm now working on an automatic call artist name - code. In the meantime you have to manually add the code available on the Musicbrainz website.

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

## Citation

## References

## Questions / Issues
Don't hesitate to contact me at [fabio@fabiolamanna.it](mailto:fabio@fabiolamanna.it)

##
This code is released under the MIT License (MIT)

Copyright (c) 2016 Fabio Lamanna



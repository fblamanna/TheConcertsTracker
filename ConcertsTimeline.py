# encoding: utf-8

##
# This Python script returns a .csv file with all information about the concerts for a single band or artist, 
# available on the [setlist.fm](http://www.setlist.fm/) website.
# You need to apply for a **setlist.fm API key** to download data and use them; they are free for non-commercial projects.
# You can get it [here](http://api.setlist.fm/docs/index.html). Please read the [API Terms of Use](http://www.setlist.fm/help/terms) carefully.

## Input ##
# The algorithm takes as input the artist name (just for naming the output file) and the [Musicbrainz MBID](https://musicbrainz.org/doc/MusicBrainz_Database) code,
# which is an identifiable code for each artist or band in the database.
# I'm now working on an automatic call artist name - code. In the meantime you have to manually add the code available on the Musicbrainz website.

## Parameters ##
# artistname = name of the artist or band (in quotation marks)  
# artistcode = Musicbrainz MBID (in quotation marks)  

# Copyright (c) 2016 Fabio Lamanna (fabio@fabiolamanna.it). Code under License GPLv3.

__author__ = """ Fabio Lamanna (fabio@fabiolamanna.it) """

# Import Modules
try:
	import ujson as json
except:
	import json

import urllib2
import csv
import sys

# Returns an artist for a given Musicbrainz MBID
# https://musicbrainz.org/doc/MusicBrainz_Database
# e.g.
# artistcode = '5441c29d-3602-4898-b1a1-b77fa23b8e50'
# artistname = 'David Bowie'
artistcode = sys.argv[1]
artistname = sys.argv[2]

def main():

	# Set Workbooks for .csv
	f = open(artistname + 'ConcertsTimeline.csv', 'wt')

	# Inizialize .csv file
	writer = csv.writer(f, delimiter=';')

	# Write .csv headers
	writer.writerow( 
	                (
	                'ID',
	                'artist',
	                'eventdate',
	                'tourname',
	                'venue',
	                'venue_id',
	                'city',
	                'city_id',
	                'city_lat',
	                'city_lon',
	                'state',
	                'state_id',
	                'country',
	                'country_id'
	                )
	                )

	# Call Setlist.fm API
	response = urllib2.urlopen('http://api.setlist.fm/rest/0.1/artist/' + artistcode + '/setlists.json?p=1')
	data = json.load(response)

	# Get total number of shows
	totalshows = int(data['setlists']['@total'])

	# Total Number of Pages needed to load
	pages = int(totalshows/20)

	for page in range(1,pages):

		data = urllib2.urlopen('http://api.setlist.fm/rest/0.1/artist/' + artistcode + '/setlists.json?p=' + str(page))

		# Read .json file line per line
		for line in data:

			data = json.loads(line)

			for i in range(len(data['setlists']['setlist'])):

				try:

					writer.writerow(
					                (
					                # Event ID
					                str(data["setlists"]["setlist"][i]["@id"]),
					                # Artist
					                str(data['setlists']['setlist'][i]["artist"]["@name"]),
					                # Eventdate
					                str(data["setlists"]["setlist"][i]["@eventDate"]),
					                # TourName
					                unicode(data["setlists"]["setlist"][i]["@tour"]).encode('utf-8'),
					                # Venue
					                unicode(data["setlists"]["setlist"][i]["venue"]["@name"]).encode('utf-8'),
					                # Venue ID
					                str(data["setlists"]["setlist"][i]["venue"]["@id"]),
					                # City
					                unicode(data["setlists"]["setlist"][i]["venue"]["city"]["@name"]).encode('utf-8'),
					                # City ID
					                str(data["setlists"]["setlist"][i]["venue"]["city"]["@id"]),
					                # City Latitude
					                float(data["setlists"]["setlist"][i]["venue"]["city"]["coords"]["@lat"]),
					                # City Longitude
					                float(data["setlists"]["setlist"][i]["venue"]["city"]["coords"]["@long"]),
					                # State
					                unicode(data["setlists"]["setlist"][i]["venue"]["city"]["@state"]).encode('utf-8'),
					                # State Code
					                str(data["setlists"]["setlist"][i]["venue"]["city"]["@stateCode"]),
					                # Country
					                unicode(data["setlists"]["setlist"][i]["venue"]["city"]["country"]["@name"]).encode('utf-8'),
					                # Country Code
					                unicode(data["setlists"]["setlist"][i]["venue"]["city"]["country"]["@code"]).encode('utf-8')
					                )
					                )

				except:
					pass

	f.close()

if __name__ == '__main__':

	main()




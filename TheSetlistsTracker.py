#
# This Python script returns a .csv file with all information about the songs played in concerts by single bands or artists, 
# available on the [setlist.fm](http://www.setlist.fm/) website.
# You need to apply for a setlist.fm API key to download data and use them; they are free for non-commercial projects.
# You can get it here: http://api.setlist.fm/docs/index.html. 
# Please read the API Terms of Use (http://www.setlist.fm/help/terms) carefully.
#
# The algorithm takes as input the artist name (just for naming the output file) and 
# the Musicbrainz MBID (https://musicbrainz.org/doc/MusicBrainz_Database) code,
# which is an identifiable code for each artist or band in the database.
# I'm now working on an automatic call artist name - code. 
# In the meantime you have to manually add the code available on the Musicbrainz website.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
__author__ = ''' Fabio Lamanna (fabio@fabiolamanna.it) '''
#
#########################################################################
#
# Copyright (c) 2017 Fabio Lamanna (fabio@fabiolamanna.it). 
# Code under License GPLv3.
#
# Version History:
# 22.07.2016 - Version 0.1
# 27.12.2016 - Version 0.2 - Fixing bugs while reading .json
# 31.08.2017 - Version 0.3 - Adding Compatibility with Setlist.fm API 1.0
# 26.05.2018 - Version 0.4 - Handle missing json fields - Drop Python 2 support
#
# Input Parameters:
# artistname: name of the artist or band (string)  
# artistcode: Musicbrainz MBID (string)
# API_KEY: Setlist.fm valid API Key
#
# Execution:
# You can run the code using the command:  
# $ python TheSetlistsTracker.py 'artistcode' 'artistname' 'API_KEY'
#
#########################################################################

# Import Modules
try:
	import ujson as json
except:
	import json

import requests
import csv
import sys
import math

#########################################################################

def main():

	# Set Workbooks for .csv
	f = open(sys.argv[2] + 'SetlistsTracker.csv', 'wt', encoding='utf-8')

	# Write .csv Headers
	writer = csv.writer(f, delimiter=';')

	writer.writerow( 
	                (
	                'eventID',
	                'song',
	                'set'
	                )
	                )

	# Call Setlist.fm API
	url = 'https://api.setlist.fm/rest/1.0/artist/' + sys.argv[1] + '/setlists?p=1'
	headers = {'Accept': 'application/json', 'x-api-key': sys.argv[3]}
	r = requests.get(url, headers=headers)
	
	# Get .json Data
	data = r.json()

	# Get total number of shows and handle missing shows
	try:
		
		totalshows = int(data['total'])

	except:
		print('Sorry, the artist you are looking for has no concerts in the database')
		sys.exit(1)

	# Total Number of Pages needed to load
	pages = int(math.ceil(totalshows/20))

	for page in range(1,pages):

		url = 'https://api.setlist.fm/rest/1.0/artist/' + sys.argv[1] + '/setlists?p=' + str(page)
		headers = {'Accept': 'application/json', 'x-api-key': sys.argv[3]}
		r = requests.get(url, headers=headers)
	
		# Get .json Data
		data = r.json()

		for line in data:

			# Loop through each setlist
			for i in range(len(data['setlist'])):

				# No Data Available
				if data['setlist'][i]['sets'] == '':

					writer.writerow(
					                (
					                # Event ID
					                data['setlist'][i]['id'],
					                # Songs
					                'None',
					                # Set
					                'None'
					                )
					                )

				else:

					for j in data['setlist'][i]['sets']:

						# Check for number of sets (Main, Encore(s))
						numberofsets = len(data['setlist'][i]['sets']['set'])

						if numberofsets == 1:

							try:

								for k in data['setlist'][i]['sets']['set']['song']:

									try:

										writer.writerow(
										                (
										                # Event ID
										                data['setlist'][i]['id'],
										                # Songs
										                k['name'],
										                # Set
										                '0'
										                )
										                )

									except:

										writer.writerow(
										                (
										                # Event ID
										                data['setlist'][i]['id'],
										                # Songs
										                data['setlist'][i]['sets']['set']['song']['name'],
										                # Set
										                '0'
										                )
										                )

							except:

								writer.writerow(
								                (
								                # Event ID
								                data['setlist'][i]['id'],
								                # Songs
								                'None',
								                # Set
								                'None'
								                )
								                )

						# Case numberofsets > 1
						elif numberofsets > 1:

							for s in range(numberofsets):

								try:

									for k in data['setlist'][i]['sets']['set'][s]['song']:

										try:

											writer.writerow(
											                (
											                # Event ID
											                data['setlist'][i]['id'],
											                # Songs
											                k['name'],
											                # Set
											                s
											                )
											                )

										except:

											writer.writerow(
											                (
											                # Event ID
											                data['setlist'][i]['id'],
											                # Songs
											                data['setlist'][i]['sets']['set'][s]['song']['name'],
											                # Set
											                s
											                )
											                )

								except:

									writer.writerow(
									                (
									                # Event ID
									                data['setlist'][i]['id'],
									                # Songs
									                'None',
									                # Set
									                'None'
									                )
									                )

	f.close()

if __name__ == '__main__':

	main()





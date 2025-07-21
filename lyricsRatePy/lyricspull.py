#from chartlyrics import ChartLyricsClient
#import csv

#client = ChartLyricsClient()
#women = ["Mary", "Sally", "Jane", "Jean", "Ruby", "Ann", "Annie", "Beverly", "Taylor", "Rose",
         #"Grace", "Jackie", "Maria", "Georgia", "Dawn", "Bonnie", "Marie", "Laura", "Linda", "Jenny",
         #"Billie", "Sue", "Molly", "Judy", "Donna", "Betty", "Barbara", "Delilah", "Daisy", "Pearl",
         #"Carrie", "Julie", "Alice", "Virginia", "Lisa", "Susan", "Susie", "Mae", "Autumn", "Lorraine",
         #"Sherry", "Lucy", "Sheila", "Caroline", "Cindy", "Diana", "Diane", "Jennifer", "Roxanne"]
#
#results = []
#for name in women:
    #print(f"Searching for songs with '{name}'...")
    #song_count = 0
    #for song in client.search_text(name):
	#print(song.artist)
	#print(song.song)
        #song_count += 1
    #results.append([name, song_count])
    #print(f"Found {song_count} songs for '{name}'")
#
#with open('women_songs_count.csv', 'w', newline='') as csvfile:
    #writer = csv.writer(csvfile)
    #writer.writerow(['Name', 'Song Count'])
    #writer.writerows(results)
#
#print("\nResults saved to women_songs_count.csv")


#for song in client.search_text("Carrie"):
#	print(song.artist)
#	print(song.song)
#	print("")

#print(client.search_text("Carrie God"))

#print(client.search_lyric(artist="Europe", song="Carrie"))


from zeep import Client

# Create SOAP client from ChartLyrics WSDL
wsdl_url = "http://api.chartlyrics.com/apiv1.asmx?WSDL"
client = Client(wsdl=wsdl_url)

# Call the SearchLyric method with artist and song
response = client.service.SearchLyric(artist="Europe", song="Carrie")

# Show result(s)
for lyric in response:
    print(f"{lyric.Artist} - {lyric.Song}")
    print(f"URL: {lyric.SongUrl}")
    print(f"LyricId: {lyric.LyricId}")
    print(f"Checksum: {lyric.LyricChecksum}")
    print("---")

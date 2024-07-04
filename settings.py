import json
from ytmusicapi import YTMusic

# Proxy configuration in requests format

ytmusic = YTMusic(location="US")

search_results = ytmusic.search(query="sunflower", filter="songs")

print(search_results )
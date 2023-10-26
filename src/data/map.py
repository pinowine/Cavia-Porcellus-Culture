import requests
import os
from math import *

d = 0.0057
t = 0.0050
lat0 = 30.2571
lng0 = 120.1049

username = 'pinowine'
style_id = 'clo3180qa006q01r89hlad42l'
api_token = 'pk.eyJ1IjoicGlub3dpbmUiLCJhIjoiY2xsY2tuNzZ4MDI2djNqcDRya2hvbnE2MiJ9.i2bUXtq9KP1MOrkuBBzZ7A'

center = []
bounds = []

def lat_lng_to_tile(lat, lng, zoom):
    def num_tiles(z):
        return pow(2, z)

    def sec(x):
        return 1 / cos(x)

    def latlon_to_relative_xy(lat, lon):
        x = (lon + 180) / 360
        y = (1 - log(tan(radians(lat)) + sec(radians(lat))) / pi) / 2
        return x, y

    def latlon_to_xy(lat, lon, z):
        n = num_tiles(z)
        x, y = latlon_to_relative_xy(lat, lon)
        return int(n * x), int(n * y)

    return latlon_to_xy(lat, lng, zoom)


for x in range(6):
    center0 = []
    bounds0 = []
    for y in range(6):
        center0.append([lat0 + t * y * 2 + t, lng0 + d * x * 2 + d])
        bounds0.append([[lat0 + t * y * 2, lng0 + d * x * 2], [lat0 + t * (y + 1) * 2, lng0 + d * (x + 1) * 2]])
    center.append(center0)
    bounds.append(bounds0)

os.makedirs('map_images', exist_ok=True)

# Loop through coordinates and download images
for i, (center_set, bounds_set) in enumerate(zip(center, bounds)):
    for j, (center_coords, bounds_coords) in enumerate(zip(center_set, bounds_set)):
        lat, lng = center_coords
        zoom = 16
        x, y = lat_lng_to_tile(lat, lng, zoom)
        print(f"x: {x}, y: {y}")
        url = f'https://api.mapbox.com/styles/v1/{username}/{style_id}/tiles/{zoom}/{x}/{y}/?access_token={api_token}'
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'map_images/map_image_{i}_{j}.png', 'wb') as f:
                f.write(response.content)
            print(f'Downloaded image {i}_{j}.')
        else:
            print(f'Failed to download image {i}_{j}. Status code: {response.status_code}')

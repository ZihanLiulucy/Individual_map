import json

file_path = "./data/gadm41_GBR_3.json"

with open(file_path, 'r') as file:
    geojson_data = json.load(file)


# Assuming original_geojson is your GeoJSON loaded into a Python dictionary
london_boroughs_geojson = {
    "type": "FeatureCollection",
    "name": "gamd41_London",
    "crs": geojson_data["crs"],  # Copy the CRS from the original GeoJSON
    "features": []
}

for feature in geojson_data["features"]:
    if feature["properties"]["NAME_2"] == "GreaterLondon" or feature["properties"]["TYPE_3"] == "Londonborough" or feature["properties"]["NAME_3"] == "KingstonuponThames":
        london_boroughs_geojson["features"].append(feature)

# Now london_boroughs_geojson contains only the features for "Great London"
# You can then convert this back to a JSON string if needed
london_boroughs_json_str = json.dumps(london_boroughs_geojson)

# Print or save london_boroughs_json_str as needed
print(london_boroughs_json_str)

file_path = './data/gadm41_london.json'

# Save the JSON string to the file
with open(file_path, 'w') as file:
    file.write(london_boroughs_json_str)

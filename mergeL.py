# First, let's load both the GeoJSON file for London boroughs and the summary data JSON
# to understand their structure and find a way to merge them based on a common key (name or code).

import json

# Load the GeoJSON data for London boroughs
with open('./data/gadm41_london.json', 'r') as file:
    london_geojson = json.load(file)

# Load the summary data
with open('./data/summary.json', 'r') as file:
    summary_data = json.load(file)

# Implementing the adjusted approach with normalization for better matching.
# Normalize function
def normalize_name(name):
    return name.replace(" ", "").lower()

# Update summary mapping with normalized keys
summary_mapping = {normalize_name(item['Area name']): item for item in summary_data}

# Reattempt the merge with adjusted name normalization
for feature in london_geojson['features']:
    normalized_geojson_name = normalize_name(feature['properties'].get('NAME_3', ''))
    if normalized_geojson_name in summary_mapping:
        # Found a match, merge the summary data
        for key, value in summary_mapping[normalized_geojson_name].items():
            if key != 'Area name':  # Avoid duplicating area name
                feature['properties'][key] = value

# Attempting to verify the merge by checking one of the properties that should have been added
# This checks if the 'percent_green' property, for example, has been successfully merged into any of the features.
found = False
for feature in london_geojson['features']:
    if 'percent_green' in feature['properties']:
        found = True
        break

# Check if we found a feature with merged summary data
print(london_geojson)
summary_mapping_json_str = json.dumps(london_geojson)
file_path = './data/london_data.json'

# Save the JSON string to the file
with open(file_path, 'w') as file:
    file.write(summary_mapping_json_str)


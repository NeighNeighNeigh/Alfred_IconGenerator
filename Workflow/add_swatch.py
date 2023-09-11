#!/usr/bin/python3

import json
import os
import sys


# Set input path
json_path = os.path.join(os.getenv("alfred_workflow_data"), "swatch.json")

# Strip trailing line from input hex color value
new_colour = sys.argv[1].rstrip()

# Read the JSON data from the file
with open(json_path) as json_file:
    data = json.load(json_file)

# New entry to be added
new_entry = {
    "title": "#" + new_colour,
    "arg": "#" + new_colour,
    "icon": {
        "path": new_colour + ".png"
    }
}

# Check for duplicate entry
for item in data["items"]:
    if item["title"] == new_entry["title"] or item["arg"] == new_entry["arg"]:
        raise ValueError("Duplicate entry found")

# Append the new entry to the beginning of the list of items
data["items"].insert(0, new_entry)

# Convert the updated data back to JSON string
json_data = json.dumps(data, indent=4)

# Print the updated JSON string
# print(json_data)

# Save the updated data back to the file
with open(json_path, 'w') as json_file:
    json_file.write(json_data)

#output the hex value
sys.stdout.write(new_colour)

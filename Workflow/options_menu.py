#!/usr/bin/python3

import json
import os



json_data = '''
{
    "items": [
        {
            "title": "Done",
            "arg": "done",
            "icon": {
                "path": "icons/bg_colour.png"
            }
        },
        {
            "title": "Foreground Colour",
            "arg": "choose_fg",
            "icon": {
                "path": "icons/fg_colour.png"
            }
        },
        {
            "title": "Background Colour",
            "arg": "choose_bg",
            "icon": {
                "path": "icons/bg_colour.png"
            }
        }
    ]
}
'''

icon_paths = {
    "Foreground Colour": os.path.join(os.getenv("alfred_workflow_data"), "swatch_icons/foreground.png"),
    "Background Colour": os.path.join(os.getenv("alfred_workflow_data"), "swatch_icons/background.png"),
    "Done": "done.png"
}

data = json.loads(json_data)

for item in data['items']:
    title = item['title']
    if title in icon_paths:
        item['icon']['path'] = icon_paths[title]

# New entry to be added
bg_yes = {
    "title": "Background Enabled",
    "arg": "bg_yes",
    "icon": {
        "path": "use_bg_yes.png"
    }
}

# New entry to be added
bg_no = {
    "title": "Background Disabled",
    "arg": "bg_no",
    "icon": {
        "path": "use_bg_no.png"
    }
}

#get useBg
useBg = os.getenv("useBg")


# Insert the new entries at the end of the list
if useBg == "1":
    data["items"].append(bg_yes)
else:
    data["items"].append(bg_no)

new_json_data = json.dumps(data, indent=4)

print(new_json_data)





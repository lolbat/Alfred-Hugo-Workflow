#!/usr/bin/env python3

import os
import json
import copy
import frontmatter
from pathlib import Path

# get the content path from the Workflow
contentType = os.getenv("contentType")
contentPath = Path(os.getenv("hugoContentPath")) / contentType

fileList = []

# get all of the markdown files in it
directoryFiles = contentPath.rglob('*.md')

for post in directoryFiles:
    blogPost = frontmatter.load(post)
    status = blogPost["draft"]

    # if it is a draft then add it to the list
    if status:
        fileList.append(post)

# now build the JSON data
# default item in JSON/dict format
fileItem = {
        "type": "file",
        "title": "",
        "subtitle": "",
        "arg": "",
        "icon": {
            "path": "./MarkdownFile.png"
        }
    }

# the JSON wrapper that we will be putting items into
jsonFileList = {"items": []}

# add each draft file
for file in fileList:
    thisJSONItem = copy.deepcopy(fileItem)
    thisJSONItem["title"] = file.stem
    thisJSONItem["subtitle"] = file.name
    thisJSONItem["arg"] = str(file)

    jsonFileList["items"].append(thisJSONItem)

# print out the JSON data
print(json.dumps(jsonFileList))

#!/usr/bin/env python 
# Inspired by jovandeginste's ruby script @ https://github.com/jovandeginste/jovandeginste.github.io/blob/master/_gentags.rb

# This script auto-generates tag pages using the tagpage layout in tags/ directory,
# based on the tags used in the blog posts.
# Works in conjunction with the tagcloud include on blog pages

# requires pyyaml, you can install using pip
import os, yaml

# First, we are going to iterate through blog posts
# the ultimate goal is to create a unique list of tags
tags = []
for filename in os.listdir("_posts"):
    if filename.endswith(".md"):

        # load the front matter as yaml
        post = "_posts/" + filename
        with open(post, 'r') as stream:
            # list comprehension to get entire file as list object
            lines = [line.rstrip('\n') for line in stream]

            # get starting / ending list index for front matter
            yaml_start_end = []
            for index, line in enumerate(lines):
                if line == "---":
                    yaml_start_end.append(index)

            # add yaml front matter to string, between yaml_start_end values
            yamlstream = ""
            for line in range(yaml_start_end[0]+1, yaml_start_end[1]):
                yamlstream += lines[line] + "\n"

            # load yaml into parser and save the tags
            try:
                post_yaml = yaml.safe_load(yamlstream)
                for tag in post_yaml["tags"]:
                    if tag not in tags:
                        tags.append(tag)
            except yaml.YAMLError as exc:
                print(exc)
                
        continue
    else:
        continue

# Now, let's create tags files for each unique tag in the list
for tag in tags:
    filename = "tags/" + tag + ".html"
    with open(filename, "w") as file:
        file.write("---\nlayout: tagpage\ntag: "+tag+"\npermalink: /tags/"+tag+"\n---\n")

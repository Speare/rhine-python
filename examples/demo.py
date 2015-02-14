### (-1). Setup

import json

from rhine.instances import *
from rhine.datatypes import *
from rhine.functions import *

client = instantiate('CEFPUFKMUVJBNZMFUOPOLZEOM') # This API key will be disabled shortly after the demo - register your own for free at www.rhine.io.

### (0). Datasets

articles = json.loads(open('articles.json').read())

images = json.loads(open('images.json').read())

profiles = json.loads(open('profiles.json').read())

### (1). Search

# Search for news articles relating to a given topic.
def search(query):
  # Iterate through each article, assigning a distance score.
  for a in articles:
    # Compute the distance from the user's query to the article text.
    a['distance'] = client.run(distance(entity(query), text(a['text'])))

    # If no relation is found, assign a distance of 100 (the maximum)
    if a['distance'] is None: a['distance'] = 100

  # Return the article with the lowest distance.
  return min(articles, key = lambda a: a['distance'])

# (examples: 'politics', 'celebrity')

### (2). Filtration

# Find users interested in something.
def interested_in(query):
  # Iterate through the user profiles, checking if any of their interests are related to what we want to know about.
  for p in profiles:
    # Compute the distance from the user's query to the profile's interests.
    p['distance'] = min(client.pipeline([distance(entity(i), entity(query)) for i in p['interests']]))

    # If no relation is found, assign a distance of 100 (the maximum)
    if p['distance'] is None: p['distance'] = 100
  
  # Return all users with distance lower than certain threshold
  return [p for p in profiles if p['distance'] < 10] 

# (examples: 'religion', 'food')

### (3). Sorting

# Automatic clustering!
def cluster():
  return client.run(clustering([entity(i) for p in profiles for i in p['interests']]))

### (4). Knowledge

# Filter images by type.
def animals():
  return [i for i in images if client.run(subclass(image.fromurl(i), entity('animal')))]

### (5). Inference / Prediction

# Match articles to users, just with distance.
def recommend(user):
  profile = [p for p in profiles if p['name'] == user][0]
  return min(articles, key = lambda a: client.run(distance(text(a['text']), \
    grouped(entity(profile['interests'][0]), \
            entity(profile['interests'][1]), \
            entity(profile['interests'][2]))))) 

# (examples: 'Alex', 'Mary' ~~)



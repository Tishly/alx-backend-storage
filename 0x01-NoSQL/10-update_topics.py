#!/usr/bin/env python3
"""MongoDB query using PyMongo"""



def update_topics(mongo_collection, name, topics):
    """Updates attributes already in the database"""
    return mongo_collection.update({"name": name}, {"$set": {"topics": topics}}, {multi: true})

#!/usr/bin/env python3
"""MongoDB query using PyMongo"""

def schools_by_topic(mongo_collection, topic):
    """Searches the database for schools based on topic"""
    return mongo_collection.find({"topics": topic})

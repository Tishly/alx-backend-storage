#!/usr/bin/env python3
"""Data base query with Pymongo"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
   results = mongo_collection.aggregate([
                                        {$group: {averageScore: {$avg: "score"}}}
                                        ])

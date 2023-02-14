#!/usr/bin/env python3
"""

"""
from mongodb import MongoClient 


with MongoClient as client:
    logs.nginx.aggregate([
        { $group:  {x: {$sum: "logs"}}
            },
        { $match: {method: }
            }
        ])

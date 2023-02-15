#!/usr/bin/env python3
"""
Log stats from a dump file
"""
from mongodb import MongoClient 


with MongoClient as client:
    """Getting log stats from a dump file"""
   # logs.nginx.aggregate([
    #    { $count: {x: {_id: "$Logs"}}
        #    },
     #   { $group: {methods: {method: "$"} }
      #      }
       # ])
    pass

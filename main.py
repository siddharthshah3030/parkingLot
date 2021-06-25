from parking import *


def execute(query):
  query = query.split(" ")
  if query[0] == "Park": 
    park(query[1],query[3])
  

with open("input.txt") as file:
  queries = file.readlines()
  for query in queries:
    execute(query)


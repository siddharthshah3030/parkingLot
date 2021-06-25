from parking_helpers import *
import warnings

def readInputFile():
  with open("input.txt") as file:
    queries = file.readlines()
    for query in queries:
      try:
        execute(query)
      except:
        warnings.warn('Execution of a query failed, query is - ""'+ ''.join(query)+'""')



if __name__ == '__main__':
  readInputFile()


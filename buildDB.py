#! python3
from pprint import pprint

def receive_data(data):
    for d in data:
        pprint(d)
    print("Showing %s documents" % len(data))
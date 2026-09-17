import json
import os
import time
import subprocess

with open('/Users/vietmac/Documents/CODE/k/batch_385_512.json', 'r') as f:
    tasks = json.load(f)

# we can't call agent tools from python easily unless we know the endpoint.
# But wait, is there a python script I can run?
print("Python script ready")

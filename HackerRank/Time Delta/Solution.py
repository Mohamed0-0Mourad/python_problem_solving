#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

month = dict(Jan=1, Feb=2, Mar=3, Apr=4, May=5, Jun=6, Jul=7, Aug=8, Sep=9, Oct=10, Nov=11, Dec=12)

def parse_date(s:str):
    pattern = r"\d{2} \w{3} \d{4}"
    date = re.findall(pattern, s)[0]
    time = re.findall(r"\d{2}:\d{2}:\d{2}", s)[0]
    return f"{date[-4:]}-{month[ date[3:6] ]}-{date[:2]} {time} {s[-5:]}"

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1, t2 = parse_date(t1), parse_date(t2)
    timestamp_obj1 = datetime.strptime(t1, "%Y-%m-%d %H:%M:%S %z")
    timestamp_obj2 = datetime.strptime(t2, "%Y-%m-%d %H:%M:%S %z")

    diff= abs( (timestamp_obj1 - timestamp_obj2).total_seconds() )
    diff = int(diff)
    return str(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

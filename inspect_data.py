import csv

with open("ward.csv", encoding = "utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print("Number of rows:", len(rows))
print("Columns:", list(rows[0].keys()))

import csv

with open("ward.csv", encoding = "utf-8-sig") as f:
    rows = list(csv.DictReader(f))

values=[]
for row in rows:
    value=float(row['population'])
    values.append(value)
    
print("Smallest:", min(values))
print("Largest:", max(values))
print("Count:", len(values))

import csv

with open("ward.csv", encoding = "utf-8-sig") as f:
    rows = list(csv.DictReader(f))

values=[]
for row in rows:
    raws=row['population'].strip()
    if  raws == " ":
        continue
    values.append(float(raws))

print("Smallest:", min(values))
print("Largest:", max(values))
print("Count:", len(values))

import csv
from unittest import result

def inspect_column (filename,column):
    
    with open(filename, encoding = "utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    values=[]
    for row in rows:
        raws=row[column].strip()
        if  raws == " ":
            continue
        values.append(float(raws))
    return{
        "smallest": min(values),
        "largest": max(values),
        "count": len(values)
    }
area_result=inspect_column("ward.csv","area_km2")
pop_result=inspect_column("ward.csv","population")
print(area_result)
print(pop_result)


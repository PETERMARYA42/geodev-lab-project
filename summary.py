import csv
from unittest import result
from unittest import result

def read_rows(filename):
    with open(filename, encoding = "utf-8-sig") as f:
       return list(csv.DictReader(f))
 
def clean_values(rows,column):
    values=[]
    for row in rows:
        raws=row[column].strip()
        if  raws == " ":
            continue
        values.append(float(raws))
    return values

def summarize(values):
    if len(values) == 0:
        return {"count": 0, "smallest": None, "largest": None, "average": None}
    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values), 
        "average": sum(values)/len(values),
    }
    
def summaries_all(filename, columns):
    rows = read_rows(filename)
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarize(values)
    return report

report = summaries_all("ward_2.csv", ["area_km2", "population"])

for column, stats in report.items():
    print(column,">", stats)

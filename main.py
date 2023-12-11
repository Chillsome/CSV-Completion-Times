import pandas as pd
import os
import glob
import csv

if __name__ == '__main__':
    path = os.getcwd()
    csv_files = glob.glob(os.path.join("dataload_csv", "*.csv"))
    reports = []
    current_completion_avg = {}
    sorted_report_completion_avg = {}
    # loop over the list of csv files
    for f in csv_files:
        current_completion_avg = {}
        # read the csv file
        df = pd.read_csv(f)
        # print the location and filename
        filename = f.split("/")[-1]
        try:
            completion_times = df["dataLoadTime"]
        except KeyError:
            completion_times = df["domComplete"]
        current_completion_avg["FileName"] = filename
        current_completion_avg["Average Completion Time (sec)"] = round(completion_times.mean()/1000, 2)
        current_completion_avg["Max Completion Time (sec)"] = round(completion_times.max()/1000, 2)
        current_completion_avg["Min Completion Time (sec)"] = round(completion_times.min()/1000, 2)
        reports.append(current_completion_avg)
    # Sort the dictionary by alphabetical order

    reports = sorted(reports, key=lambda d: d['FileName'])
    try:
        with open('AverageCompletionTime.csv', 'w', encoding='UTF8') as f:
            header = list(reports[0].keys())
            writer = csv.writer(f)
            writer.writerow(header)
            for i in reports:
                row = list(i.values())
                writer.writerow(row)
            f.close()
    except ValueError:
        print("No files found")

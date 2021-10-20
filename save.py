import csv

def save_to_file(indeed_jobs):
  file = open("jobs.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "link"])
  for job in indeed_jobs:
    writer.writerow(list(job.values()))

  return
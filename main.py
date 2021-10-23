from indeed import get_indeed_jobs
from weworkremotely import get_wwr_jobs
from remoteok import get_remote_jobs
from save import save_to_file
from flask import Flask, render_template, request, redirect, send_file

"""
MODEL = https://imgur.com/DCIdYE5
"""

##### GET INDEED JOBS #####
indeed_jobs = get_indeed_jobs("react")

#### GET WEWORKREMOTELY JOBS #####
wwr_jobs = get_wwr_jobs("react")

#### GET REMOTEOK JOBS #####
remoteok_jobs = get_remote_jobs("react")


app = Flask("Personal Job Scraper")
jobs_database = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    jobs = []
    if word:
        word = word.lower()
        existing_jobs = jobs_database.get(word)
        if existing_jobs:
            jobs = existing_jobs
        else:
            indeed_jobs = get_indeed_jobs(word)
            wwr_jobs = get_wwr_jobs(word)
            remoteok_jobs = get_remote_jobs(word)

            jobs = indeed_jobs + wwr_jobs + remoteok_jobs

            jobs_database[word] = jobs
    else:
       return redirect("/")

    return render_template("report.html",
                            searchingBy=word,
                            resultNumber=len(jobs),
                            jobs=jobs
                            )

@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = jobs_database.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


app.run(host="0.0.0.0")

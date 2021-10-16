from indeed import extract_indeed_pages, extract_indeed_jobs, get_indeed_jobs
from weworkremotely import extract_wwr_sections, extract_wwr_jobs, get_wwr_jobs
from save import save_to_file
from flask import Flask, render_template, request, redirect, send_file

# last_indeed_pages = extract_indeed_pages()
# indeed_jobs = extract_indeed_jobs(last_indeed_pages)
# jobs = get_indeed_jobs("vue")
# save_to_file(jobs)
sections = get_wwr_jobs("react")



"""
app = Flask("SuperScrapper")
existing_jobs_database = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existing_jobs = existing_jobs_database.get(word)
        if existing_jobs:
            jobs = existing_jobs
        else:
            jobs = get_indeed_jobs(word)
            existing_jobs_database[word] = jobs
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
        jobs = existing_jobs_database.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


app.run(host="0.0.0.0")
"""
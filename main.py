# from indeed import extract_indeed_pages, extract_indeed_jobs
# from save import save_to_file
from flask import Flask, render_template, request

# last_indeed_pages = extract_indeed_pages()
# indeed_jobs = extract_indeed_jobs(last_indeed_pages)
# save_to_file(indeed_jobs)

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    return render_template("report.html", searchingBy=word)

app.run(host="0.0.0.0")





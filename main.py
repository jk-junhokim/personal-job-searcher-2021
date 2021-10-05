# from indeed import extract_indeed_pages, extract_indeed_jobs
# from save import save_to_file
from flask import Flask

# last_indeed_pages = extract_indeed_pages()
# indeed_jobs = extract_indeed_jobs(last_indeed_pages)
# save_to_file(indeed_jobs)

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return "Hello! Welcome to mi casa!"

@app.route("/contact")
def contact():
    return "Contact me!"

app.run(host="0.0.0.0")




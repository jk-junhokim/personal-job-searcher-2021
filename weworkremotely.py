import requests
from bs4 import BeautifulSoup

def extract_wwr_job_info(wwr_url):

    # job_title, job_company, job_application_link

    wwr_result = requests.get(wwr_url)
    wwr_soup = BeautifulSoup(wwr_result.text, 'html.parser')
    all_sections = wwr_soup.find("div", {"class":"jobs-container"})
    sections_separated = all_sections.find_all("section", {"class":"jobs"})

    jobs = []

    for section in sections_separated:
        section_info = section.find("ul")
        jobs_per_section = section_info.find_all("li")
        for job in jobs_per_section:
            get_correct_link = job.find_all("a")
            correct = "region company"
            for link_unique in get_correct_link:
                link_string = str(link_unique)
                if correct in link_string:
                    correct_link = link_unique
                    return_link = correct_link.get("href")
                else:
                    return_link = "None"
        
                if return_link != "None":
                    return_job_title = correct_link.find("span", {"class":"title"}).string
                    return_company_name = correct_link.find("span", {"class":"company"}).string
                    return_application_link = f"https://weworkremotely.com/{return_link}"

                    job_info = {"title":return_job_title,
                                "company":return_company_name,
                                "_link":return_application_link}

                    jobs.append(job_info)

    return jobs

def get_wwr_jobs(word):
    wwr_url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    jobs = extract_wwr_job_info(wwr_url)

    return jobs

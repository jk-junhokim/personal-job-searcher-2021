import requests
from bs4 import BeautifulSoup

"""
https://weworkremotely.com/
https://stackoverflow.com/jobs
https://remoteok.io/

MODEL = https://imgur.com/DCIdYE5
"""


def extract_wwr_job_info(wwr_url):

    # job_title, job_company, job_application_link

    wwr_result = requests.get(wwr_url)
    wwr_soup = BeautifulSoup(wwr_result.text, 'html.parser')
    sections = wwr_soup.find("div", {"class":"jobs-container"})
    sections_divided = sections.find_all("section", {"class":"jobs"})

    for each_section in sections_divided:
        section_specifics = each_section.find("ul")
        jobs_per_section = section_specifics.find_all("li")
        for jobs in jobs_per_section:
            get_correct_link = jobs.find_all("a")
            correct = "region company"
            for link_unique in get_correct_link:
                link_string = str(link_unique)
                if correct in link_string:
                    correct_link = link_unique
                    return_link = correct_link.get("href")
                else:
                    return_link = "None"
            
            # get company name & application link
            if return_link != "None":
                return_job_title = correct_link.find("span", {"class":"title"}).string
                return_company_name = correct_link.find("span", {"class":"company"}).string
                return_application_link = f"https://weworkremotely.com/{return_link}"

            return {"job_title":return_job_title,
                    "job_company":return_company_name,
                    "job_link":return_application_link}

def extract_wwr_jobs(job_sections, indeed_url):
  jobs = []
  for page in range(job_sections):
    print(f"Scrapping page {page}")
    result = requests.get(f"{indeed_url}&start={page}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("a", {"class":"fs-unmask"})
    for result in results:
      job = extract_wwr_job_info(result)
      jobs.append(job)
    
  return jobs
    

"""
https://weworkremotely.com/remote-jobs/search?term=react
"""

def get_wwr_jobs(word):
    wwr_url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    job_sections = extract_wwr__job_info(wwr_url)
    # jobs = extract_wwr_jobs(job_sections, wwr_url)
    
    # return jobs
    pass

import requests
from bs4 import BeautifulSoup

LIMIT = 50

def extract_indeed_pages(indeed_url):
  indeed_result = requests.get(indeed_url)
  indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
  pagination = indeed_soup.find("div", {"class":"pagination"})
  links = pagination.find_all('a')
  pages = []

  for link in links[:-1]:
    pages.append(int(link.string))

  max_page = pages[-1]

  return max_page


def extract_indeed_job_info(result):

  # get job
  job_title = result.find("td", {"class":"resultContent"}).find("div", {"class":"heading4"}).find_all("span")
  if len(job_title) > 1:
    job_title = job_title[1].string
  else:
    job_title = job_title[0].string

  # get company
  NO_COMPANY_NAME = None
  find_company_1 = result.find("div",{"class":"heading6"})
  if type(find_company_1) == type(NO_COMPANY_NAME):
    company_name = "Currently Unavailable"
  else:
    find_company_2 = find_company_1.find("span",{"class":"companyName"})
    if type(find_company_2) == type(NO_COMPANY_NAME):
      company_name = "Currently Unavailable"
    else:
      find_company_3 = find_company_2.find("a")
      if type(find_company_3) == type(NO_COMPANY_NAME):
        company_name = "Currently Unavailable"
      else:
        company_name = find_company_3.string

  # get location
  get_location = result.find("div",{"class":"heading6"}).find("div", {"class": "companyLocation"}).text
  location = get_location

  # get link
  get_link = result["href"]
  job_link = f"https://www.indeed.com{get_link}"

  return {"title": job_title,  "company": company_name, "location": location, "link": job_link}


def extract_indeed_jobs(last_page, indeed_url):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{indeed_url}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("a", {"class":"fs-unmask"})
    for result in results:
      job = extract_indeed_job_info(result)
      jobs.append(job)
    
  return jobs
    
def get_indeed_jobs(word):
    indeed_url = f"https://www.indeed.com/jobs?q={word}&l=Austin%2C%20TX&limit={LIMIT}&radius=25"
    last_page = extract_indeed_pages(indeed_url)
    jobs = extract_indeed_jobs(last_page, indeed_url)
    
    return jobs

import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&l=Austin%2C%20TX&limit={LIMIT}&radius=25"


def extract_indeed_pages():
  indeed_result = requests.get(URL)
  indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
  pagination = indeed_soup.find("div", {"class":"pagination"})
  links = pagination.find_all('a')
  pages = []

  for link in links[:-1]:
    pages.append(int(link.string))

  max_page = pages[-1]

  return max_page


def extract_job_info(result):

  # get job
  job_title = result.find("td", {"class":"resultContent"}).find("div", {"class":"heading4"}).find_all("span")
  if len(job_title) > 1:
    job_title = job_title[1].string
  else:
    job_title = job_title[0].string

  # get company
  NO_COMPANY_NAME = None
  find_company = result.find("div",{"class":"heading6"}).find("span",{"class":"companyName"}).find("a")
  if type(find_company) == type(NO_COMPANY_NAME):
    company_name = str(NO_COMPANY_NAME)
  else:
    company_name = find_company.string

  # get location
  get_location = result.find("div",{"class":"heading6"}).find("div", {"class": "companyLocation"}).text
  location = get_location

  # get link
  get_link = result["href"]
  job_link = f"https://www.indeed.com{get_link}"

  return {"job": job_title,  "company": company_name, "location": location, "link": job_link}


def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping page {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("a", {"class":"fs-unmask"})
    for result in results:
      job = extract_job_info(result)
      jobs.append(job)
    
  return jobs
    


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

def extract_indeed_jobs(last_page):
  # for page in range(last_page):
  result = requests.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, 'html.parser')
  results = soup.find_all("a", {"class":"fs-unmask"})
  index = 1
  for result in results:
    job_title = result.find("td", {"class":"resultContent"}).find("div", {"class":"heading4"}).find_all("span")
    if len(job_title) > 1:
      job_title = job_title[1].string
    else:
      job_title = job_title[0].string

    NO_COMPANY_NAME = None
    find_company = result.find("div",{"class":"heading6"}).find("span",{"class":"companyName"}).find("a")
    if type(find_company) == type(NO_COMPANY_NAME):
      company_name = str(NO_COMPANY_NAME)
    else:
      company_name = find_company.string
    
    print("#" + str(index) + " - job: " + job_title + " / company: " + company_name)
    index += 1
    








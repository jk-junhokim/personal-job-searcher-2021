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
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}")
    print(result.status_code)

# from 2.6



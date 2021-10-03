import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l=Austin%2C%20TX&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=f2e0073c7a5ec089")

# print(indeed_result.text)
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
# print(indeed_soup.prettify())

pagination = indeed_soup.find("div", {"class":"pagination"})
# print(pagination)

pages = pagination.find_all('a')
# print(pages)

for page in pages:
  print(page.find("span"))



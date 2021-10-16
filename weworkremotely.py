import requests
from bs4 import BeautifulSoup


def extract_wwr_sections(wwr_url):

    # job_title, job_company, job_application_link

    wwr_result = requests.get(wwr_url)
    wwr_soup = BeautifulSoup(wwr_result.text, 'html.parser')
    sections = wwr_soup.find("div", {"class":"jobs-container"})
    sections_divided = sections.find_all("section", {"class":"jobs"})

    for each_section in sections_divided:
        section_specifics = each_section.find("ul")
        jobs_per_section = section_specifics.find_all("li")
        # print(jobs_per_section)
        for jobs in jobs_per_section:
            # unique_job_link = jobs.find("a")["href"]
            check_new_or_not = jobs.find("span", {"class":"new"})
            if check_new_or_not != None:
                unique_job_link = jobs.select_one(":nth-child(4)")
                print(unique_job_link)
                print("")
                print(type(unique_job_link))
                print("-------------------------------------------")
            elif check_new_or_not == None:
                unique_job_link = jobs.select_one(":nth-child(3)")
                print(unique_job_link)
                print("")
                print(type(unique_job_link))
                print("-------------------------------------------")
            else:
                print("Exception!")
                


            # job_application_link = f"https://weworkremotely.com{unique_job_link}"
            # print(job_application_link)
            # print("-------------------------------------------")

        

#   links = sections.find_all('section')
#   pages = []

#   for link in links[:-1]:
#     pages.append(int(link.string))

#   job_sections = pages[-1]

#   return job_sections
pass


def extract_wwr_job_info(result):

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
    job_sections = extract_wwr_sections(wwr_url)
    # jobs = extract_wwr_jobs(job_sections, wwr_url)
    
    # return jobs
    pass

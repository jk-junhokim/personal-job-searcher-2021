import requests
from bs4 import BeautifulSoup

# what does "headers" do?
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def extract_remote_job_info(remote_url):

    # job_title, job_company, job_application_link

    remote_result = requests.get(remote_url, headers=headers)
    remote_soup = BeautifulSoup(remote_result.text, 'html.parser')
    job_container = remote_soup.find("div", {"class":"container"}).find("table", {"id":"jobsboard"}).find_all("tr", {"class":"job"})

    jobs = []

    for job in job_container:
        return_job_title = job.find("h2", {"itemprop":"title"}).string

        return_company_name = job["data-company"]

        link = job["data-href"]
        return_application_link = f"https://remoteok.io{link}"

        job_info = {"job_title":return_job_title,
                    "job_company":return_company_name, "job_link":return_application_link}

        jobs.append(job_info)

    return jobs

def create_remote_url(word):
    remote_url = f"https://remoteok.io/remote-{word}-jobs"

    return remote_url    

def get_remote_jobs(word):

    remote_url = create_remote_url(word)
    jobs = extract_remote_job_info(remote_url)

    return jobs

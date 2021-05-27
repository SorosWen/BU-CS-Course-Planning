from bs4 import BeautifulSoup, SoupStrainer
import requests

headers = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}

####################################
## ##
####################################
def find_courses():
    url = 'https://www.bu.edu/academics/cas/courses/computer-science/'
    webpage = requests.get(url, headers = headers)
    soup = BeautifulSoup(webpage.content, "lxml")
    container = soup.find_all("a")
    course_info = []
    for link in container:
        try: 
            link = link.get('href')
            if link[0] == '/' and link[-2].isdigit(): 
                link = 'https://www.bu.edu' + link
                course_info.append(get_course_info(link))
        except:
            continue
    return course_info

####################################
## [name, id, pre-requisites] ######
####################################
def get_course_info(url):
    info = []
    webpage = requests.get(url, headers = headers)
    soup = BeautifulSoup(webpage.content, "lxml")
    course_name = soup.find("h1").text
    course_id = soup.find("h2").text
    info.append(course_name)
    info.append(course_id)

    container = soup.find_all('dd')
    for dd in container: 
        dd = dd.text
        if not dd.isdigit():
            info.append(dd)
            return info
    info.append('')
    return info

info= find_courses()
for course in info:
    print(course[2])


def comprehension():
    requirement = []
    return requirement
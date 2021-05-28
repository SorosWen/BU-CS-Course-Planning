from bs4 import BeautifulSoup, SoupStrainer
import requests
from .Node import And_Node, Or_Node

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
#### [name, id, pre-requisites] ####
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



####################################
####################################
'''
def prereq_comprehension(prerequisite):
    prerequisite = prerequisite.replace(' ', '').replace('or equivalent', '').replace('or consent of instructor', '')
    requirement = []
    
    if prerequisite == '' or prerequisite == 'approval of the Honors Committee':
        return requirement
    
    curr_word_start_idx = 0
    idx = 0
    or_mode = False
    while idx < len(prerequisite): 
        print(prerequisite[idx])
        if prerequisite[idx] == ',':
            requirement.append(prerequisite[curr_word_start_idx: idx])
            curr_word_start_idx = idx + 1
        if prerequisite[idx] == ';':
            requirement.append(prerequisite[curr_word_start_idx: idx])
            curr_word_start_idx = idx + 1
            or_mode = False
        elif prerequisite[idx] == '.':
            requirement.append(prerequisite[curr_word_start_idx: idx])
            curr_word_start_idx = idx + 1
            break
        elif idx == len(prerequisite) - 1:
            if prerequisite[idx].isdigit():
                requirement.append(prerequisite[curr_word_start_idx: idx + 1])
        elif prerequisite[idx].islower():
            if prerequisite[idx] == 'a':
                if prerequisite[idx - 1].isdigit(): 
                    requirement.append(prerequisite[curr_word_start_idx: idx])
                idx += 2
                curr_word_start_idx = idx + 1
            elif prerequisite[idx] == 'o':
                if prerequisite[idx - 1].isdigit(): 
                    requirement.append(prerequisite[curr_word_start_idx: idx])
                if not or_mode:
                    requirement = [requirement]
                idx += 1
                curr_word_start_idx = idx + 1
                or_mode = True
            elif prerequisite[idx] == 'r': #recommended
                idx += 10
                curr_word_start_idx = idx
        idx += 1
    return requirement
'''

def prereq_comprehension(prerequisite):
    prerequisite = prerequisite.split(';')
    print(prerequisite)

    for phrase in prerequisite:
        if 'and' in phrase:
            tree = Or_Node()

print(prereq_comprehension('CASCS112, CASCS131, and CASCS132; or CASCS235 or CASCS237'))
print(prereq_comprehension('CAS CS 108 or CAS CS 111; CAS CS 132 or CAS MA 242 or CAS MA 442;'))
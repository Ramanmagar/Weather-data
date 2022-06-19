from bs4 import BeautifulSoup
import requests

# print('Put some skill that you are not familiar with')
# unfamiliar_skill = input('>')
# print(f"Filtering out {unfamiliar_skill}")

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs: 
    published_date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_date:
       #print(published_date)

       company_name = job.find('h3', class_ = 'joblist-comp-name').text
       #.replace(' ','')
       #print(company_name)

       skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')
       #print(skills)

       more_info = job.header.h2.a['href']
    

       print(f"Company Name: {company_name.strip()}")
       print(f"Required Skills: {skills.strip()}")
       print(f"Apply Here: {more_info}")
       print(f"Posted Date: {published_date.strip()}")

           #     print(f'''
           #    Company Name:{company_name}
           #    Required Skills:{skills}
           #    Posted Date: {published_date}
           #    ''')

       print('')
 
















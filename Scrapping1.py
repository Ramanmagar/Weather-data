from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

with open("scrapping2.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    #print(soup.prettify())
    # tags = soup.find('h3')
    # print(tags)
    tags = soup.head.title
    print(tags)












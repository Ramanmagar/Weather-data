from requests_html import HTMLSession

s = HTMLSession()

query = 'latur'
url = f'https://www.google.com/search?q=whether+{query}'

r = s.get(url, headers ={'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'})

temp = print(r.html.find('span#wob_tm', first=True).text)
unit = print(r.html.find('div.vk_bk.wob-unit span.wob_t', first = True).text)
desc = print(r.html.find('div.VQF4g', first = True).find('span#wob_dc', first = True).text)
print(query, temp, unit, desc)







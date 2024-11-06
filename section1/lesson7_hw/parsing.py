import fake_useragent
import requests
from bs4 import BeautifulSoup


data = {'custname': 'qwre',
        'custtel': '213',
        'custemail': 'eqwd@fqwefew.fe',
        'size': '2',
        'topping': 'deq',
        'delivery': 'edeq',
        'comments': 'dqe# '}

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Host": "httpbin.org",
    "Priority": "u=3, i",
    "Referer": "https://httpbin.org/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0.1 Safari/605.1.15",
    "X-Amzn-Trace-Id": "Root=1-672242d0-3fa15ed135cd709639e83e9d"
  }

session = requests.Session()
session.get('https://httpbin.org/form/post')
response = session.post('https://httpbin.org/post', headers=headers,
                        data=data, allow_redirects=True)

# response = requests.post('https://httpbin.org/post', headers=headers,
#                          data=data)
# print(response.text)

# params = {'q': 'London',
#           'appid': '159d1093e5a6fab015cd45bcd9b397db',
#           'units': 'metric'}

# response = requests.post('https://httpbin.org/forms/post', headers=headers,
#                          data=data)
# print(response)

# response = requests.get('https://httpbin.org/headers', headers=headers)
# print(response.text)

# params = {'q': 'London',
#           'appid': '159d1093e5a6fab015cd45bcd9b397db',
#           'units': 'metric'}
# response = requests.get('https://api.openweathermap.org/data/2.5/weather',
#                         params=params)
# print(response.status_code)
# print(response)
# print(response.text)
# print(response.json())
#
# x = response.json()
# print(x['weather'][0]['main'])
# print(response.headers)

# params = {'q': 'funny cats'}
# response = requests.get('https://www.google.com/search', params=params)
# print(response.status_code)
# print(response.headers)
# print(response.text)

# user = fake_useragent.UserAgent().random
# header = {'user-agent': user}
#
# link = 'https://browser-info.ru'
# response = requests.get(link, headers=header).text
# soup = BeautifulSoup(response, 'lxml')
# block = soup.find('div', id='tool_padding')
#
# check_js = block.find('div', id='javascript_check')
# status_js = check_js.find_all('span')[1].text
# result_js = f'Javascript: {status_js}'
#
# check_flash = block.find('div', id='flash_version')
# status_flash = check_flash.find_all('span')[1].text
# result_flash = f'Flash: {status_flash}'
#
# check_user = block.find('div', id='user_agent').text
# result_user = f'User agent: {check_user}'
# print(result_js)
# print(result_flash)
# print(result_user)

# print(response)

# with open('parsing.html', 'w', encoding='utf-8') as file:
#     file.write(response)

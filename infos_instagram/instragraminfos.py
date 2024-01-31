from bs4 import BeautifulSoup
import requests

URL = "https://www.instagram.com/{}/"
header = {

            'authority': 'www.instagram.com',
            "pragma": "no-cache",
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
            'accept': '*/*',
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin'

        }

def parse_data(s):
    data = {}
    s = s.split("-")[0]
    s = s.split(" ")[2]
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
    return data

def scrape_data(username):
    r = requests.get(URL.format(username), headers=header)
    s = BeautifulSoup(r.text , "html.parser")
    metas = s.find_all('meta')
    for m in metas:
      if m.get('property') == 'og:description':
        return m.get('content')

if __name__ == "__main__":
    username = "leogomesss_"
    data = scrape_data(username)
    
    print(f"This account has {data}  followers ")
    print(f"This account has {data} following ")
    print(f"This account has {data} Posts ")
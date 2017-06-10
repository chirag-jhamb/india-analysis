import requests
from bs4 import BeautifulSoup as bs
import requests
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
hdr = { 'User-Agent' : user_agent }
thelink='https://www.zomato.com/india'
html = requests.get(thelink, headers=hdr)
soup = bs(html.content)
#Scrape all the state names and links-

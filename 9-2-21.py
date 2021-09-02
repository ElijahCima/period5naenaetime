# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:45:38 2021

@author: Elijah
"""

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github,io/fake-jobs/"
page = requests.get(URL)

print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
results_location = soup.find_all("p", class_="location")
results_title = soup.find_all("h2", class_="title is-5")

for result in results_location:
    print(result.text.strip())

for result in results_title:
    print(result.text.strip())
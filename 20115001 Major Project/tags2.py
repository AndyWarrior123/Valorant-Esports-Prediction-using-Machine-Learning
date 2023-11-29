# class="wf-card fc-flex m-item

import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

with open("Datasets/team.html", "r", encoding="UTF-8") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

links = ""
for i in soup.find_all(class_="wf-card fc-flex m-item", href=True):
    # links.append("https://www.vlr.gg" + str(i['href']))
    links += ("https://www.vlr.gg" + str(i['href']) + "\n")

print(links)

with open("url.txt", "w") as f:
    f.write(links)
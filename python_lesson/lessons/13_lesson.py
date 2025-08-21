import requests
import json
from bs4 import BeautifulSoup

response = requests.get("https://www.themoscowtimes.com").text
# print(response)
soup = BeautifulSoup(response, "html.parser")
# print(soup)

# find()->argument sifatida htmldagi taglarni qabul qiladi class lariga asoslanib bizga kerakli ma'lumotlarni olib beradi
# find()->birinchi to'g'ri kelgan tag va classni bizga taqdim etadi

# blocks= soup.find_all("div", class_="article-excerpt-default__content")
# print(text_section)

articels = soup.find_all("div", class_="article-excerpt-default article-excerpt-default--ukraine_war")
json_data = []
for articel in articels:
    titel = articel.find("h3", class_="article-excerpt-default__headline").get_text(strip=True)
    print(titel)
    description = articel.find("div", class_="article-excerpt-default__teaser").get_text(strip=True) if articel.find(
        "div", class_="article-excerpt-default__teaser") else "NONE"
    print(description)
    category = articel.find("span", class_="article-excerpt-default__author").get_text(strip=True) if articel.find(
        "span", class_="article-excerpt-default__author") else "NONE"
    print(category)
    image_link = articel.find("img")["src"]
    print(image_link)
    articel_link = articel.find('a')['href']
    print(articel_link)
    json_data.append({
        "title": titel,
        "description": description,
        "category": category,
        "image_link": image_link,
        "articel_link": articel_link
    })

    response2 = requests.get(articel_link).text
    soup2 = BeautifulSoup(response2, "html.parser")
with open("json_data.json", mode="w", encoding="utf-8") as json_file:
    json.dump(json_data, json_file, indent=4, ensure_ascii=False)

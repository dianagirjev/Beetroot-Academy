import requests, bs4

response = requests.get('https://beetrootacademy.com')
# print(response.text)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
print(soup)

items = soup.find_all("div", {"class": "courses-item-text"})
print(len(items))
print(items[0])

data = []
for item in items:
    curs = {
        "tip": item.find("div", {"class": "course-items-type"}).text,
        "titlu": item.find("div", {"class": "course-items-title"}).text,
        "duration": item.find("div", {"class": "course-items-duration"}).text,
    }
    print(curs)
    data.append(curs)

print(data)

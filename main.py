import requests
from  bs4 import BeautifulSoup

f = open('recette.html', 'r', encoding="utf-8")
html_content = f.read()

# html_content = requests.get("https://www.python.org/").text
soup = BeautifulSoup(html_content, "html.parser") 

titre_h1 = soup.find("h1")
texte_h1 = titre_h1.text
print(texte_h1)

div_centre = soup.find_all("div", class_="centre")


description_p = div_centre[1].find("p", class_="description")
print(description_p.text)




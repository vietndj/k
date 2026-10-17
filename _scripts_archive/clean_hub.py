from bs4 import BeautifulSoup

with open('diaryofaceo.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

grids = soup.find_all('div', class_='apple-cards-grid')
for grid in grids:
    grid.clear()

with open('diaryofaceo.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

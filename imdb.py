from bs4 import BeautifulSoup 
import requests
import csv

url = requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')
src = url.content
soup = BeautifulSoup(src,'lxml')

series_list = []

def main(url):
    
    src = url.content
    soup = BeautifulSoup(src,'lxml')

    body = soup.find('tbody',{'class':'lister-list'})

    group = body.find_all('tr')
    series_num = len(group)

    for i in range(series_num):
        title = group[i].find('td',{'class':'titleColumn'}).contents[1].text.strip()
        year = group[i].find('td',{'class':'titleColumn'}).contents[3].text.strip()[1:-1]
        num_series = group[i].find('td',{'class':'titleColumn'}).contents[0].text.strip()
        rating = group[i].find('td',{'class':'ratingColumn imdbRating'}).contents[1].text.strip()

        series_list.append({
        'I' : num_series,
        'Name' : title,
        'Year' : year,
        'Rating' : rating
        })

    keys = series_list[0].keys()
    
    with open('Top 250 Series.csv','w', newline = '', encoding="utf-8") as file :
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(series_list)
        print('Enjoy !!')
main(url)


from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

open('append_data.json', 'w').close()


#### SCRAPING

url = 'https://www.google.com/finance'


request = Request(url)
request.add_header('User-Agent', 'Mozilla/5.0')

page = urlopen(request)

html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

main_section = soup.find('div', {'class': {'GCviOb'}})

#div 1
def getDiv1():
    div1 = main_section.find('a', {'class': {'NaLFgc'}})
    div1_abr = div1.find('div', {'class': {'COaKTb'}})
    div1_title = div1.find('div', {'class': {'TwnKPb'}})
    div1_percentage = div1.find('div', {'class': {'JwB6zf'}})

    div1_abr = div1_abr.text
    div1_title = div1_title.text
    div1_percentage = div1_percentage.text
    div1_total = div1_abr + " " + div1_title + " " + div1_percentage

    return div1_total


#div 2
div2 = main_section.find_all('a', class_='NaLFgc')[1]
div2_abr = div2.find('div', {'class': {'COaKTb'}})
div2_title = div2.find('div', {'class': {'TwnKPb'}})
div2_percentage = div2.find('div', {'class': {'JwB6zf'}})

div2_abr = str(div2_abr.text)
div2_title = str(div2_title.text)
div2_percentage = str(div2_percentage.text)
div2_total = div2_abr + " " + div2_title + " " + div2_percentage

def getDiv2():
    return div2_total

#div 3
div3 = main_section.find_all('a', class_='NaLFgc')[2]
div3_abr = div3.find('div', {'class': {'COaKTb'}})
div3_title = div3.find('div', {'class': {'TwnKPb'}})
div3_percentage = div3.find('div', {'class': {'JwB6zf'}})


div3_abr = str(div3_abr.text)
div3_title = str(div3_title.text)
div3_percentage = str(div3_percentage.text)
div3_total = div3_abr + " " + div3_title + " " + div3_percentage

def getDiv3():
    return div3_total

#div 4
div4 = main_section.find_all('a', class_='NaLFgc')[3]
div4_abr = div4.find('div', {'class': {'COaKTb'}})
div4_title = div4.find('div', {'class': {'TwnKPb'}})
div4_percentage = div4.find('div', {'class': {'JwB6zf'}})

div4_abr = str(div4_abr.text)
div4_title = str(div4_title.text)
div4_percentage = str(div4_percentage.text)
div4_total = div4_abr + " " + div4_title + " " + div4_percentage

def getDiv4():
    return div4_total

#div 5
div5 = main_section.find_all('a', class_='NaLFgc')[4]
div5_abr = div5.find('div', {'class': {'COaKTb'}})
div5_title = div5.find('div', {'class': {'TwnKPb'}})
div5_percentage = div5.find('div', {'class': {'JwB6zf'}})

div5_abr = str(div5_abr.text)
div5_title = str(div5_title.text)
div5_percentage = str(div5_percentage.text)
div5_total = div5_abr + " " + div5_title + " " + div5_percentage

def getDiv5():
    return div5_total

#div 6
div6 = main_section.find_all('a', class_='NaLFgc')[5]
div6_abr = div6.find('div', {'class': {'COaKTb'}})
div6_title = div6.find('div', {'class': {'TwnKPb'}})
div6_percentage = div6.find('div', {'class': {'JwB6zf'}})

div6_abr = str(div6_abr.text)
div6_title = str(div6_title.text)
div6_percentage = str(div6_percentage.text)
div6_total = div6_abr + " " + div6_title + " " + div6_percentage

def getDiv6():
    return div6_total
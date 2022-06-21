import requests
import datetime
from bs4 import BeautifulSoup

#Used headers/agent because the request was timed out and asking for an agent. 
#Using following code we can fake the agent.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

filename = 'companies.csv'
f = open(filename, 'a')
columns = 'Date, Weekday, Companies, Votes\n'
f.write(columns)

response = requests.get('https://www.producthunt.com/time-travel/2022/1/1', headers=headers)
content = response.content
soup = BeautifulSoup(content,"html.parser")
items = soup.find_all('li',class_= "styles_item__Sn_12")    
i = 0 
for item in items:
    try:
        company_name = item.find('h3',class_ = "styles_font__m46I_ styles_medium__pDQUU styles_semiBold__yhRqL styles_title__jWi91 styles_lineHeight__kGlRn styles_underline__IqHIA").text
        votes = item.find('span',class_ = "styles_font__m46I_ styles_black__Z9fG_ styles_small__lLD08 styles_semiBold__yhRqL styles_lineHeight__kGlRn styles_underline__IqHIA").text
        votes = votes.replace(',','')
        f.write(votes)
    except:
        continue

f.close()
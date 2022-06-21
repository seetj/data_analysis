import requests
import datetime
from bs4 import BeautifulSoup

#Used headers/agent because the request was timed out and asking for an agent. 
#Using following code we can fake the agent.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
year_url = range(2015,2023)
month_url = range(1,13)
day_url = range(1,32)
filename = 'companies3.csv'
f = open(filename, 'w')
columns = 'Date, Weekday, Companies, Votes\n'
f.write(columns)

for year in year_url:
    for month in month_url:
        for day in day_url:
            response = requests.get('https://www.producthunt.com/time-travel/' + str(year) + '/' + str(month) + '/' + str(day), headers=headers)
            content = response.content
            soup = BeautifulSoup(content,"html.parser")
            items = soup.find_all('li',class_= "styles_item__Sn_12")    
            i = 0 
            for item in items:
                try:
                        date = str(month) + '/' + str(day) + '/' + str(year)
                        weekday = datetime.date(year, month, day).weekday()
                        company_name = item.find('h3',class_ = "styles_font__m46I_ styles_medium__pDQUU styles_semiBold__yhRqL styles_title__jWi91 styles_lineHeight__kGlRn styles_underline__IqHIA").text
                        votes = item.find('span',class_ = "styles_font__m46I_ styles_black__Z9fG_ styles_small__lLD08 styles_semiBold__yhRqL styles_lineHeight__kGlRn styles_underline__IqHIA").text
                        votes = votes.replace(',','')
                        f.write(date + ',' + str(weekday) + ',' +company_name + ',' + votes + '\n' )
                except:
                    continue

f.close()

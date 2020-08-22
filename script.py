from bs4 import BeautifulSoup
import requests
from win10toast import ToastNotifier
url="http://worldometers.info/coronavirus/country/india/"
r=requests.get(url)
#parse the html content
soup=BeautifulSoup(r.content,"html.parser")

# New cases information
cases=soup.find("li", {"class":"news_li"}).strong

cases_information=cases.get_text()

#print(cases_information)

# New deaths information
deaths_information= list(soup.find("li", {"class":"news_li"}).strong.next_siblings)[1].text

#print(deaths)

# Notifier
notifier=ToastNotifier()

message=cases_information+ "\n" + deaths_information

#print(message)

notifier.show_toast(title="Covid-19 update", msg=message ,duration=5 , icon_path="virus.ico" )
True
 


from plyer import notification
from bs4 import BeautifulSoup
import time
import requests
def getDesktopNotification(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="corona.ico",
        timeout=10
    )

def getDataFromWebsite(url):
    scrappedData=requests.get(url)
    return scrappedData.text
if __name__ == "__main__":
    #getDesktopNotification("Abhishek","You recieved the desktop notification" )
    scraped_HTML_Data=getDataFromWebsite("https://www.mohfw.gov.in")
    #print(scraped_HTML_Data)
    myData=""
    soup=BeautifulSoup(scraped_HTML_Data,'html.parser')
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myData+=tr.get_text()

    #print(myData)
    #print("******************************************************************************************************")
    myData=myData[1:]
    itemList=myData.split('\n\n')
    #print(itemList)
    states=['Bihar','Rajasthan','West Bengal','Delhi']
    dataList=None
    for element in itemList[0:27]:
        dataList=element.split('\n')
        if dataList[1] in states:
            print(dataList)
            notification_title="COVID-19 Cases in India"
            notification_message=f"State: {dataList[1]}\nConfirmed case: {dataList[2]}\nDischarged: {dataList[3]}\nDeath: {dataList[4]}"
            getDesktopNotification(notification_title,notification_message)
            time.sleep(4)




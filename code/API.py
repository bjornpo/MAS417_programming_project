#import json
import requests



def createRequestLink(parameters):
    year = parameters["Year"]
    month = parameters["Month"]
    day = parameters["Day"]
    area = parameters["PriceArea"]
    link =    "https://www.hvakosterstrommen.no/api/v1/prices/{}/{}-{}_{}.json".format(year, month,day,area)
    #print (link)
    return link
    
    

def getElectricityPrice(userInput):
    requestLink = createRequestLink(userInput);
    response = requests.get(requestLink)  #gets the status code from the request
    statusCode = response.status_code
    jsonData = response.json()  #returns the json file contents from the response in a dict format
    
    info = [jsonData, statusCode]
    return info
  


if __name__ == '__main__':
    getElectricityPrice()
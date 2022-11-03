import json
#import UI_mock.py

#parameters = getUserInput()



rawData = '[{"NOK_per_kWh":0.92542,"EUR_per_kWh":0.08906,"EXR":10.391,"time_start":"2022-10-27T00:00:00+02:00",' \
          '"time_end":"2022-10-27T01:00:00+02:00"},{"NOK_per_kWh":0.96771,"EUR_per_kWh":0.09312999999999999,' \
          '"EXR":10.391,"time_start":"2022-10-27T01:00:00+02:00","time_end":"2022-10-27T02:00:00+02:00"},' \
          '{"NOK_per_kWh":0.98818,"EUR_per_kWh":0.09509999999999999,"EXR":10.391,' \
          '"time_start":"2022-10-27T02:00:00+02:00","time_end":"2022-10-27T03:00:00+02:00"},{"NOK_per_kWh":0.96667,' \
          '"EUR_per_kWh":0.09303,"EXR":10.391,"time_start":"2022-10-27T03:00:00+02:00",' \
          '"time_end":"2022-10-27T04:00:00+02:00"},{"NOK_per_kWh":0.99016,"EUR_per_kWh":0.09529,"EXR":10.391,' \
          '"time_start":"2022-10-27T04:00:00+02:00","time_end":"2022-10-27T05:00:00+02:00"},{"NOK_per_kWh":1.10134,' \
          '"EUR_per_kWh":0.10599,"EXR":10.391,"time_start":"2022-10-27T05:00:00+02:00",' \
          '"time_end":"2022-10-27T06:00:00+02:00"},{"NOK_per_kWh":1.24848,"EUR_per_kWh":0.12015,"EXR":10.391,' \
          '"time_start":"2022-10-27T06:00:00+02:00","time_end":"2022-10-27T07:00:00+02:00"},{"NOK_per_kWh":1.33971,' \
          '"EUR_per_kWh":0.12893000000000002,"EXR":10.391,"time_start":"2022-10-27T07:00:00+02:00",' \
          '"time_end":"2022-10-27T08:00:00+02:00"},{"NOK_per_kWh":1.39697,"EUR_per_kWh":0.13444,"EXR":10.391,' \
          '"time_start":"2022-10-27T08:00:00+02:00","time_end":"2022-10-27T09:00:00+02:00"},{"NOK_per_kWh":1.35644,' \
          '"EUR_per_kWh":0.13054,"EXR":10.391,"time_start":"2022-10-27T09:00:00+02:00",' \
          '"time_end":"2022-10-27T10:00:00+02:00"},{"NOK_per_kWh":1.31145,"EUR_per_kWh":0.12621,"EXR":10.391,' \
          '"time_start":"2022-10-27T10:00:00+02:00","time_end":"2022-10-27T11:00:00+02:00"},{"NOK_per_kWh":1.19735,' \
          '"EUR_per_kWh":0.11523,"EXR":10.391,"time_start":"2022-10-27T11:00:00+02:00",' \
          '"time_end":"2022-10-27T12:00:00+02:00"},{"NOK_per_kWh":1.087,"EUR_per_kWh":0.10461,"EXR":10.391,' \
          '"time_start":"2022-10-27T12:00:00+02:00","time_end":"2022-10-27T13:00:00+02:00"},{"NOK_per_kWh":1.01759,' \
          '"EUR_per_kWh":0.09793,"EXR":10.391,"time_start":"2022-10-27T13:00:00+02:00",' \
          '"time_end":"2022-10-27T14:00:00+02:00"},{"NOK_per_kWh":1.06664,"EUR_per_kWh":0.10265,"EXR":10.391,' \
          '"time_start":"2022-10-27T14:00:00+02:00","time_end":"2022-10-27T15:00:00+02:00"},{"NOK_per_kWh":1.2066,' \
          '"EUR_per_kWh":0.11612,"EXR":10.391,"time_start":"2022-10-27T15:00:00+02:00",' \
          '"time_end":"2022-10-27T16:00:00+02:00"},{"NOK_per_kWh":1.29243,"EUR_per_kWh":0.12437999999999999,' \
          '"EXR":10.391,"time_start":"2022-10-27T16:00:00+02:00","time_end":"2022-10-27T17:00:00+02:00"},' \
          '{"NOK_per_kWh":1.25274,"EUR_per_kWh":0.12056,"EXR":10.391,"time_start":"2022-10-27T17:00:00+02:00",' \
          '"time_end":"2022-10-27T18:00:00+02:00"},{"NOK_per_kWh":1.26978,"EUR_per_kWh":0.1222,"EXR":10.391,' \
          '"time_start":"2022-10-27T18:00:00+02:00","time_end":"2022-10-27T19:00:00+02:00"},{"NOK_per_kWh":1.2835,' \
          '"EUR_per_kWh":0.12351999999999999,"EXR":10.391,"time_start":"2022-10-27T19:00:00+02:00",' \
          '"time_end":"2022-10-27T20:00:00+02:00"},{"NOK_per_kWh":1.25721,"EUR_per_kWh":0.12099,"EXR":10.391,' \
          '"time_start":"2022-10-27T20:00:00+02:00","time_end":"2022-10-27T21:00:00+02:00"},{"NOK_per_kWh":1.28744,' \
          '"EUR_per_kWh":0.12390000000000001,"EXR":10.391,"time_start":"2022-10-27T21:00:00+02:00",' \
          '"time_end":"2022-10-27T22:00:00+02:00"},{"NOK_per_kWh":1.19091,"EUR_per_kWh":0.11461,"EXR":10.391,' \
          '"time_start":"2022-10-27T22:00:00+02:00","time_end":"2022-10-27T23:00:00+02:00"},{"NOK_per_kWh":1.0204,' \
          '"EUR_per_kWh":0.09820000000000001,"EXR":10.391,"time_start":"2022-10-27T23:00:00+02:00",' \
          '"time_end":"2022-10-28T00:00:00+02:00"}] '
APIdata = json.loads(rawData)  # convert from Json to dict


def getElectricityPrice(userInput):
    """
    response = requests.get("https://api.open-notify.org/astros.json") #sends a request to the API endpoint
    #response = requests.get("https://www.hvakosterstrommen.no/strompris-api",  params=parameters)
    print(response.status_code) #prints the status code from the request
    print(response.json())  #prints the data received from the API
    """
    y = {
        "APIdata": APIdata,
        "HTTP_response": 200
    }
    return y



"""
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
"""


if __name__ == '__main__':
    print(json.dumps(APIdata, indent=4))
    # print(APIdata[12]["NOK_per_kWh"])    #Print price at 12:00

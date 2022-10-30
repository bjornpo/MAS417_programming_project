
def getUserInput():
    userinput = {
        "PriceArea": "NO5",         #NO1/NO2/NO3/NO4/NO5
        "Year": "2022",             #Always four digits
        "Month": "10",              #Always two digits, first digit 0 
        "Day": "27"                 #Always two digits, first digit 0 
    }
    return userinput


if __name__ == '__main__':
    print(getUserInput())

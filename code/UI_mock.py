
from datetime import date


def getUserInput():
    
    #get the date
    dateInput = input("Select Date (year-mo-day): ").split('-')
    print(dateInput)    
    year, month, day = [int(item) for item in dateInput]
    
    #get the area
    print("NO1 = Oslo\ Øst-Norge")
    print("NO2 = Kristiansand / Sør-Norge" )
    print("NO3 = Trondheim / Midt-Norge")
    print("NO4 = Tromsø / Nord-Norge") 
    print("NO5 = Bergen / Vest-Norge): ")
    area = input ("Select Area: ")
    
    userinput = {
        "PriceArea": area,         #NO1/NO2/NO3/NO4/NO5
        "Year": year,             #Always four digits
        "Month": month,              #Always two digits, first digit 0 
        "Day": day                 #Always two digits, first digit 0 
    }
    return userinput




if __name__ == '__main__':
    print(getUserInput())


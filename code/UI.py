import datetime

loop=False    #used in order to print the area code text only on the first area input attempt.


def getUserInput():
    date = getDate()
    year, month, day = [str(item) for item in date]
    area = getArea()
    userInput = {
        "PriceArea": area,         #NO1/NO2/NO3/NO4/NO5
        "Year": year,             #Always four digits
        "Month": month,              #Always two digits, first digit 0 
        "Day": day                 #Always two digits, first digit 0 
    }
    return userInput

def getDate():
    
    correctForm = False
    
    #if wrong input is entered, keep asking for correct input.
    while not correctForm:
        
        #get input from user
        dateInput = input("Select Date (year-month-day): ")  
        
        #remove empty spaces from string      
        dateInput = dateInput.strip()         
              
        #iterate through string until you find any type of date separator (. / or -)   
        for x in dateInput:
            if x=="-":
                typeOfSeparator = x
                break
            elif x==".":
                typeOfSeparator = x
                break
            elif x=="/":
                typeOfSeparator = x
                break
            else:        #no separator was found
                typeOfSeparator = "0"     
                
     
        if typeOfSeparator != "0":
            
            #split date into month day and year at the separator points
            dateInput = dateInput.split(typeOfSeparator)
            
            #date split should give 3 values else date format is wrong
            if len(dateInput)==3:
                
                #split date into variables
                year, month, day = [str(item) for item in dateInput]
                
                #check the variables if they are valid
                check1 = numbersCheck(year,month,day)
                check2 = validDateCheck(year, month, day)
                
                if check1 and check2:
                    return dateInput
                    correctForm=True
                    break
                else:
                    wrongInput(4)            
                    
            else: #if too many or too few separators are found, date is wrong
                wrongInput(4)
                    
        else:   #if no separator is found, the date is wrong
            wrongInput(4)
        
    
    
    
def getArea():
    correctArea = False
    while correctArea == False: 
        if loop==False:
            print("NO1 = Oslo\ Øst-Norge")
            print("NO2 = Kristiansand / Sør-Norge" )
            print("NO3 = Trondheim / Midt-Norge")
            print("NO4 = Tromsø / Nord-Norge") 
            print("NO5 = Bergen / Vest-Norge): ")
            area = input ("Select Area: ")
        else:
            area = input ("Select Area: ")
        if len(area)==3:
            correctArea = checkArea(area);
            if correctArea==True:
                return area
            else:
                wrongInput(1)
        else:
            wrongInput(1)
                
   
    
def checkArea(area):
    if (area[0] == "N" and area[1] == "O"):
        if area[2]== "1" or area[2]== "2" or area[2]==  "3" or area[2]==  "4" or area[2]== "5":
            print("this is area", area[2])
            return True
        else: 
            return False            
    else:
        return False
                
           



#DOES THE DATE CONSIST OF NUMBERS?
def numbersCheck(year,month,day):
    
    c=True
    
    if len(year) == 4 and len(month)==2 and len(day) ==2:
        for x in year:
            if ord(x)<48 or ord(x)>57:
                c=False;
                return False;
        for x in month:
            if ord(x)<48 or ord(x)>57:
                c=False;
                return False;
        for x in day:
            if ord(x)<48 or ord(x)>57:
                c=False;
                return False;
        if c==True:    
            return True
        else:
            return False
    else: 
        return False




#IS THE DATE WITHIN A VALID RANGE FOR THE API?
def validDateCheck(year,month,day):
    today = datetime.date.today()
    date = datetime.date(int(year), int(month), int(day))
    
    #the API provides dates only after 1 sept 2022
    APIlimit = datetime.date(2022,9,1)
    
    if date>today: 
        wrongInput(2)
        return False
    elif date < APIlimit:
        wrongInput(3)
        return False
    else:
        return True
    
  






def wrongInput(x):
    global loop
    if x==1:
        print("Please insert the area code in the correct form.")
        loop=True
    elif x==2:
        print("The app cannot display price data from the future.")
    elif x==3:
        print("The app can only display price data from 1/9/2022 and after.")
    else:
        print("Please insert the date in the correct form.")
    

if __name__ == '__main__':
   userInput = getUserInput()


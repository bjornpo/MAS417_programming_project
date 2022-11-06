import UI
import API
import generateSTL_mock
from API import getElectricityPrice

def main():
    userInput = UI.getUserInput()
    APIdata = getElectricityPrice(userInput)

    
    """"
    if(APIdata["HTTP_response"] == 200):
        STL = generateSTL_mock.generateSTL(userInput, APIdata["APIdata"])
        str = "STL file: " + STL["fileName"] + "is ready, and is stored at " + STL["filePath"]
        print(str)
    else:
        str = "HTTP error " + APIdata["HTTP_response"]
        print(str)
    """

if __name__ == '__main__':
    main()

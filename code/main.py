import UI as UI
import API as API
import generateSTL as generateSTL

def main():
    userInput = UI.getUserInput()
    APIdata = API.getElectricityPrice(userInput)
    #print(APIdata)

    if(APIdata["HTTP_response"] == 200):
        STL = generateSTL.generateSTL(userInput, APIdata["APIdata"])
        str = "STL-file generated\n Filename: " + STL["fileName"] + "\n File location: " + STL["filePath"]
        print(str)
    else:
        str = "HTTP error " + APIdata["HTTP_response"]
        print(str)


if __name__ == '__main__':
    main()

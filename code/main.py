import UI_mock
import API_mock
import generateSTL_mock

def main():
    userInput = UI_mock.getUserInput()
    APIdata = API_mock.getElectricityPrice(userInput)

    if(APIdata["HTTP_response"] == 200):
        STL = generateSTL_mock.generateSTL(userInput, APIdata["APIdata"])
        str = "STL file: " + STL["fileName"] + "is ready, and is stored at " + STL["filePath"]
        print(str)
    else:
        str = "HTTP error " + APIdata["HTTP_response"]
        print(str)


if __name__ == '__main__':
    main()

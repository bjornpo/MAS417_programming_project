import requests
import numpy
from stl import mesh


def generateSTL():
    fileInfo = {
        "fileName": "Filename",
        "filePath": "FilePath"
    }
    return fileInfo


def createRequestLink(parameters):
    year = parameters["Year"]
    month = parameters["Month"]
    day = parameters["Day"]
    area = parameters["PriceArea"]
    link = "https://www.hvakosterstrommen.no/api/v1/prices/{}/{}-{}_{}.json".format(year, month, day, area)
    #print (link)
    return link


def getElectricityPrice(userInput):
    requestLink = createRequestLink(userInput)
    response = requests.get(requestLink)  #gets the status code from the request
    #print(response.status_code)
    jsonData = response.json()  #returns the json file contents from the response in a dict format
    #print(response.json()[0])
    return jsonData


if __name__ == '__main__':

    #UI = {
    #    "PriceArea": input("Price Area: "),
    #    "Year": input("Year: "),
    #    "Month": input("Month: "),
     #   "Day": input("Day: ")
    #}

    dummyUI = {
        "PriceArea": "NO5",
        "Year": "2022",
        "Month": "10",
        "Day": "27"
    }

    jsonData = getElectricityPrice(dummyUI)

    NOK_per_kWh = []

    for index, item in enumerate(jsonData):
        NOK_per_kWh.append(jsonData[index]["NOK_per_kWh"])

    print(NOK_per_kWh)

    vertices = numpy.empty((0, 3), float)
    faces = numpy.empty((0, 3), int)

    for index, item in enumerate(jsonData):
        vertices = numpy.append(vertices, [[index, 0, 0]], axis=0)
        vertices = numpy.append(vertices, [[index, 10*NOK_per_kWh[index],0]], axis=0)


    for index, item in enumerate(vertices):
        faces = numpy.append(faces, [[index-2, index -1, index]], axis=0)
        #faces = numpy.append(faces, [[index + 5, index + 4, index + 3]], axis=0)
    print(vertices)

    cube = mesh.Mesh(numpy.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = vertices[f[j],:]

    # Write the mesh to file "cube.stl"
    cube.normals
    cube.save('cube.stl')

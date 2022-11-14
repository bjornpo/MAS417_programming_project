import cadquery as cq
import math
from cadquery import exporters
from pathlib import Path

def generateSTL(userInput, APIdata):

    baseWidth = 170
    baseDepth = 45
    baseHeigth = 40
    baseTh = 2
    barSenterToEdge = 5
    barDepth = 8
    barWidth = 5

    try:
        highestPrice = max([x['NOK_per_kWh'] for x in APIdata])
    except:
        highestPrice = 3.0
        print(f'Unable to find maximum price. assume {highestPrice}kr')

    #Scale the height of the barchart based on maximum price
    if highestPrice < 1.0:
        Hfactor = 100 #mm barheight pr. krone
    elif highestPrice < 2.5:
        Hfactor = 50
    elif highestPrice < 5.0:
        Hfactor = 25
    else:
        Hfactor = 20

    year = userInput.get('Year', "YYYY")
    month = userInput.get('Month', "MM")
    day = userInput.get('Day', "DD")
    priceZone = userInput.get('PriceArea', "NOX")

    barSpacing = (baseWidth - barSenterToEdge*2)/23
    angle = math.degrees(math.atan((baseDepth-barDepth) / (baseHeigth-baseTh)))

    print("Generating stl-file. This may take several minutes")

    model = (
        cq.Workplane("YZ")
        .lineTo(baseDepth, 0)
        .lineTo(baseDepth, baseTh)
        .lineTo(barDepth, baseHeigth)
        .lineTo(0, baseHeigth)
        .close()
        .extrude(-baseWidth)
    )

    model = ( #Find workplane for nameplate
            model.faces(">Z").workplane(origin=(0,barDepth))
            .transformed(offset=cq.Vector(0, 0, 0), rotate=cq.Vector(angle-90,0,180))
            .tag("nameplate")
    )

    model = ( #Generating bar timestamp
            model.workplaneFromTagged("nameplate")
            .center(barSenterToEdge-barSpacing,-2)
            .transformed(offset=cq.Vector(0, 0, 0), rotate=cq.Vector(0,0,90))
            )
    #for h in range(1): #speed up processing time when testing
    for h, item in enumerate(APIdata):
        text = f'{h:02d}-{h+1:02d}'
        model = model.center(0,-barSpacing)
        model = model.text(txt=text, fontsize=barSpacing-0, distance=-0.5, halign="right", valign="center")

    model = ( #generating text for price-zone and date
            model.workplaneFromTagged("nameplate")
            .center(5 ,-50)
            #.text(txt="12-11-2022", fontsize=15, distance=-1, halign="left", valign="bottom")
            .text(txt=f'{day}-{month}-{year}', fontsize=15, distance=-1, halign="left", valign="bottom")
            .workplaneFromTagged("nameplate")
            .center(baseWidth-5 ,-50)
            .text(txt=f'{priceZone}', fontsize=15, distance=-1, halign="right", valign="bottom")
            .workplaneFromTagged("nameplate")
            .center(baseWidth/2,-35)
            .text(txt=f'Spot-price electricity (1kr = {Hfactor}mm)', fontsize=10, distance=-1, halign="center", valign="bottom")
            )

    #generate bars
    model = model.faces(">Z").workplane(origin=(-barSenterToEdge+barSpacing,barDepth/2))#.box(10,10,10)
    #for h in range(1): #speed up time during testing
    for h, item in enumerate(APIdata):
        try:
            price = APIdata[h]["NOK_per_kWh"]
        except:
            price = 0.001
            print("Error getting value from API-data")

        model = model.center(-barSpacing,0).box(barWidth, barDepth, price*Hfactor, centered=[True,True,False])

    #export stl-file
    filePath = Path().cwd() / 'stl_files'
    filePath.mkdir(parents=True, exist_ok=True) #Create directory if it not exsists
    filename = f'{year}_{month}_{day}_{priceZone}.stl'
    exporters.export(model, str(filePath / filename))

    fileInfo = {
        "fileName": str(filename),
        "filePath": str(filePath)
    }
    return fileInfo

if __name__ == '__main__':
    generateSTL({}, [{}])

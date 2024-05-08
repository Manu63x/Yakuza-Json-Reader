import json

def getItemsNumber(jsonFile):
    f = open(jsonFile)
    data = json.load(f)
    return data['ROW_COUNT']

def printAllItems(jsonFile):
    f = open(jsonFile)
    data = json.load(f)
    totalObjNumber = data['ROW_COUNT']
    for i in range(totalObjNumber):
        a = json.dumps(data['' + str(i)])
        for key in json.loads(a):
            objCat = data['' + str(i)]['' + key]['category']
            if(objCat == 2 or objCat == 3 or objCat == 4 or objCat == 5 or objCat == 6 or objCat == 7):
                print(data['' + str(i)]['' + key]['name'])
                print(data['' + str(i)]['' + key]['explanation'])
                print('\n')
    f.close()


def printAllItemsOnFile(jsonFile, outputFile):
    f = open(jsonFile)
    f2 = open(outputFile, 'w')
    data = json.load(f)
    totalObjNumber = data['ROW_COUNT']
    for i in range(totalObjNumber):
        a = json.dumps(data['' + str(i)])
        for key in json.loads(a):
            objCat = data['' + str(i)]['' + key]['category']
            if(objCat == 2 or objCat == 3 or objCat == 4 or objCat == 5 or objCat == 6 or objCat == 7):
                string = data['' + str(i)]['' + key]['name'] + '\n' + data['' + str(i)]['' + key]['explanation'] + '\n\n'
                f2.write(string)
    f.close()

def printInnerTags(jsonFile, topObjID):
    f = open(jsonFile)
    data = json.load(f)
    a = json.dumps(data[topObjID])
    for key in json.loads(a):
        print(key)

def getNameById(jsonFile, topObjID):
    f = open(jsonFile)
    data = json.load(f)
    f.close()
    a = json.dumps(data['' + str(topObjID)])
    for key in json.loads(a):
        return data['' + str(topObjID)]['' + key]['name']

def getExplanationById(jsonFile, topObjID):
    f = open(jsonFile)
    data = json.load(f)
    f.close()
    a = json.dumps(data['' + str(topObjID)])
    for key in json.loads(a):
        return data['' + str(topObjID)]['' + key]['explanation']

# printAllItems('item.json')
# print(getExplanationById('item.json', 2951))
from conected import *
from conected import *

dictionary= findItems(conected())


def recursiveCreateAllMats(material,allMats):
    mat= viewItem(dictionary.get(material))   

    for nodeMat in mat.dictNecessaryMaterias.keys():
        
        if ("Vein" in nodeMat):
            continue
        
        try:
            allMats[nodeMat] += mat.dictNecessaryMaterias[nodeMat]
        except:
            allMats[nodeMat] = mat.dictNecessaryMaterias[nodeMat]
        
        recursiveCreateAllMats(nodeMat,allMats)       
    
    return
    

def createDictAllMats(material,allMats):
    mat= viewItem(dictionary.get(material))   

    for nodeMat in mat.dictNecessaryMaterias.keys():
        
        try:
            allMats[nodeMat] += mat.dictNecessaryMaterias[nodeMat]
        except:
            allMats[nodeMat] = mat.dictNecessaryMaterias[nodeMat]
            
        recursiveCreateAllMats(nodeMat,allMats)
        


    return allMats




allMats=createDictAllMats("Electromagnetic Matrix",{})

print(allMats)



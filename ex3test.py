with open("testFile.txt") as f:
    parse = f.read().replace("\n", " ").split(" ")
    data = [word for word in parse if word is not ""]
f.close()
def Caps (data):
    FinalList=[]   
    for word in data:
        
        for letter in word[1:]:
            if letter.isupper():
                FinalList.append(word)
                break
    return FinalList

def lowerSort(FinalList):
    return FinalList.lower()

printList = Caps(data)

printList.sort(key=lowerSort)
print (printList)


        
    
    

with open("testFile2.txt") as f:
    parse = f.read().replace("\n", " ").split(" ")
    data = [word for word in parse if word is not ""]
f.close()

def Surrounded (word,index):
    if index == 0 or index == len(word)-1:
        return False
    return word[index-1].isalpha() and word[index+1].isalpha()
                
                
def NonAlpha (data):
    FinalList=[]
    for word in data:
        for index, letter in enumerate(word):
            
            if not letter.isalpha():
                if Surrounded(word,index):
                    FinalList.append(letter)
                    
                
                
    return FinalList
print (NonAlpha(data))

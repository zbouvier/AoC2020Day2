def partOne():
    f = open('values.txt', 'r+')
    count = 0
    for line in f.readlines(): #some REGEX stuff can cleanup like 85% of this code may do later
        minValueOfCharacters = line.split("-")[0] #12
        maxValueOfCharacters = line.split("-")[1].split(" ")[0] #15
        targetCharacter = line.split("-")[1].split(" ")[1].split(":")[0] #q
        targetLine = line.split("-")[1].split(" ")[2].rstrip() #qqqqqqqqqqxq
        charCount = 0
        for ch in targetLine:
            if(ch == targetCharacter):
                charCount=charCount+1
        if((charCount <= int(maxValueOfCharacters) and charCount >= int(minValueOfCharacters)) or (charCount <= int(minValueOfCharacters) and charCount >= int(maxValueOfCharacters))):
            count+=1
    f.close()
    return count

def partTwo():
    f = open('values.txt', 'r+')
    count = 0
    for line in f.readlines(): #some REGEX stuff can cleanup like 85% of this code may do later
        minValueOfCharacters = int(line.split("-")[0]) - 1 #12 - 1
        maxValueOfCharacters = int(line.split("-")[1].split(" ")[0]) - 1 #15 - 1
        targetCharacter = line.split("-")[1].split(" ")[1].split(":")[0] #q
        targetLine = line.split("-")[1].split(" ")[2].rstrip() #qqqqqqqqqqxq
        if (targetLine[minValueOfCharacters] == targetCharacter and targetLine[maxValueOfCharacters] != targetCharacter) ^ (targetLine[maxValueOfCharacters] == targetCharacter and targetLine[minValueOfCharacters] != targetCharacter):
            count+=1 #Uses XOR operator ^ 
    f.close()
    return count



print(partOne())
print(partTwo())


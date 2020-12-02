import re
f = open('values.txt', 'r+')
def partOne():
    count = 0
    for line in f.readlines():
        woFirstValue = line.split("-")
        minValueOfCharacters = woFirstValue[0]
        woSecondValue = woFirstValue[1].split(" ")
        maxValueOfCharacters = woSecondValue[0]
        targetCharacter = woSecondValue[1].split(":")[0]
        #print(woSecondValue)
        targetLine = woSecondValue[2].rstrip()
        #print(woSecondValue[2])
        #print(minValueOfCharacters + "  " + maxValueOfCharacters + "  " + targetCharacter + "  " + targetLine)
        charCount = 0
        for ch in targetLine:
            #print("comp " + ch + " to "+ targetCharacter)
            if(ch == targetCharacter):
                charCount=charCount+1
        #print(charCount)
        if((charCount <= int(maxValueOfCharacters) and charCount >= int(minValueOfCharacters)) or (charCount <= int(minValueOfCharacters) and charCount >= int(maxValueOfCharacters))):
            count+=1
    return count

def partTwo():
    validCount = 0
    for line in f.readlines():
        woFirstValue = line.split("-")
        minValueOfCharacters = int(woFirstValue[0]) - 1
        woSecondValue = woFirstValue[1].split(" ")
        maxValueOfCharacters = int(woSecondValue[0]) - 1
        targetCharacter = woSecondValue[1].split(":")[0]
        targetLine = woSecondValue[2].rstrip()
        if(targetLine[minValueOfCharacters] == targetCharacter and targetLine[maxValueOfCharacters] == targetCharacter):
            print(str(minValueOfCharacters) + "  " + str(maxValueOfCharacters) + "  " + targetCharacter + "  " + targetLine + " is invalid")
        elif(targetLine[minValueOfCharacters] == targetCharacter and targetLine[maxValueOfCharacters != targetCharacter]):
            validCount+=1
        elif(targetLine[maxValueOfCharacters] == targetCharacter and targetLine[minValueOfCharacters != targetCharacter]):
            validCount+=1
        else:
            print(str(minValueOfCharacters) + "  " + str(maxValueOfCharacters) + "  " + targetCharacter + "  " + targetLine + " is invalid")
    return validCount



print(partTwo())

f.close()
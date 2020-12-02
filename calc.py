def partOne():
    f = open('values.txt', 'r+')
    count = 0
    for line in f.readlines(): #some REGEX stuff can cleanup like 85% of this code may do later
        minValueOfCharacters = line.split("-")[0]
        maxValueOfCharacters = line.split("-")[1].split(" ")[0]
        targetCharacter = line.split("-")[1].split(" ")[1].split(":")[0]
        targetLine = line.split("-")[1].split(" ")[2].rstrip()
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
        minValueOfCharacters = int(line.split("-")[0]) - 1
        maxValueOfCharacters = int(line.split("-")[1].split(" ")[0]) - 1
        targetCharacter = line.split("-")[1].split(" ")[1].split(":")[0]
        targetLine = line.split("-")[1].split(" ")[2].rstrip()
        if(targetLine[minValueOfCharacters] == targetCharacter and targetLine[maxValueOfCharacters] == targetCharacter):
            pass # skips the double whammies
        elif((targetLine[minValueOfCharacters] == targetCharacter and targetLine[maxValueOfCharacters != targetCharacter]) or (targetLine[maxValueOfCharacters] == targetCharacter and targetLine[minValueOfCharacters != targetCharacter])):
            validCount+=1
    f.close()
    return count



print(partOne())
print(partTwo())


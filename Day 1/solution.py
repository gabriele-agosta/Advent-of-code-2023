res = 0
hashMap = {"one":1, "two":2, "three":3, 
           "four":4, "five":5, "six":6,
           "seven":7, "eight":8, "nine":9}

with open("calibration_doc.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        left, right = 0, len(line) - 1
        while left < len(line) and not line[left].isdigit():
            left += 1
        while right > 0 and not line[right].isdigit():
            right -= 1

        if left < len(line): firstDigit = line[left]
        if right > -1: secondDigit = line[right]

        temp = 0
        tempWord = ""
        found = False
        while temp < left and not found:
            tempWord += line[temp] 
            for key in hashMap:
                if key in tempWord:
                    firstDigit = hashMap[key]
                    found = True
                    break
            temp += 1
        
        temp = len(line) - 1
        tempWord = ""
        found = False
        while temp > right and not found:
            tempWord = line[temp] + tempWord
            for key in hashMap:
                if key in tempWord:
                    secondDigit = hashMap[key]
                    found = True
                    break
            temp -= 1

        n = str(firstDigit) + str(secondDigit)
        res += int(n)
    
print(res)
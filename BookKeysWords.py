import re
#program read text file and create key words with their lines numbers

def main():
    #creating list to store lines of text in file
    data = []
    #opening file ad reading data
    with open('just550lines.txt', 'r',encoding='UTF-8') as f:
        data = f.readlines()
        f.close()
    #create list to keep lines of text without any other than punctations
    lines = []
    string = ''

    for x in data:
        #z = x.replace('\n', '')
        z = x
        #d = z.replace('"', '')
        d = re.sub(r"[^a-zA-Z0-9_]+" , ' ', z)

        lines.append(d)
    #print(lines)

    #creating one string with all lines
    for y in lines:
        string = string + y
        string = string + ' '

    #creating words list
    words = string.split()

    #creating key words list
    keyWords = list(dict.fromkeys(words))




    #storing lines numbers for keys words
    counter = 0
    counter1 = 0
    keyLinesNumbers = [[0 for x in range(2)] for i in range(len(keyWords))]
    progress = len(keyWords)

    for x in keyWords:
        c = x
        keyLinesNumbers[counter][0] = c
        counter = counter + 1


    for x in keyWords:
        counter = 0
        xLines = []
        for y in lines:
        
            wordsx = y.split()

            for a in wordsx:
            

                if x == a:
                    v = counter
                    xLines.append(v)
               
            counter = counter + 1
        keyLinesNumbers[counter1][1] = xLines  
        #print(x)
        #print(xLines)
    
    
        counter1 = counter1 + 1
        print('Done '+ str(counter1)+' keywords from '+ str(progress) +'.')


    #print(keyLinesNumbers)

    #creating file with results
    stringFile = ''
    with open('keywords.txt', 'w') as k:

        for x in keyLinesNumbers:

            keyWord = x[0]
            yLines = x[1]
            addString = str(keyWord) + ' - ' + str(yLines) + '\n'
            stringFile = stringFile + addString
        
        k.write(stringFile)
        k.close()


main()

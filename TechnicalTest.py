def main():
    strArr =  ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]
    #strArr =  ["abcgefd", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]
    strArr[0] = strArr[0].lower()
    strArr[1] = strArr[1].lower()
    print("Resultado: " + WordSplit(strArr))

def WordSplit(strArr):
    outPut = "Not possible"
    dictionaryWord = strArr[1].split(',')
    for index in range(len(strArr[0])):
        if (strArr[0][:index] in dictionaryWord and 
            strArr[0][index:] in dictionaryWord):
            outPut = strArr[0][:index] + "," + strArr[0][index:]
            break
    return outPut

if __name__ == '__main__':
    import sys
    sys.exit(int (main() or 0))
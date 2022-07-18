def main():
    #strArr =  ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]
    strArr =  ["abcgefd", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]
    strArr[0] = strArr[0].lower()
    strArr[1] = strArr[1].lower()
    print(WordSplit(strArr))

def WordSplit(strArr):
    contIndex = 1
    return RecursiveWordSplit(strArr,contIndex)

def RecursiveWordSplit(strArr,contIndex):
    if contIndex < (len(strArr[0])):
        if (strArr[0][0:contIndex] in strArr[1]) and (strArr[0][contIndex:len(strArr[0])] in strArr[1]):
            return strArr[0][0:contIndex] + "," + strArr[0][contIndex:len(strArr[0])]
        else:
            return RecursiveWordSplit(strArr,contIndex + 1)
    else:
        return "not possible"

if __name__ == '__main__':
    import sys
    sys.exit(int (main() or 0))
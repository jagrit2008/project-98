def countWordsFromFile():
    fileName =  input("Enter the file name:- ")

    

    with open(fileName , 'r') as a:
        data_a = a.read()
    
    with open(fileName , 'w') as a:
     a.write(data_b)





countWordsFromFile()
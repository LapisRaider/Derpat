param_dict = {}

def init_parameters(fileName):
    file = open(fileName)
    print("this is called")
    for line in file:        
        #ignore comments
        if line.startswith("#") or line.startswith("\n"):
            continue

        modifiedLine = line.strip() # remove \n
        modifiedLine = modifiedLine.split(' = ') # split to variable name and value
        #print(modifiedLine)
        param_dict[modifiedLine[0]] = modifiedLine[1];


init_parameters("src/assets/data/parameters.txt")

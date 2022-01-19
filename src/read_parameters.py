param_dict = {}

def init_parameters(fileName):
    file = open(fileName)
    for line in file:        
        #ignore comments
        if line.startswith("#"):
            continue

        modifiedLine = line.strip()
        modifiedLine = modifiedLine.split(' = ')
        param_dict[modifiedLine[0]] = modifiedLine[1];


init_parameters("src/assets/data/parameters.txt")

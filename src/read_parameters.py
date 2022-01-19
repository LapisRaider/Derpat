param_dict = {}
asset_param_dist = {}
text_param = []

def init_parameters(fileName, dict):
    file = open(fileName)
    for line in file:        
        #ignore comments
        if line.startswith("#") or line.startswith("\n"):
            continue

        modifiedLine = line.strip() # remove \n
        modifiedLine = modifiedLine.split(' = ') # split to variable name and value
        #print(modifiedLine)
        dict[modifiedLine[0]] = modifiedLine[1];

def init_text_parameters(fileName):
    file = open(fileName,'r', encoding='UTF-8')
    for line in file:
        #ignore comments
        if line.startswith("#") or line.startswith("\n"):
            continue

        modifiedLine = line.strip()
        text_param.append(modifiedLine)
       

init_parameters("src/assets/data/parameters.txt", param_dict)
init_parameters("src/assets/data/asset_params.txt", asset_param_dist)
init_text_parameters("src/assets/data/text_window_params.txt")
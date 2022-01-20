state_param_dict = {}
asset_param_dict = {}
note_param = []

def init_parameters(file_name, dict):
    file = open(file_name)
    for line in file:        
        # Ignore comments.
        if line.startswith("#") or line.startswith("\n"):
            continue

        modified_line = line.strip() # Remove \n.
        modified_line = modified_line.split(' = ') # Split into variable name and value.
        dict[modified_line[0]] = modified_line[1]

def init_note_parameters(file_name):
    file = open(file_name,'r', encoding='UTF-8')
    for line in file:
        # Ignore comments.
        if line.startswith("#") or line.startswith("\n"):
            continue

        modified_line = line.strip()
        note_param.append(modified_line)
       

init_parameters("assets/data/state_params.txt", state_param_dict)
init_parameters("assets/data/asset_params.txt", asset_param_dict)
init_note_parameters("assets/data/note_params.txt")
import re
import linecache

varname_pattern = r'(^\:\:\s*)(\S+)\s+(\S+)(?=\s*\=)'

class tree:
    def __init__(self, type: str, var_name: str, raw_declaration: str) -> None:
        self._children = []
        self.type = type
        self.var_name = var_name
        self._raw_declaration = raw_declaration

def findUserSelection(file, type_name, var_name=None):
    with open(file) as source:
        variable_locations = [[x, _treename] for x,varname in enumerate(source, 1) if re.match(varname_pattern, varname, re.IGNORECASE) and (_treename:=(re.search(varname_pattern, varname, re.IGNORECASE).group(2))) == type_name]
        for location in variable_locations:
            raw_declaration = ""
            i = 0
            while True:
                line = linecache.getline(file, location[0]+i)
                if i == 0 or ("|" in line and (not ("::" in line) and not ("=" in line))) or line[0] == "\n":
                    raw_declaration += line
                    i += 1
                else:
                    break
            print(re.sub("\n|\s{2,}", " ", raw_declaration.strip()))

        
        
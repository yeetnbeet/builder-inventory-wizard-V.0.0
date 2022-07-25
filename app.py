from cmath import nan
import csv ;

#config is the object that contains file locations and data for manipulations
class config :
    def __init__(self, builderFile = "./BUILDER.csv",framesFile = "./FRAMES.csv"):
        self.builderFile = builderFile
        self.framesFile = framesFile
    Aframes = []
    Abuilders = []
    fields = []

def dataINIT(config):
    builderCSV = config.builderFile
    framesCSV = config.framesFile  
    

    with open(framesCSV, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        config.fields = next(csvreader)
        for row in csvreader:
            config.Aframes.append(row)
    
    with open(builderCSV, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        Bfields = next(csvreader)
        for row in csvreader:
            config.Abuilders.append(row)

    return 

def syncronize(config):
    Aframes = config.Aframes
    Abuilders = config.Abuilders
    


if __name__ == "__main__":
    C = config()
    dataINIT(C)
    print()
    print(C.fields)
    for l in C.Aframes:
        print(l)

    syncronize(C)

    print()
    print(C.fields)
    for l in C.Aframes:
        print(l)

    
    

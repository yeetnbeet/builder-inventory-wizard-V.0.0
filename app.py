import csv ;

#config is the object that contains file locations and data for manipulations
class config :
    def __init__(self, builderFile = "./BUILDER.csv",framesFile = "./FRAMES.csv",outputFile = "./OUTPUT.csv"):
        self.builderFile = builderFile
        self.framesFile = framesFile
        self.outputFile = outputFile
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
    for i in Abuilders:
        for r in Aframes:
            if r[8] == i[8]:
                if r[16] != i[16] and r[11] == "Contender Park City" and i[11] == "Contender Park City":
                    print("*Triggered* PC SKU: ",i[8]," Changed: ",i[16]," to: ",r[16])
                    i[16] = r[16]    
                if r[16] != i[16] and r[11] == "Contender Salt Lake City" and i[11] == "Contender Salt Lake City":
                    print("*Triggered* SLC SKU: ",i[8]," Changed: ",i[16]," to: ",r[16])
                    i[16] = r[16]
                if r[16] != i[16] and r[11] == "Contender Warehouse" and i[11] == "Contender Warehouse":
                    print("*Triggered* WH SKU: ",i[8]," Changed: ",i[13]," to: ",r[13])
                    i[16] = r[16]

def output(config):
    outputCSV = config.outputFile
    with open(outputCSV,mode='w') as csvFile:
        writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(config.fields)
        for i in config.Abuilders:
            writer.writerow(i)


if __name__ == "__main__":
    C = config()
    dataINIT(C)
    print("\nTEST_LOGS:\n")
    syncronize(C)
    output(C)
    print("\n\n\n")

    
    

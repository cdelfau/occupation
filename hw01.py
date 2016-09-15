#Team Chlan - Chloe Delfau & Alan Chen
#SoftDev1 pd8
#HW01 -- Divine your Destiny
#2016-09-16


def main(filename, mode):
    #format data for processing
    f = open(filename, mode) #create new file object
    contents = f.read().split("\r\n") #parse plaintext by \r\n
    
    dictionary = dict() #create an empty dictionary
    
    #fill dictionary
    for pair in contents:
        if pair != "": #for stupid \n at the end of the file
            if pair[0] == '"': #if the pair contains quotes
                dictionary[pair.split('"')[1]] = float(pair.split('"')[2].split(",")[1])
            else:
                dictionary[pair.split(",")[0]] = float(pair.split(",")[1])

    #>:(
        


#DNA

#De4 Kvælstof baser
#1 Adenine  (A)
#2 Thymine  (T)
#3 Cytosine (C)
#4 Guanine  (G)

#Purinbaser og Pyrimidinbaser
# Baserne kan opdeles i to kategorier, purinbaser og pyrimidinbaser.
# Adenine og Guanine er purinbaser. Thymine og Cytosine er pyrimidbaser.
# Purinbaser har en struktur der består af ring med seks atomer og en ring med fem atomer. Eks. se Guanine (https://en.wikipedia.org/wiki/Guanine)
#Pyrmidbaser har kun en ring med seks atomer. Eks. se Thymine (https://en.wikipedia.org/wiki/Thymine)

#Chargaffs regl 
#Basepar dannes altid kun som Adenine og Thymine (A-T), Cytosine og Guanine (C-G)
#Adenine vil altid danne et basepar med Thymine.

#Chargaff opdagede at menneskets opdeling for basepar har en ratio svarende til;
#30.9 percent Adenine
#29.4 percent Thymine
#19.8 percent Cytosine
#19.9 percent Guanine

#Cytosine og Guanine har triple bindinger.
#Adenine og Thymine har double bindinger


#DNA polymerase

#Cytosine og Guanine har triple bindinger.
#Adenine og Thymine har double bindinger
def linkStrengtFunction(string):
    result = ''
    for x in string:
        if x == 'C' or x == "G":
            result = result  + 'S' 
        if x == 'A' or x == "T":
            result = result  + 'W' 
    return (result)

def Fowardprimer(string):
    result =  "5' " 
    for x in string:
        if x == 'A':
            result = result +  'T' 
        if x == 'G':
            result = result +  'C' 
        if x == 'C':
            result = result +  'G' 
        if x == 'T':
            result = result +  'A' 
    result = result + " 3'" 
    return (result)

def Reverseprimer(string):
    result = ""
    for x in string:
        if x == 'A':
            result = result + 'T'
        if x == 'G':
            result = result + 'C'
        if x == 'C':
            result = result + 'G'
        if x == 'T':
            result = result + 'A'
    result =  result + " '5"
    reversedResult = result[::-1]
    reversedResult = reversedResult + " 3'"  
    print(reversedResult)
    return (reversedResult)

def main(string):
    #linkStrengtFunction(string)
    #print("Foward primer " + Fowardprimer(string))
    #print("Reverse primer " + Reverseprimer(string))
    #print("linkStrengtFunction " + linkStrengtFunction(string))
    pass
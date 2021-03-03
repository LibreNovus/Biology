import lzma
import zlib
from corona import coronagenome


def Compressgenome(genome):
    for x in " \n0123456789":
        genome = genome.replace(x, '')
    lzc = lzma.compress(genome.encode("utf-8"))
    return(len(lzc)) #Kolmogorov Complexity in bytes

def Basepairs(genome):
    for x in " \n0123456789":
        genome = genome.replace(x, '')
    return(len(genome)) #Number of basepairs

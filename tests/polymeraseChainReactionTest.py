import sys
sys.path.insert(0,'..')

from polymeraseChainReaction import Fowardprimer, Reverseprimer
from color import colors

from corona import coronagenome
from genome import Compressgenome, Basepairs
for x in " \n0123456789":
    coronagenome = coronagenome.replace(x, '')

Fowardprimer("AAGCTGGTTTTGACGAC")

def function_tests():
    print("===Polymerase Chain reaction===")
    if Fowardprimer("AAGCTGGTTTTGACGAC") == "5' TTCGACCAAAACTGCTG 3'" and Fowardprimer("CGTTACGTGATGCTAAGCTA") == "5' GCAATGCACTACGATTCGAT 3'":
        print("1. Fowardprimer" + colors.BLUE + " Passed" + colors.ENDC)
    else:
        print("1. Fowardprimer" + colors.RED + " Failed" + colors.ENDC)

    if Reverseprimer("AAGCTGGTTTTGACGAC") == "5' GTCGTCAAAACCAGCTT 3'" and Reverseprimer("CGATTCGATCTCATGACATC") == "5' GATGTCATGAGATCGAATCG 3'":
        print("2. Reverseprimer" + colors.BLUE + " Passed" + colors.ENDC)
    else:
        print("2. Reverseprimer" + colors.RED + " Failed" + colors.ENDC)

    print("===Genomes===")
    if Compressgenome(coronagenome) == 8408:
        print("1. compressgenome" + colors.BLUE + " Passed" + colors.ENDC)
    else:
        print("1. compressgenome" + colors.RED + " Failed" + colors.ENDC)

    if Basepairs(coronagenome) == 29903:
        print("2. Basepairs" + colors.BLUE + " Passed" + colors.ENDC)
    else:
        print("2. Basepairs" + colors.RED + " Failed" + colors.ENDC)

if __name__ == "__main__":
    function_tests()

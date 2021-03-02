import sys
sys.path.insert(0,'..')

from polymeraseChainReaction import Fowardprimer, Reverseprimer

Fowardprimer("AAGCTGGTTTTGACGAC")

def test_sum():
    print("===Function tests===")
    if Fowardprimer("AAGCTGGTTTTGACGAC") == "5' TTCGACCAAAACTGCTG 3'" and Fowardprimer("CGTTACGTGATGCTAAGCTA") == "5' GCAATGCACTACGATTCGAT 3'":
        print("1. Fowardprimer Pass")
    else:
        print("1. Fowardprimer failed")

    if Reverseprimer("AAGCTGGTTTTGACGAC") == "5' GTCGTCAAAACCAGCTT 3'" and Reverseprimer("CGATTCGATCTCATGACATC") == "5' GATGTCATGAGATCGAATCG 3'":
        print("2. Reverseprimer Pass")
    else:
        print("2. Reverseprimer failed")

if __name__ == "__main__":
    test_sum()

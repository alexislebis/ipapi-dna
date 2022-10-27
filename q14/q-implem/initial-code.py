from typing import List

def reconstruct(arnSeq:str, prots:List[str]) -> str :
    for prot in prots:
        arnSeq += mostProbableNucl(prot) #What about overlaping prot and triplets?
    
    #TODO:arnSeq no guarantee to have either U{A,G,C}A!
    
    return arnSeq
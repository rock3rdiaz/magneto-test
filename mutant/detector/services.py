from typing import List
import re

keys = ['A', 'T', 'G', 'C']
pattern = 'C{4}|T{4}|G{4}|A{4}'

def horizontally(dna: List[str]) -> bool:
    for e in dna:
        print(f'searching in {e}')
        r = re.match(pattern, e) 
        if r:
            print(f'founded {e}')
            return True
    return False
            
def vertically(dna: List[str]) -> bool:
    new_dna = []
    reorder = list(zip(*dna))
    for r in reorder:
        new_dna.append(''.join(r))
    horizontally(new_dna)

def diagonal(dna:List[str]) -> bool:
    new_dna = []
    for c in range(len(dna[0])):
        el = ''
        for r in range(len(dna)):
            el = dna[c][(len(dna) - 1) - r]
            print(el)
            
def mutant_detector(dna: List[str]) -> bool:
    """
    Funcion que detecta si la secuencia de ADN pertenece o no a 
    un mutante.
    @param dna: Lista de secuencias de ADN
    @return bool: True si es mutante, False en caso contrario 
    """
    return horizontally(dna)
                
                
        
    
          
#orizontally(dna)
#vertically(dna)
#diagonal(dna)
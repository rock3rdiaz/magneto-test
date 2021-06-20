from typing import List, Tuple
import re
from .models import Stats


pattern = 'C{4}|T{4}|G{4}|A{4}'


class MutatorService:
    """
    Mutator service
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if MutatorService.__instance is None:
            return object.__new__(cls)
        raise NotImplementedError('please use get_instance method!')

    def __init__(self):
        if MutatorService.__instance is None:
            MutatorService.__instance = self

    @staticmethod
    def get_instance():
        if MutatorService.__instance is None:
            MutatorService()
        return MutatorService.__instance

    @staticmethod
    def horizontally(dna: List[str]) -> Tuple[bool, str]:
        for e in dna:
            print(f'searching in {e}')
            r = re.match(pattern, e) 
            if r:
                print(f'founded {e}')
                return True, e
        return False, None
            
    def vertically(cls, dna: List[str]) -> Tuple[bool, str]:
        new_dna = []
        reorder = list(zip(*dna))
        for r in reorder:
            new_dna.append(''.join(r))
        return MutatorService.horizontally(new_dna)

    def diagonal(cls, dna:List[str]) -> Tuple[bool, str]:
        """
        solo se busca en entradas con 4 o mas caracteres
        """
        new_dna = []
        for c in range(len(dna)):
            for r in range(len(dna[0])):
                el = ''
                for index in range(len(dna)):
                    if (c + index) < len(dna) and (r + index) < len(dna):
                        el = el + dna[c + index][r + index]
            new_dna.append(el)
        cls.horizontally([i for i in new_dna if len(i) >= 4])
    
    @classmethod        
    def detect(cls, dna: List[str]) -> bool:
        """
        Funcion que detecta si la secuencia de ADN pertenece o no a 
        un mutante.
        @param dna: Lista de secuencias de ADN
        @return bool: True si es mutante, False en caso contrario 
        """
        res, dna = cls.horizontally(dna)
        if res:
            Stats.objects.create(dna=dna)
            return res
        else:
            res, dna = cls.vertically(dna=dna)
            if res:
                Stats.objects.create(dna=dna)
                return res
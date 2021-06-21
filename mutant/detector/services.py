from typing import List, Tuple
import re

from django.db.models import F
from .models import Mutants, Stats


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
            
    @staticmethod
    def vertically(dna: List[str]) -> Tuple[bool, str]:        
        new_dna = []
        reorder = list(zip(*dna))
        for r in reorder:
            new_dna.append(''.join(r))
        return MutatorService.horizontally(new_dna)

    @staticmethod
    def diagonal(dna:List[str]) -> Tuple[bool, str]:
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
        return MutatorService.horizontally([i for i in new_dna if len(i) >= 4])
    
    @staticmethod
    def __update_stats(dna: List[str], res: bool) -> None:
        s = Stats.objects.first()
        if s:
            if res:
                s.count_human_dna = s.count_human_dna + (len(dna) - 1)
                s.count_mutant_dna = s.count_mutant_dna + 1
                s.ratio = s.count_mutant_dna / s.count_human_dna
                s.save()
            else:
                s.count_human_dna = s.count_human_dna + (len(dna))
                s.ratio = s.count_mutant_dna / s.count_human_dna
                s.save()
        else:
            Stats.objects.create(count_mutant_dna=1,
                                count_human_dna=(len(dna) - 1),
                                ratio = 1 / (len(dna) - 1))
                
    @staticmethod        
    def detect(dna: List[str]) -> bool:
        """
        Funcion que detecta si la secuencia de ADN pertenece o no a 
        un mutante.
        @param dna: Lista de secuencias de ADN
        @return bool: True si es mutante, False en caso contrario 
        """
        res, dna_founded = MutatorService.horizontally(dna)        
        if not res:
            res, dna_founded = MutatorService.vertically(dna) 
            if not res:
                res, dna_founded = MutatorService.diagonal(dna)
                if not res:
                    MutatorService.__update_stats(dna, res)
                    return False
                else:
                    MutatorService.__update_stats(dna, res)
                    return True
            else:
                MutatorService.__update_stats(dna, res)
                return True
        else:
            MutatorService.__update_stats(dna, res)
            return True
        return False
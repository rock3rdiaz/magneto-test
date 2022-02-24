import logging
import math
import re
from typing import List, Tuple

from .models import Mutants, Stats

logger = logging.getLogger(__name__)

pattern = 'C{4}|T{4}|G{4}|A{4}'
compile_pattern = re.compile(pattern)
sequence_len = 4


def horizontally(dna: List[str]) -> Tuple[bool, list]:
    dna_founded = re.findall(compile_pattern, ''.join(dna))
    print(f'------------- dna founded => {dna_founded}')
    if len(dna_founded) >= 1:
        return True, dna_founded
    return False, None


def vertically(dna: List[str]) -> Tuple[bool, str]:
    new_dna = [''.join(i) for i in zip(*dna)]
    return horizontally(new_dna)


def diagonal(dna_list: List[str]) -> Tuple[bool, str]:
    """
    Solo se busca en entradas con 4 o mas caracteres en diagonal tanto
    de derecha a izquierda como de izquierda a derecha
    """
    # items = []
    # half_size = len(dna_list) // 2
    # for index, row in enumerate(dna_list):
    #     if index < half_size:
    #         items.append(row[:(half_size + index)])
    #     elif index == half_size and len(dna_list) % 2 != 0:
    #         items.append(row[(index - half_size + 1):len(row) - 1])
    #     else:
    #         items.append(row[(index - half_size + 1):])

    items = []
    data = ''.join(dna_list)
    size = len(data)
    rank = int(math.sqrt(size))
    interval = rank + 1
    # positions inside sequence to get diagonal string
    valid_positions = [(index, rank * index) for index in range(0, size) if index <= (rank - sequence_len)]
    print(f'------------------ valid_positions => {valid_positions}')
    for pivot1, pivot2 in valid_positions:
        if pivot1 == pivot2:
            items.append(data[pivot1::interval])
        else:
            items.append(data[pivot1:size - (pivot1 * rank):interval])
            items.append(data[pivot2::interval])
    print(f'--------------------- items => {items}')
    return horizontally(items)


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
        if res:
            Stats.objects.create(count_mutant_dna=1,
                                 count_human_dna=(len(dna) - 1),
                                 ratio=1 / (len(dna) - 1))
        else:
            Stats.objects.create(count_mutant_dna=0,
                                 count_human_dna=(len(dna) - 1),
                                 ratio=0 / (len(dna) - 1))


def detect(dna: List[str]) -> bool:
    """
    Funcion que detecta si la secuencia de ADN pertenece o no a
    un mutante.
    @param dna: Lista de secuencias de ADN
    @return bool: True si es mutante, False en caso contrario
    """
    dna_list = ''.join(dna)
    res, dna_founded = horizontally(dna_list)
    if res:
        Mutants.objects.create(dna=dna_founded)
        __update_stats(dna, res)
        return True
    else:
        res, dna_founded = vertically(dna)
        if res:
            Mutants.objects.create(dna=dna_founded)
            __update_stats(dna, res)
            return True
        else:
            res, dna_founded = diagonal(dna)
            if res:
                Mutants.objects.create(dna=dna_founded)
                __update_stats(dna, res)
                return True
    __update_stats(dna, res)
    return False

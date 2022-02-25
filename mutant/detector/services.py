import logging
import math
import re
from typing import List, Tuple

from .models import Stats, DNA

logger = logging.getLogger(__name__)

pattern = 'C{4}|T{4}|G{4}|A{4}'
compile_pattern = re.compile(pattern)
sequence_len = 4


def horizontally(dna: List[str]) -> List[str]:
    dna_founded = re.findall(compile_pattern, ''.join(dna))
    print(f'------------- dna founded => {dna_founded}')
    return dna_founded


def vertically(dna: List[str]) -> List[str]:
    new_dna = [''.join(i) for i in zip(*dna)]
    return horizontally(new_dna)


def left_to_right_diagonal(dna_list: List[str]) -> List[str]:
    """
    Left to right Diagonal search
    """
    items = []
    data = ''.join(dna_list)
    size = len(data)
    rank = int(math.sqrt(size))
    interval = rank + 1
    # positions inside sequence to get diagonal string
    valid_positions = [(index, rank * index) for index in range(0, size) if index <= (rank - sequence_len)]
    for pivot1, pivot2 in valid_positions:
        if pivot1 == pivot2:
            items.append(data[pivot1::interval])
        else:
            items.append(data[pivot1:size - (pivot1 * rank):interval])
            items.append(data[pivot2::interval])
    return horizontally(items)


def right_to_left_diagonal(dna_list: List[str]) -> Tuple[bool, str]:
    """
    Right to lef search
    """
    items = []
    for row in dna_list:
        items.append(row[::-1])
    return left_to_right_diagonal(items)


def __update_stats_by_type(s: Stats, dna_type: int) -> None:
    if dna_type:
        s.count_mutant_dna = s.count_mutant_dna + 1
        s.ratio = round(s.count_mutant_dna / s.count_human_dna, 2)
        s.save(update_fields=['count_mutant_dna', 'ratio'])
    else:
        s.count_human_dna = s.count_human_dna + 1
        s.ratio = round(s.count_mutant_dna / s.count_human_dna, 2)
        s.save(update_fields=['count_human_dna', 'ratio'])


def __update_stats(dna: List[str], dna_type: int) -> None:
    """
    :param dna_sequence => DNA sequence received
    :param dna_type => {0: human, 1: mutant}
    """
    dna_sequence = ''.join(dna)
    s = Stats.objects.first()
    dna, created = DNA.objects.get_or_create(dna=dna_sequence, type=dna_type)
    if created:
        __update_stats_by_type(s, dna_type)


def detect(dna: List[str]) -> bool:
    """
    Detection start point
    @param dna: ADN sequences
    @return bool: ADN type, True to mutants, False otherwise
    """
    dna_founded = horizontally(dna)
    if len(dna_founded) > 1:
        __update_stats(dna, 1)
        return True
    else:
        dna_founded.extend(vertically(dna))
        if len(dna_founded) > 1:
            __update_stats(dna, 1)
            return True
        else:
            dna_founded.extend(left_to_right_diagonal(dna))
            if len(dna_founded) > 1:
                __update_stats(dna, 1)
                return True
            else:
                dna_founded.extend(right_to_left_diagonal(dna))
                if len(dna_founded) > 1:
                    __update_stats(dna, 1)
                    return True
                __update_stats(dna, 0)
                return False

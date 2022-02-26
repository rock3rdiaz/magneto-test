import pytest

from detector.models import Stats
from detector.services import detect, horizontally, vertically, left_to_right_diagonal, right_to_left_diagonal


def test_horizontally():
    mutant_dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TTTTCG"]
    human_dna = ["ATGCGA", "CAGTGC", "TTATTAT", "AGACGG", "GCGTCA", "TCACTG"]
    sequence = horizontally(mutant_dna)
    assert len(sequence) > 1
    sequence = horizontally(human_dna)
    assert len(sequence) == 0


def test_vertically():
    mutant_dna = ["ATGCGA", "ATATGC", "ATATGT", "ATAAGG", "ATCCTA", "TTTTCG"]
    human_dna = ["ATGCGA", "CAGTGC", "TTATTAT", "AGACGG", "GCGTCA", "TCACTG"]
    sequence = vertically(mutant_dna)
    assert len(sequence) > 1
    sequence = vertically(human_dna)
    assert len(sequence) == 0


def test_left_to_right_diagonal():
    human_dna = ["ATGCGA", "ATATGC", "ATATGT", "ATAAGG", "ATCCTA", "TTTTCG"]
    mutant_dna = ["AAAAAAAATC", "GATCGCTTAG", "AAAGCCTGAC", "GGTAAGTCTG", "GTTCAGTCAA", "GTTACATACG", "GCTACAACGT",
                  "GCTACGGAGT", "TCTACAACAT", "GCTACAATTA"]
    sequence = left_to_right_diagonal(mutant_dna)
    assert len(sequence) > 1
    sequence = left_to_right_diagonal(human_dna)
    assert len(sequence) == 0


def test_right_to_left_diagonal():
    human_dna = ["ATGCGA", "ATATGC", "ATATGT", "ATAAGG", "ATCCTA", "TTTTCG"]
    mutant_dna = ["ATGCGT", "CAGTTC", "TTATCT", "AGTCGG", "CCCCTA", "TCACTG"]
    sequence = right_to_left_diagonal(mutant_dna)
    assert len(sequence) > 1
    sequence = right_to_left_diagonal(human_dna)
    assert len(sequence) == 0


@pytest.mark.django_db
def test_detect_horizontally_vertically():
    mutant_dna = ["ATGCGT", "CAGTGC", "TTATGT", "AGTAGG", "CCCCTA", "TCACTG"]
    human_dna = ["ATGCGA", "CAGTGC", "TTCTTAT", "AGACGG", "GCGTCA", "TCACTG"]
    is_mutant = detect(mutant_dna)
    assert is_mutant is True
    is_mutant = detect(human_dna)
    assert is_mutant is False


@pytest.mark.django_db
def test_detect_diagonals():
    mutant_dna = ["ATGCGT", "CAGTTC", "TTATGT", "AGTAGG", "CCCATA", "TCACTG"]
    human_dna = ["ATGCGA", "CAGTGC", "TTCTTAT", "AGACGG", "GCGTCA", "TCACTG"]
    is_mutant = detect(mutant_dna)
    assert is_mutant is True
    is_mutant = detect(human_dna)
    assert is_mutant is False


@pytest.mark.django_db
def test_stats():
    mutant_dna = ["ATGCGT", "CAGTGC", "TTATGT", "AGTAGG", "CCCCTA", "TCACTG"]
    human_dna = ["ATGCGA", "CAGTGC", "TTCTTAT", "AGACGG", "GCGTCA", "TCACTG"]
    detect(mutant_dna)
    detect(human_dna)
    s = Stats.objects.first()
    assert s.count_mutant_dna == 1
    assert s.count_human_dna == 1
    assert 1.0 == s.ratio

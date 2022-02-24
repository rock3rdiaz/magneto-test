from detector.services import diagonal


#
# def test_horizontally():
#     mutant_dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
#     human_dna = ["ATGCGA", "CAGTGC", "TTATTAT", "AGACGG", "GCGTCA", "TCACTG"]
#     result, sequence = horizontally(mutant_dna)
#     assert result == True
#     result, sequence = horizontally(human_dna)
#     assert result == False
#
#
# def test_vertically():
#     mutant_dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
#     human_dna = ["ATGCGA", "CAGTGC", "TTATTAT", "AGACGG", "GCGTCA", "TCACTG"]
#     result, sequence = vertically(mutant_dna)
#     assert result == True
#     result, sequence = horizontally(human_dna)
#     assert result == False


def test_diagonalx6():
    #mutant_dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    mutant_dna = ["ATTCTAA", "GATGTAT", "TCACGAC", "CTAATTG", "ACGTTCA", "CTCCAGT", "CTTTGCC"]
    result, sequence = diagonal(mutant_dna)
    assert result, True


# def test_diagonalx5():
#     mutant_dna = ["ACTAT", "AATGG", "TAATC", "TCGAC", "TGATG"]
#     result, sequence = diagonal(mutant_dna)
#     assert result, True

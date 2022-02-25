from django.db import models


class Stats(models.Model):
    """
    Stats model
    """
    count_mutant_dna = models.PositiveIntegerField(null=True, default=0)
    count_human_dna = models.PositiveIntegerField(null=True, default=0)
    ratio = models.FloatField(null=True, default=0.0)

    def __str__(self) -> str:
        return f'[count_mutant_dna={self.count_mutant_dna}, count_human_dna={self.count_human_dna},' \
               f'ratio={self.ratio}]'

    class Meta:
        ordering = ('-ratio',)


class DNA(models.Model):
    """
    ADN sequences
    type = {0: human, 1: mutant}
    """
    dna = models.CharField(max_length=200, db_index=True, unique=True)
    type = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'[dna={self.dna}, type={self.type}'

    class Meta:
        ordering = ('-created_at',)

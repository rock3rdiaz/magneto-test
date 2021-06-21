from django.db import models

class Stats(models.Model):
    """
    Modelo para estadisticas de deteccion
    """
    count_mutant_dna = models.PositiveIntegerField(null=True)
    count_human_dna = models.PositiveIntegerField(null=True)
    ratio = models.FloatField(null=True)
    
    def __str__(self) -> str:
        return self.ratio
    
    class Meta:
        ordering = ('-ratio',)


class Mutants(models.Model):
    """
    Modelo con las cadenas de mutantes encontradas
    """
    dna = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.adn
    
    class Meta:
        ordering = ('-created_at',)

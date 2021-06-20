from django.db import models

class Stats(models.Model):
    """
    Modelo para estadisticas de deteccion
    """
    dna = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.adn
    
    class Meta:
        ordering = ('-created_at',)

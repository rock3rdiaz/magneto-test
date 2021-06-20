from rest_framework import serializers


class StatsSerializer(serializers.Serializer):
    """
    Stats serializer
    """
    count_mutant_dna = serializers.IntegerField()
    count_human_dna = serializers.IntegerField()
    ratio = serializers.FloatField()

    def get_count_mutant_dna(self, instance):
        pass

    def get_count_human_dna(self, instance):
        pass
    
    def get_ratio(self, instance):
        pass
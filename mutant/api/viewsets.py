import logging
import re
import traceback
from functools import wraps

from rest_framework import viewsets, status
from rest_framework.response import Response

from api.serializers import StatsSerializer
from detector.models import Stats
from detector.services import detect

logger = logging.getLogger(__name__)

pattern = '[^ACTG]'
compile_pattern = re.compile(pattern)


def dna_validator(func):
    """
    Input validator
    :param func:
    :return:
    """

    @wraps(func)
    def inner(*args, **kwargs):
        dna_sequence = ''.join(args[1].data['dna'])
        invalid = re.findall(compile_pattern, dna_sequence)
        if invalid:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={
                'message': f'Invalid dna char: {invalid}'
            })
        return func(*args, **kwargs)

    return inner


class MutantViewSet(viewsets.ViewSet):
    """
    Mutant resource
    """

    @dna_validator
    def create(self, request):
        """
        Add a DNA sequence
        Valid chars => [A,T, C, G]
        Input form "dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
        """
        try:
            if type(request.data['dna']) is not list:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={
                    'message': 'ws needs a list!'
                })
            res = detect(request.data['dna'])
            if res:
                logger.error('----------- i found a mutant!')
                return Response()
            else:
                logger.error('----------- i don\'t found a mutant')
                return Response(status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            logger.error(f'error with input values => {traceback.print_exc()}')
            return Response(status=status.HTTP_400_BAD_REQUEST)


class StatsViewSet(viewsets.ViewSet):
    """
    Stats resource
    """

    def list(self, request):
        """
        Return list of stats
        """
        try:
            stats = Stats.objects.first()
            serializer = StatsSerializer(stats)
            return Response(serializer.data)
        except KeyError:
            logger.error(f'error with input values => {traceback.print_exc()}')
            return Response(status=status.HTTP_400_BAD_REQUEST)

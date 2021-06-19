import re
import logging
import traceback
from rest_framework import viewsets, status
from rest_framework.response import Response
from detector.services import mutant_detector


logger = logging.getLogger(__name__)


class MutantViewSet(viewsets.ViewSet):
    """
    Resource asociado a la busqueda de mutantes
    """
    def create(self, request):
        """
        Verirfica si la cadena DNA enviada corresponde a un mutante o humano.
        Input de la forma "dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
        """
        try:
            if type(request.data['dna']) is not list:
                logger.error('----------- ws needs a list!')
                return Response(status=status.HTTP_400_BAD_REQUEST)
            res = mutant_detector(request.data['dna'])
            if res:
                logger.error('----------- i found a mutant!')
                return Response()
            else:
                logger.error('----------- i don\'t found a mutant')
                return Response(status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            logger.error(f'error with input values => {traceback.print_exc()}')
            return Response(status=status.HTTP_400_BAD_REQUEST)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MutantViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'mutant', MutantViewSet, basename='mutant')

urlpatterns = [
    path('', include(router.urls))
]
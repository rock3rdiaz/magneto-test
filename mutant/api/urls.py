from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.viewsets import MutantViewSet, StatsViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'mutant', MutantViewSet, basename='mutant')
router.register(r'stats', StatsViewSet, basename='stats')

urlpatterns = [
    path('', include(router.urls))
]
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets

from .serializers import DishSerializer
from ..models import Dish


class DishesViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows Dishes to be viewed or edited.'''
    authentication_classes = []
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    http_method_names = ['get']


    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(DishesViewSet, self).dispatch(*args, **kwargs)

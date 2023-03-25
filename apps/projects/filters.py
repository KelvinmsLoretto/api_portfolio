import django_filters
from .models import Project, Tecnology
 
class ProjectFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr='exact')
    name = django_filters.CharFilter(lookup_expr='icontains')
    tecnologies = django_filters.CharFilter(field_name='Tecnology__name')
    data = django_filters.DateFromToRangeFilter()
    last_update = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Project
        fields = ['name', 'tecnologies', 'data', 'last_update']

class TecnologyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    use = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Tecnology
        fields = ['name', 'use']



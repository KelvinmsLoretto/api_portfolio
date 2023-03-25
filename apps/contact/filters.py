import django_filters
from .models import Contact
 
class ContactFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr='exact')
    ddd = django_filters.NumberFilter(lookup_expr='exact')
    subject = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Contact
        fields = ['id', 'ddd', 'subject']
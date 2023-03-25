from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .serializers import ContactSerializer
from .models import Contact
from .filters import ContactFilter


# Create your views here.
class ContactAPIView(APIView):
    """
    API view to list logins.
    """
    serializer_class = ContactSerializer
    model_class = Contact
    filter_class = ContactFilter
    
    def get(self, request):
        queryset = self.model_class.objects.all()
        filter_params = request.query_params.dict()
        filtered_queryset = self.filter_class(filter_params, queryset=queryset).qs

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK) 
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
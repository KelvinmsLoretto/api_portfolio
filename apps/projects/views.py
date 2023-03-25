from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TecnologySerializer, ProjectSerializer
from .models import Project, Tecnology
from .filters import ProjectFilter, TecnologyFilter

# Create your views here.
class ProjectListAPIView(APIView):
    """
    API view for list projects.
    """
    serializer_class = ProjectSerializer
    
    def get(self, request):
        queryset = Project.objects.all()
        filter_params = request.query_params.dict()
        filtered_queryset = ProjectFilter(filter_params, queryset=queryset).qs

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data, HTTP_200_OK) 
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class TecnologyListAPIView(APIView):
    """
    API view for list Tecnology.
    """
    serializer_class = TecnologySerializer
    
    def get(self, request):
        queryset = Tecnology.objects.all()
        filter_params = request.query_params.dict()
        filtered_queryset = TecnologyFilter(filter_params, queryset=queryset).qs

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data, HTTP_200_OK) 
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


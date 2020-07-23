from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics

from .serializers import MusicSerializer
from .models import Music


class ToDoListAPIView(APIView):

    def get(self, request):
        task = Music.objects.random()
        serializer = MusicSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MusicListView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['name']
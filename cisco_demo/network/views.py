from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from network.models import *
from network.serializers import *

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class RouterListView(APIView):
    """
    List all Router, or create a new Routers.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        queryset = router_details.objects.all()
        serializer = routerSerializer(queryset, many=True)
    
        return Response(serializer.data,status=200)

    def post(self, request, format=None):
        serializer = routerSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        router_details.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RouterDetailView(APIView):
    """
    Retrieve, update or delete a router instance.
    """
    def get_object(self, pk):
        try:
            return router_details.objects.get(pk=pk)
        except router_details.DoesNotExist:
            return Response("Product Not Found", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        router = self.get_object(pk)
        serializer = routerSerializer(router)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        router = self.get_object(pk)
        serializer = routerSerializer(router, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        router = self.get_object(pk)
        router.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

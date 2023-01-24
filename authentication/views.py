
# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import (
  RegistrationSerializer,
  ProfileGetSerializer,
  ProfileSerializer
)
class RegistrationAPIView(APIView):
    
    permission_classes = (AllowAny, )
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetProfile(APIView):
    permission_classes = (IsAuthenticated, )


    def get(self, request):
        w = User.objects.get(pk=request.user.pk)
        return Response({f'{request.user.username}': ProfileGetSerializer(w).data})
    

    def patch(self, request):
    
        try:
            instance = User.objects.get(pk=request.user.pk)
        except:
            return Response({"error": "Object does not exists"})
 
        serializer = ProfileSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
 
        return Response({"patch": serializer.data})
  

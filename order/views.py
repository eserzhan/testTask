from cProfile import Profile
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import OrderSerializer
from .models import Order
from django.db.models import Q
# Create your views here.


class OrderAPIView(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            q = Order.objects.filter(Q(profile_id=request.user.pk) | Q(profile_id= None))
        else:
            q = Order.objects.filter(profile_id=request.user.pk)
        return Response({'Order': OrderSerializer(q,many=True).data})

    def post(self, request):
        request.data["profile"] = request.user.pk 
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    
        serializer.save()
 
        return Response({'post': serializer.data})
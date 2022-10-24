from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from api.models import Entry
from api.serializers import UserSerializer,EntrySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions,authentication

# Create your views here.

class SignUpView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class EntryView(ModelViewSet):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication]

    def create(self, request, *args, **kwargs):
        serializer=EntrySerializer(data=request.data,context={"user":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
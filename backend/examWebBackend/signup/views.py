from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view


@api_view(['POST'])
def SignUpView(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        # Check if user already exists
        username = serializer.validated_data['username']
        if User.objects.filter(username=username).exists():
            return Response({'error': 'User with this username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Optionally check for existing email
        email = serializer.validated_data.get('email')
        if email and User.objects.filter(email=email).exists():
            return Response({'error': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Use serializer's save method
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
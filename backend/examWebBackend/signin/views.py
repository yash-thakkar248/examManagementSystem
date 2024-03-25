from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignInSerializer
from rest_framework.decorators import api_view


@api_view(['POST'])
def sign_in(request):
    if request.method == 'POST':
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

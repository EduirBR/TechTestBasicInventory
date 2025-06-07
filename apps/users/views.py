from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer

class RegisterView(APIView):
    """
    View to handle user registration.
    """
    
    def post(self, request: Request) -> Response:
        """
        Handle POST request for user registration.
        Returns both access and refresh tokens upon successful registration.
        """
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Generate tokens for the new user
        refresh = RefreshToken.for_user(user)
        
        return Response({
            "message": "User registered successfully!",
            "tokens": {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }
        })

class ProfileView(APIView):
    """
    View to handle user profile retrieval.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request) -> Response:
        """
        Handle GET request to retrieve user profile.
        Returns the user's email and active status.
        """
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
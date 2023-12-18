import uuid

from django.contrib.auth import login
from rest_framework import generics, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.models import User
from config.settings import email_settings
from django.core.mail import send_mail
from apps.user.serilizers import RegisterSerializer, TokenObtainPairSerializer, LoginSerializer, \
    ResetPasswordSerializer, ConfirmPasswordSerializer

from apps.user.tasks import send_email_task


class RegisterAPIView(generics.GenericAPIView):
    """Register user"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user).key
        return Response({"token": token}, status.HTTP_201_CREATED)


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class LoginApiView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(
            data=self.request.data,
            context={'request': self.request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(data={"You are log in!"}, status=status.HTTP_202_ACCEPTED)


class ResetPasswordApi(APIView):

    def post(self, request, *args, **kwargs):
        print("SER    :")
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        user = User.objects.filter(email__exact=email).filter()

        if user:
            api_version = request.version

            reset_url = (
                    request.build_absolute_uri(
                        reverse(f"{api_version}:users:confirm-password")
                    )
                    + f"?uid={user.uid}"
            )

            send_email_task.delay(
                "Confirmation email for reset password",
                f"click on link {reset_url}",
                [user.email]
            )

            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ConfirmPasswordApi(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ConfirmPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_password = serializer.validated_data["new_password"]
        confirm_password = serializer.validated_data["confirm_password"]
        uid = serializer.validated_data["uid"]

        if new_password != confirm_password:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(uid__exact=uid).first()
        if user:
            user.set_password(new_password)
            user.uid = uuid.uuid4()
            user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

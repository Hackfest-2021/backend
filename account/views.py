import json
from drf_yasg.openapi import IN_PATH, Parameter, Schema
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status, generics

from account.serializers import RegistrationSerializer, AccountSerializer, ChangePasswordSerializer, \
    AccountUpdateSerializer, RolesSerializer
from rest_framework.authtoken.models import Token
from account.models import Account, Roles
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import os


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        print(request.data)
        print('ENV', os.environ.get('ENV'))
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)



        return Response({
            'token': token.key,
            'is_admin': user.is_admin,
            'id': user.id,
            'name': user.username,
        })


@api_view(['POST', ])
# @swagger_auto_schema(query_serializer=RegistrationSerializer)
def registration_view(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            cur_status = status.HTTP_201_CREATED
        else:
            data = serializer.errors
            cur_status = status.HTTP_400_BAD_REQUEST

        return Response(data, status=cur_status)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = Account.objects.all()
    lookup_field = 'email'
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class ListCreateRolesView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RolesSerializer

class RetrieveUserView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountSerializer


class UpdateUserView(generics.UpdateAPIView):
    queryset = Account.objects.all()
    lookup_field = 'email'
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountUpdateSerializer




@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def approve_pending_user_view(request):
    if not request.user.is_admin:
        return Response({'You are not allowed to call this service'}, status=status.HTTP_403_FORBIDDEN)
    print(request.data)
    if request.method == 'PUT':
        if 'email' not in request.data:
            return Response({'Unable to approve: email missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.data['email']
        accounts = Account.objects.get(email=request.data['email'])

        accounts.is_active = True
        accounts.save()
        return Response({'User approved successfully'}, status=status.HTTP_200_OK)


@swagger_auto_schema(operation_description='Show all devices to user which are assigned to his organization'
                                           '....Pass the user email in postman parameters',
                     method='get',
                     manual_parameters=[Parameter('email', IN_PATH, type='str', required=True)],
                     responses={'200': 'list of devices.'})


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def approvedUser_detail_view(request):
    if not request.user.is_admin:
        return Response({"You are not allowed to perform this operation"}, status=status.HTTP_403_FORBIDDEN)

    try:
        accounts = Account.objects.all().filter(is_admin=0, is_active=1)
    except Account.DoesNotExist:
        return Response({'No user found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)



@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def nonapprovedUser_detail_view(request):
    if not request.user.is_admin:
        return Response({"You are not allowed to perform this operation"}, status=status.HTTP_403_FORBIDDEN)

    try:
        accounts = Account.objects.all().filter(is_admin=0, is_active=0)
    except Account.DoesNotExist:
        return Response({'No user found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)




@api_view(['DELETE', ])
@permission_classes((IsAuthenticated,))
def user_delete_view(request, slug):
    if not request.user.is_admin:
        return Response({"You are not allowed to perform this operation"})

    try:
        account = Account.objects.get(id=slug)
    except Account.DoesNotExist:
        return Response({'Unable to find Device with Serial Number'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        data = {}
        operation = account.delete()
        if operation:
            data["success"] = "delete successful"
            cur_status = status.HTTP_200_OK
        else:
            data["success"] = "delete failed"
            cur_status = status.HTTP_400_BAD_REQUEST

        return Response(data=data, status=cur_status)




@api_view(['GET', ])
def isAdminView(request):
    return Response({"isAdmin": request.user.is_superuser})

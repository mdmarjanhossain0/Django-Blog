from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from account.api.serializers import RegistrationSerializer, AccountPropertiesSerializer


@api_view(['POST',])
def registration_view(request):

	if request.method == "POST":
		serializer = RegistrationSerializer(data=request.data)
		data = {}

		if serializer.is_valid():
			account = serializer.save()
			data['response'] = "Succesfully create a new account"
			data['email'] = account.email
			data['username'] = account.username
			token = Token.objects.get(user=account).key
			data['token'] = token

		else:
			data = serializer.errors

		return Response(data=data)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def account_properties_view(request):


	try:
		account = request.user
	except Account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)


	if request.method == 'GET':
		serializer =  AccountPropertiesSerializer(account)
		return Response(serializer.data)


@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def account_update_view(request):


	try:
		account = request.user
	except Account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)


	if request.method == 'PUT':
		serializer =  AccountPropertiesSerializer(account, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data['response'] = "Account Update Succesfully"
			return Response(data=data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
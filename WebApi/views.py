from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from django.shortcuts import get_object_or_404

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response(status=status.HTTP_404_NOT_FOUND)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({'token': token.key, 'user': serializer.data})

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        user.set_password(request.data['password'])
        user.save()

        token = Token.objects.create(user=user)

        return Response({'token': token.key, 'user': serializer.data})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def test_request(request):
    return Response({})

@api_view(['GET'])
def demo_course(request):
    cards = [
                {
                    'Question': 'https://visie-eo.cdn.eo.nl/w_2400/s3-visie-eo/77069d90-e7e1-47a9-b5e0-41d70e45a956.jpg',
                    'Answer':'Tree',
                    'Hint':'Boom',
                    'CardType': 'Image'
                },
                {
                    'Question': 'https://www.1800flowers.com/_next/image?url=https%3A%2F%2Fwww.1800flowers.com%2Fblog%2Fwp-content%2Fuploads%2F2017%2F03%2Fsingle-red-rose.jpg&w=750&q=75',
                    'Answer': 'Rose',
                    'Hint': 'Roos',
                    'CardType': 'Image'
                },
                {
                    'Question': 'https://www.thoughtco.com/thmb/XRS8J7vnB3Vx6KRaElWO5fzzg1Y=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/blue-runners--947498612-5c634cd3c9e77c0001566e32.jpg',
                    'Answer': 'Fish',
                    'Hint': 'Vis',
                    'CardType': 'Image'
                },
                {
                    'Question': 'https://www.thoughtco.com/thmb/pNr1IIDYAuVP8IPDW72NI3lWPzg=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/close-up-of-flame-536940503-59b2b3de845b3400107a7f27-5b967c9546e0fb00254ed63b.jpg',
                    'Answer': 'Fire',
                    'Hint': 'Vuur',
                    'CardType': 'Image'

                }
            ]

    return Response(cards)
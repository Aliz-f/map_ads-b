
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from .serializer import dataFlightSerializer
# Create your views here.

class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return

def map (request):
    return render(request, 'flight/gmap.html')

class getData(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):
        try:
        
            global flight
            flight = request.data
            data = request.data
            print(data)
            for item in data:
                if item.get('validposition')==1 and item.get('lat')!=0.0 and item.get('lon')!=0.0:
                    ser = dataFlightSerializer(data=item)
                    if ser.is_valid():
                        ser.save()        
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(str(e))
            return Response({"details":str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            return Response(flight, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"details":str(e)}, status=status.HTTP_400_BAD_REQUEST)

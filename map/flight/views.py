
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions

# Create your views here.

class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return

def map (request):
    return render(request, 'flight/gmap.html')


class getData(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    
    def post(self, request):
        try:
            self.data = request.data
        except Exception as e:
            return Response({"details":str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"details":str(e)}, status=status.HTTP_400_BAD_REQUEST)


class setData(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    
    def get(self, request):
        try:
            pass
        except Exception as e:
            return Response({"details":str(e)}, status=status.HTTP_400_BAD_REQUEST)
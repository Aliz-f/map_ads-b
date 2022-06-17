
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from .serializer import dataFlightSerializer
from .models import dataFlight

import os
import folium
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
            # print(data)
            for item in data:
                if item.get('validposition')==1 and item.get('lat')!=0.0 and item.get('lon')!=0.0:
                    ser = dataFlightSerializer(data=item)
                    if ser.is_valid():
                        ser.save()
                        return Response(status=status.HTTP_201_CREATED)
                    else:
                        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)        
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            # print(str(e))
            return Response({"details":str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            return Response(flight, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"details":str(e)}, status=status.HTTP_400_BAD_REQUEST)

class generateMap:
    def __init__(self):
        self.flight_list=[]
        self.data=[]
        self.colors=['black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'forestgreen', 'fuchsia', 'gainsboro', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'hotpink', 'indianred', 'indigo', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lime', 'limegreen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mistyrose', 'moccasin', 'navy', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'yellow', 'yellowgreen']
        self.colorIter=0
        self.map=None
        self.prepareData()
        self.createMap()
    
    def prepareData(self):
        locationsTemp = []
        data = dataFlight.objects.all()
        for item in data:
            if item.validposition ==1 and item.lat > 0.0 and item.lon> 0.0:
                eachLocation={
                    'code':item.flight,
                    'lat':item.lat,
                    'long':item.lon,
                }
                locationsTemp.append(eachLocation)
        # print(locationsTemp)
        for loc in locationsTemp:
            if loc['code'] not in self.flight_list:
                self.flight_list.append(loc['code'])

        self.data ={}
        locTemp=[]
        self.colorIter=0
        for flight in self.flight_list:
            for loc in locationsTemp:
                if loc['code'] == flight:
                    locTemp.append(list((float(loc['lat']), float(loc['long']))))
            self.data[flight]={'locations':locTemp, 'color':self.colors[self.colorIter]}
            locTemp=[]
            self.colorIter+=1
            if self.colorIter>=111:
                self.colorIter=0


    def createMap(self):
        self.map = folium.Map(location=[32.935342,51.549186])
        folium.Marker([32.743938, 51.867955], popup="<i>Isfahan International Airport</i>", tooltip='More Details').add_to(self.map)
        for flight in self.flight_list:
            folium.PolyLine(self.data[flight]['locations'], tooltip=f"<i>{flight}</i>",color=self.data[flight]['color'],weight=8, opacity=15).add_to(self.map)
            # folium.t
        path = os.getcwd()
        self.map.save(f"{path}/flight/templates/flight/map.html")


def offlineMap(request):
    Map = generateMap()
    return render(request, 'flight/map.html')
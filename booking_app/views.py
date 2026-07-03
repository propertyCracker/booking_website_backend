from .models import Room, RoomImage
from .serializers import RoomSerializer, RoomImageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def getRooms(request):
    queryset = Room.objects.all()
    serializer = RoomSerializer(data=queryset, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


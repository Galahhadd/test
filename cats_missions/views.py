from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError


from .models import SpyCat, Mission, Target
from .serializers import CatSerializer, MissionSerializer, TargetSeializer

class RetrieveCatsApiView(ListAPIView):
    queryset = SpyCat.objects.all()
    serializer_class = CatSerializer

class CreateCatApiView(CreateAPIView):
    queryset = SpyCat.objects.all()
    serializer_class = CatSerializer

class RetrieveUpdateDestroyCatAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SpyCat.objects.all()
    serializer_class = CatSerializer

class RetrieveMissionsApiView(ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class CreateMissionApiView(CreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class RetrieveUpdateDestroyMissionAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        try:
            self.perform_destroy(mission)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)
    
class UpdateTargetApiView(RetrieveUpdateAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSeializer

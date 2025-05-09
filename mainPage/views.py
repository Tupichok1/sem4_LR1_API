from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from .permissions import IsAuthorOrRead
from .models import Incidents
from .serializers import AttacksSerializer, UpdateAttack

class AllAttacks(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Incidents.objects.all()
    serializer_class = AttacksSerializer

class CreateNote(ListCreateAPIView):
    queryset = Incidents.objects.all()
    serializer_class = AttacksSerializer

class UpdateDeleteNote(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrRead, )
    queryset = Incidents.objects.all()
    serializer_class = UpdateAttack
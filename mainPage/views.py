from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from .permissions import IsAuthorOrRead
from .models import Attacks
from .serializers import AttacksSerializer, UpdateAttack

class AllAttacks(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Attacks.objects.all()
    serializer_class = AttacksSerializer

class CreateNote(ListCreateAPIView):
    queryset = Attacks.objects.all()
    serializer_class = AttacksSerializer

class UpdateDeleteNote(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrRead, )
    queryset = Attacks.objects.all()
    serializer_class = UpdateAttack
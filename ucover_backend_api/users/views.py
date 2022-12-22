from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permisions import IsCoverer

class CustomUserCreate(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format='json'):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(reg_serializer.data, status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsCoverer]
    serializer_class = UserSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, is_active = True).first()
    def list(self,request):
        product_serializer = self.get_serializer(self.get_queryset(), many= True)
        return Response(product_serializer.data,status=status.HTTP_200_OK)
    def create(self, request):
        # Redirige al usuario a la vista CustomUserCreate con los datos del formulario en la solicitud POST con status code 307
        #return redirect('CustomUserCreate', data=request.data)
        return Response({"error": "No se pueden crear nuevos usuarios"}, status=status.HTTP_400_BAD_REQUEST)

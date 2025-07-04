from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User
from .models import ExpenseIncome
from .serializers import RegisterSerializer, ExpenseIncomeSerializer
from .permissions import IsOwnerOrSuperuser


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrSuperuser]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return ExpenseIncome.objects.all()

        if self.action == 'list':
            return ExpenseIncome.objects.filter(user=user)

        return ExpenseIncome.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj

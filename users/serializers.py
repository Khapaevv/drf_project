from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from users.models import Payments, User


class UserSerializer(ModelSerializer):

    payments_history = SerializerMethodField()


    def get_payments_history(self, user):
        return Payments.objects.filter(user=user).values(
            "payment_date",
            "payment_amount",
        )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "phone",
            "city",
            "payments_history",
            "password",
        )


class PaymentsSerializer(ModelSerializer):

    class Meta:
        model = Payments
        fields = "__all__"

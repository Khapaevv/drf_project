from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from payments.models import Payments
from payments.serializers import PaymentsSerializer
from payments.services import (create_stripe_price, create_stripe_product,
                               create_stripe_session)


class PaymentsCreateAPIView(CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)

        if payment.paid_course or payment.paid_lesson:
            product = (
                payment.paid_course if payment.paid_course else payment.paid_lesson
            )
            product_id = create_stripe_product(product)
            price = create_stripe_price(payment.payment_amount, product_id)
            session_id, payment_link = create_stripe_session(price)

            payment.session_id = session_id
            payment.link = payment_link
            payment.save()
        else:
            raise ValidationError("Выберите курс или урок для оплаты")


class PaymentsListAPIView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["payment_method", "paid_course", "paid_lesson"]
    ordering_fields = ["payment_date"]


class PaymentsRetrieveAPIView(RetrieveAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsUpdateAPIView(UpdateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsDestroyAPIView(DestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

from rest_framework.routers import SimpleRouter
from django.urls import path

from payments.apps import PaymentsConfig
from payments.views import PaymentsListAPIView, PaymentsRetrieveAPIView, PaymentsCreateAPIView, \
    PaymentsDestroyAPIView, PaymentsUpdateAPIView

app_name = PaymentsConfig.name

# router_payments = SimpleRouter()
# router_payments.register("payments/", PaymentsListAPIView)

urlpatterns = [
    path("payments/", PaymentsListAPIView.as_view(), name="payments_list"),
    path("payments/<int:pk>/", PaymentsRetrieveAPIView.as_view(), name="payments_retrieve"),
    path("payments/create/", PaymentsCreateAPIView.as_view(), name="payments_create"),
    path(
        "payments/<int:pk>/delete/", PaymentsDestroyAPIView.as_view(), name="payments_delete"
    ),
    path(
        "payments/<int:pk>/update/", PaymentsUpdateAPIView.as_view(), name="payments_update"
    ),

]
               # + router_payments.urls)


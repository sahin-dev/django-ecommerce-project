from django.urls import path
from core.views import index,payment

app_name = "core"

urlpatterns = [
    path("", index,name="index"),
    path("payment/", payment,name='payment')
]

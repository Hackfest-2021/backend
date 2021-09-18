from django.urls import path

from alerts.views import AlertCreateList, alert_types

app_name = 'alerts'
urlpatterns = [
    path('', AlertCreateList.as_view(), name="create_alert"),
    path('types/', alert_types, name="create_alert"),

]
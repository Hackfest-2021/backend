from django.urls import path

from alerts.views import AlertCreateList

app_name = 'alerts'
urlpatterns = [
    path('', AlertCreateList.as_view(), name="create_alert"),

]
from django.urls import path

from alerts.views import AlertCreateList

app_name = 'alerts'
urlpatterns = [
    path('', AlertCreateList, name="create_alert"),

]
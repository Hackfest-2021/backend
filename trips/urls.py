from django.urls import path

from trips.views import CreateListTrips, CreateTripPassenger, CreateTripAlert, CreatePassengerTripAlertFeedBack

app_name = 'trips'
urlpatterns = [
    path('', CreateListTrips.as_view(), name="create_trip"),
    path('passenger/', CreateTripPassenger.as_view(), name='create_passenger'),
    path('alert/', CreateTripAlert.as_view(), name='create_trip_alert'),
    path('passenger/alert/', CreatePassengerTripAlertFeedBack.as_view(), name='create_passenger_alert'),

]

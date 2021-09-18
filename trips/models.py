from django.db import models

# Create your models here.
from account.models import Account
from alerts.models import Alerts


class Trips(models.Model):
    id = models.AutoField(primary_key=True, db_column="id", auto_created=True)
    driver = models.ForeignKey(Account, on_delete=models.DO_NOTHING, db_column="driver")
    finished = models.BooleanField(default=False)

class TripPassengers(models.Model):
    id = models.AutoField(primary_key=True, db_column="id", auto_created=True)
    passenger = models.ForeignKey(Account, on_delete=models.CASCADE, db_column="passenger")
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE, db_column="trip")

class TripAlerts(models.Model):
    id = models.AutoField(primary_key=True, db_column="id", auto_created=True)
    alert = models.ForeignKey(Alerts, on_delete=models.CASCADE, db_column="alert")
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE, db_column="trip")

#     todo on Trip Alert save send that alert to all trip passengers

class PassengerAlerts(models.Model):
    id = models.AutoField(primary_key=True, db_column="id", auto_created=True)
    is_alert_valid = models.BooleanField(default=True)
    trip_alert = models.ForeignKey(TripAlerts, on_delete=models.CASCADE, db_column="trip_alert")
    passenger = models.ForeignKey(Account, on_delete=models.CASCADE, db_column="passenger")

#     todo on passenger save allert call function to reevaluate alert sevrity





from django.db import models


# Create your models here.

class AlertType(models.Model):
    un_authorized = "un authorized"
    drowsy = 'drowsy'
    distracted = 'distracted'
    weapon = "weapon"
    alert_types = [
        drowsy, un_authorized, distracted, weapon
    ]
    id = models.AutoField(primary_key=True, db_column="id", auto_created=True)
    name = models.CharField(max_length=250, choices=alert_types)


class Alerts(models.Model):
    id = models.AutoField(primary_key=True, db_column="id", auto_created=True)
    alert_type = models.ForeignKey(AlertType, on_delete=models.SET_NULL, null=True, db_column="alert_type")
    trip_id = models.CharField(max_length=250, default='trip_1')

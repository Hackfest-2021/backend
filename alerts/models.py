from django.db import models


# Create your models here.

class AlertType(models.Model):
    un_authorized = "un authorized"
    drowsy = 'drowsy'
    distracted = 'distracted'
    weapon = "weapon"
    alert_types = [
        (drowsy,drowsy), (un_authorized,un_authorized), (distracted,distracted), (weapon,weapon)
    ]
    id = models.AutoField(primary_key=True, db_column="id", auto_created=True)
    name = models.CharField(max_length=250, choices=alert_types)


class Alerts(models.Model):
    id = models.AutoField(primary_key=True, db_column="id", auto_created=True)
    alert_type = models.ForeignKey(AlertType, on_delete=models.SET_NULL, null=True, db_column="alert_type")
    alert_severity = models.FloatField(default=0.5)
    resolved = models.BooleanField(default=False)


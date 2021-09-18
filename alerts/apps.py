from django.apps import AppConfig




class AlertsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alerts'

    def ready(self):
        # pass
        from alerts.models import AlertType
        for i in AlertType.alert_types:
            alert_type = AlertType.objects.filter(name=i[0]).first()
            if alert_type:
                pass
            else:
                alert_type = AlertType()
                alert_type.name = i
                alert_type.save()
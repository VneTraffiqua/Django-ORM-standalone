from django.db import models
import django.utils.timezone
import datetime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=django.utils.timezone.localtime(
                value=self.entered_at
            ),
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        now_time = datetime.datetime.now(datetime.timezone.utc)
        if self.leaved_at:
            difference_in_time = self.leaved_at - self.entered_at
        else:
            difference_in_time = now_time - self.entered_at
        return difference_in_time

    def is_visit_long(self, minutes=60):
        visit_time = self.get_duration()
        visit_time_in_sec = int(datetime.timedelta.total_seconds(visit_time))
        return (visit_time_in_sec // minutes * 60) >= minutes * 60

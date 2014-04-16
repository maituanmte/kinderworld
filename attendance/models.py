from django.db import models

class WorkingSchedule(models.Model):
    pass

class SchoolCalendar(models.Model):
    pass

class LeaveForm(models.Model):
    pass

class DayOff(models.Model):
    pass

class DayOn(models.Model):
    pass

class Reason(models.Model):
    pass

class LeaveFormReason(Reason):
    class Meta:
        proxy = True
    pass

class WorkingScheduleReason(Reason):
    class Meta:
        proxy = True
    pass

class SchoolCalendarReason(Reason):
    class Meta:
        proxy = True
    pass


from django.db import models
from students.models import SchoolClass


class CalendarEvent(models.Model):
    EVENT_TYPE_CHOICES = [
        ("PTM", "Parent-Teacher Meeting"),
        ("HOLIDAY", "Holiday"),
        ("EXAM", "Exam"),
        ("ACTIVITY", "Activity"),
        ("OTHER", "Other"),
    ]

    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=10, choices=EVENT_TYPE_CHOICES)
    date = models.DateField()
    school_class = models.ForeignKey(
        SchoolClass, on_delete=models.CASCADE, null=True, blank=True,
        help_text="Leave blank for a school-wide event"
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.date})"
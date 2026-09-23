from django.db import models
from students.models import SchoolClass
from accounts.models import User


class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    school_class = models.ForeignKey(
        SchoolClass, on_delete=models.CASCADE, null=True, blank=True,
        help_text="Leave blank to send to the whole school"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
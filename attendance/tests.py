import pytest
from datetime import date
from django.db import IntegrityError
from students.models import SchoolClass, Student
from attendance.models import AttendanceRecord


@pytest.mark.django_db
def test_cannot_duplicate_attendance_for_same_day():
    school_class = SchoolClass.objects.create(name="Grade 5", section="A")
    student = Student.objects.create(first_name="Asha", last_name="Rao",
                                      date_of_birth="2015-05-10", school_class=school_class)
    AttendanceRecord.objects.create(student=student, date=date(2026, 9, 1), status="PRESENT")

    with pytest.raises(IntegrityError):
        AttendanceRecord.objects.create(student=student, date=date(2026, 9, 1), status="ABSENT")
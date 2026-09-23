import pytest
from datetime import date
from django.contrib.auth import get_user_model
from students.models import SchoolClass, Student

User = get_user_model()


@pytest.mark.django_db
def test_student_creation_and_str():
    school_class = SchoolClass.objects.create(name="Grade 5", section="A")
    student = Student.objects.create(
        first_name="Asha", last_name="Rao",
        date_of_birth=date(2015, 5, 10),
        school_class=school_class,
        blood_group="O+",
    )
    assert str(student) == "Asha Rao"
    assert student.school_class == school_class


@pytest.mark.django_db
def test_parent_only_sees_own_children():
    school_class = SchoolClass.objects.create(name="Grade 5", section="A")
    parent1 = User.objects.create_user(username="p1", password="x", role="PARENT")
    parent2 = User.objects.create_user(username="p2", password="x", role="PARENT")

    Student.objects.create(first_name="Kid", last_name="One", date_of_birth="2015-01-01",
                            school_class=school_class, parent=parent1)
    Student.objects.create(first_name="Kid", last_name="Two", date_of_birth="2016-01-01",
                            school_class=school_class, parent=parent2)

    assert Student.objects.filter(parent=parent1).count() == 1

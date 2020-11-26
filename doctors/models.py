from datetime import date

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
from django.urls import reverse


class Profession(models.Model):
    STATUS_CHOICES = [('Rehab', 'Rehabilitator'),
                      ('Physio', 'Physiotherapist'),
                      ('Mass', 'Masseur'),
                      ('Train', 'Trainer'),
                      ]
    name = models.CharField("doctor's profession", max_length=13,
                            choices=STATUS_CHOICES,
                            default='instructor')

    class Meta:
        verbose_name = 'Professions'
        verbose_name_plural = 'Profession'

    def __str__(self):
        return self.name


class Service(models.Model):
    STATUS_CHOICES = [('PT', 'Personal training'),
                      ('GT', 'Group training'),
                      ('MS', 'Massage'),
                      ('RT', 'Rehabilitation training'),
                      ]
    name = models.CharField("your service", max_length=23,
                            choices=STATUS_CHOICES,
                            default='instructor')
    description = models.TextField('Description', max_length=1000)
    price = models.IntegerField('Price for this service', max_length=1000)

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Service"


class User(AbstractBaseUser):
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    email = models.EmailField("Email")
    avatar = models.ImageField("Avatar", upload_to="users/")
    service = models.ManyToManyField(Service, related_name="services")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "User"


class Doctor(AbstractBaseUser):
    first_name = models.CharField("doctor's first name", max_length=250, blank=False,
                                  error_messages={'blank': 'Cant be empty'})
    second_name = models.CharField("doctor's second name", max_length=250, blank=False,
                                   error_messages={'blank': 'Cant be empty'})
    bio = models.TextField("doctor's biography")
    diploma = models.ImageField("doctor's diplomas", upload_to="doc_diploma/")
    avatar = models.ImageField("doctor's photo", upload_to='doc_avatar/')
    date_of_registration = models.DateTimeField("doctor's date of registration", default=date.today)
    profession = models.ForeignKey(Profession, verbose_name="Profession", on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(User, verbose_name="Patient", on_delete=models.SET_NULL, null=True)
    service = models.ManyToManyField(Service,  related_name="services")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('doc_detail', kwargs={"slug": self.first_name})

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "User"


class RatingStar(models.Model):
    value = models.SmallIntegerField("Value", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Star rating"
        verbose_name_plural = "Stars rating"
        ordering = ["-value"]


class Rating(models.Model):
    ip = models.CharField("IP", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="star")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="doctor", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.doctor}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

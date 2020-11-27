from datetime import date

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from django.urls import reverse


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


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
    description = models.TextField('Description', max_length=1000)
    price = models.IntegerField('Price for this service')
    name = models.CharField("doctor's profession", max_length=21,
                            choices=STATUS_CHOICES,
                            default='training')

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Service"


class User(AbstractBaseUser):
    user_name = models.CharField("User name", max_length=100)
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    email = models.EmailField("Email", unique=True)
    avatar = models.ImageField("Avatar", upload_to="users/")
    service = models.ManyToManyField(Service)
    USERNAME_NAME = 'email'
    USERNAME_FIELD = 'email'
    objects = UserManager()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # This next two params need to create user not remove them
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "User"


class Doctor(AbstractBaseUser):
    user_name = models.CharField("User name", max_length=100)
    first_name = models.CharField("doctor's first name", max_length=250, blank=False,
                                  error_messages={'blank': 'Cant be empty'})
    second_name = models.CharField("doctor's second name", max_length=250, blank=False,
                                   error_messages={'blank': 'Cant be empty'})
    bio = models.TextField("doctor's biography")
    diploma = models.ImageField("doctor's diplomas", upload_to="doc_diploma/")
    avatar = models.ImageField("doctor's photo", upload_to='doc_avatar/')
    date_of_registration = models.DateTimeField("doctor's date of registration", default=date.today)
    profession = models.ForeignKey(Profession, verbose_name="Profession", on_delete=models.SET_NULL, null=True)
    email = models.EmailField("Email", unique=True)
    USERNAME_NAME = 'email'
    USERNAME_FIELD = 'email'
    service = models.ManyToManyField(Service)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    # This next two params need to create user not remove them
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('doc_detail', kwargs={"slug": self.first_name})

    class Meta:
        verbose_name = "Doctors"
        verbose_name_plural = "Doctor"


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


class Review(models.Model):
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Text', max_length=1000)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="doctor")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user")

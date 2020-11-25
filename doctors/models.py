from django.db import models
from django.urls import reverse
from django.utils import timezone


class Doctor(models.Model):
    STATUS_CHOICES = [('Rehab', 'Rehabilitator'),
                      ('Physio', 'Physiotherapist'),
                      ('Mass', 'Masseur'),
                      ('Train', 'Trainer'),
                      ]
    first_name = models.CharField("doctor's first name", max_length=250, blank=False,
                                  error_messages={'blank': 'Cant be empty'})
    second_name = models.CharField("doctor's second name", max_length=250, blank=False,
                                   error_messages={'blank': 'Cant be empty'})
    bio = models.TextField("doctor's biography")
    diploma = models.ImageField("doctor's diplomas")
    avatar = models.ImageField("doctor's photo")
    rating = models.IntegerField("doctor's rating", default=0)
    email = models.EmailField("doctor's email", unique=True, blank=False, )
    date_of_registration = models.DateTimeField("doctor's date of registration", auto_now=True)
    profession = models.CharField("doctor's specialization", max_length=13,
                                  choices=STATUS_CHOICES,
                                  default='instructor')

    class Meta:
        ordering = ('-rating',)

    def get_absolute_url(self):
        return reverse('doctors', args=[self.pk])

    def __str__(self):
        return f'{self.first_name} {self.profession}'


class Post(models.Model):
    author = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    photo = models.URLField('Link for photo for your post')

    def __str__(self):
        return self.title

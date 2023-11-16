from django.db import models


class DragonAdded(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    MALE = "M"
    FEMALE = "F"

    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
    ]

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    digestion_period_hours = models.IntegerField()
    herbivore = models.BooleanField()
    time = models.TimeField()
    park_id = models.IntegerField()

    def __str__(self):
        return self.name


class DragonRemoved(models.Model):
    dragon_id = models.IntegerField()
    time = models.DateTimeField()
    park_id = models.IntegerField()

    def __str__(self):
        return self.dragon_id


class DragonLocationUpdated(models.Model):
    location = models.CharField(max_length=10)
    dragon_id = models.IntegerField()
    time = models.DateTimeField()
    park_id = models.IntegerField()

    def __str__(self):
        return self.dragon_id


class DragonFed(models.Model):
    dragon_id = models.IntegerField()
    time = models.DateTimeField()
    park_id = models.IntegerField()
    last_meal_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.dragon_id


class MaintenancePerformed(models.Model):
    location = models.CharField(max_length=10)
    time = models.DateTimeField()
    park_id = models.IntegerField()





# class Dragons(models.Model):
#     name = models.CharField()
#     id = models.AutoField(primary_key=True)
#     zone = models.ForeignKey(zones , on_delete= models.CASCADE)

#     MALE = 'M'
#     FEMALE = 'F'

#     GENDER_CHOICES = [
#         (MALE, 'Male'),
#         (FEMALE, 'Female'),
#     ]

#     gender = models.CharField(
#         max_length=1,
#         choices=GENDER_CHOICES,
#         default=MALE,
#     )

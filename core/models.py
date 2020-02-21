from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='profile'
    )
    bio = models.CharField(max_length=500, null=True, blank=True)
    phone_number = PhoneNumberField()
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    update_date = models.DateTimeField('update_date', auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.id)


class Ticket(models.Model):
    SALES = 'Sales'
    ACCOUNTS = 'Accounts'
    IT = 'IT'
    SUPPORT_CATEGORY_CHOICES = [
        (SALES, 'Sales'),
        (ACCOUNTS, 'Accounts'),
        (IT, 'IT'),
    ]

    NEWLY_LOGGED = 'Newly logged'
    IN_PROGRESS = 'In Progress'
    RESOLVED = 'Resolved'
    STATUS_CHOICES = [
        (NEWLY_LOGGED, 'Newly logged'),
        (IN_PROGRESS, 'In Progress'),
        (RESOLVED, 'Resolved'),
    ]

    VERY_HIGH = 'Very'
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'low'
    PRIORITY_CHOICES = [
        (VERY_HIGH, 'Very High'),
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    logger = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='logger',
    )
    category = models.CharField(
        max_length=100,
        default=SALES,
        choices=SUPPORT_CATEGORY_CHOICES
    )
    priority = models.CharField(
        max_length=100,
        default=LOW,
        choices=PRIORITY_CHOICES
    )
    status = models.CharField(
        max_length=100,
        default=NEWLY_LOGGED,
        choices=STATUS_CHOICES
    )
    subject = models.CharField(max_length=254, blank=True)
    description = models.CharField(max_length=500, blank=True)
    start_date = models.DateField(default=None, null=True)
    end_date = models.DateField(default=None, null=True)
    update_date = models.DateTimeField('update_date', auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)


class TicketGeoLocation(models.Model):
    ticket = models.OneToOneField(
        Ticket,
        on_delete=models.CASCADE,
        verbose_name='ticket'
    )
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

from django.dispatch import receiver
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User

class Job(models.Model):
    customer_name = models.CharField(max_length=300)
    def __str__(self):

        return self.customer_name

    GEAR_CHOICES = (
            ('All','ALL'),
            ('Lockpick Kit', 'LOCKPICK KIT'),
            ('DRILL','DRILL'),
            ('Casual','CASUAL'),
            ('Non Specific','NON SPECIFIC'),
        )
            
    priority = models.CharField(max_length=300, default="Urgent, Normal, Low")
    street_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)
    supplies_needed = models.CharField(max_length=300, choices=GEAR_CHOICES, default='All')
    accepted = models.BooleanField(default=False)
    accepted_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    done = models.BooleanField(default=False)
    free_field = models.TextField(max_length=300, null=True, blank=True)

    def get_absolute_url(self):
	    return f"/{self.pk}"

@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        print("Creating Inactive User")
        instance.is_active = False
    else:
        print("Updating User Record")

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Server(models.Model):

    #__Server_FIELDS__
    vm_name = models.CharField(max_length=255, null=True, blank=True)
    fqdn_domain = models.CharField(max_length=255, null=True, blank=True)
    ip = models.IntegerField(null=True, blank=True)
    vs_intenal = models.IntegerField(null=True, blank=True)
    vs_external = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    responsible = models.CharField(max_length=255, null=True, blank=True)

    #__Server_FIELDS__END

    class Meta:
        verbose_name        = _("Server")
        verbose_name_plural = _("Server")



#__MODELS__END

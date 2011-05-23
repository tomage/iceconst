from django.db import models
from django.contrib.auth.models import User as ContribUser, Group as ContribGroup
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class User(ContribUser):
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
    TYPE_CHOICES = (
        ('ADMIN', _('Administrator')),
        ('ANALYST', _('Analyst')),
        ('NORMAL', _('Normal internet user')),
    )
    type = models.CharField(_('Type'), \
            max_length=max(len(s[0]) for s in TYPE_CHOICES), \
            choices=TYPE_CHOICES)
    
    def save(self, *args, **kwargs):
        self.is_superuser = self.type == 'ADMIN'
        self.is_staff = self.type == 'ANALYST'
        super(User, self).save(*args, **kwargs)

class Group(ContribGroup):
    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
    pass
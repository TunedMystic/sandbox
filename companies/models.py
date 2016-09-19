from __future__ import unicode_literals

from django.db import models


class Company(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(
        max_length=400,
        verbose_name='Name',
        help_text='Name of Company',
    )

    description = models.TextField(
        max_length=1500,
        verbose_name='Description',
        help_text='An overview of the company',
    )

    website = models.URLField(
        max_length=400,
        null=True,
        blank=True,
        verbose_name='Website',
        help_text="company's website",
    )

    def __unicode__(self):
        return '{}'.format(self.name[:24])

    class Meta:
        ordering = ('name',)

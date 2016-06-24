# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('notivinco', '0002_auto_20160624_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='user',
            field=models.ForeignKey(related_name='notice', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

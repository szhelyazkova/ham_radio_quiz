# Generated by Django 4.1.3 on 2022-12-12 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('examination', '0008_examresultsmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examresultsmodel',
            name='username_exam',
        ),
        migrations.AddField(
            model_name='examresultsmodel',
            name='user_exam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

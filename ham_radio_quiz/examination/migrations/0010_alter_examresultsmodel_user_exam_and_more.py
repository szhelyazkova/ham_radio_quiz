# Generated by Django 4.1.3 on 2022-12-13 00:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('examination', '0009_remove_examresultsmodel_username_exam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examresultsmodel',
            name='user_exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='generatedquestionsmodel',
            name='user_generated_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-11 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0006_remove_exammodel_user_test_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='exammodel',
            name='user_test_question_id',
            field=models.PositiveIntegerField(default=None),
        ),
    ]

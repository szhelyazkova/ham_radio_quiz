# Generated by Django 4.1.3 on 2022-12-10 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_question_amateur_class_alter_question_category'),
        ('examination', '0003_remove_exammodel_user_test_id_exammodel_user_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exammodel',
            name='user_test_question_id',
        ),
        migrations.AddField(
            model_name='exammodel',
            name='user_test_question_id',
            field=models.ManyToManyField(to='quiz.question'),
        ),
    ]

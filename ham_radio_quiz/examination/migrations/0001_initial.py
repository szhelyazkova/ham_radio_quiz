# Generated by Django 4.1.3 on 2022-12-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_test_id', models.IntegerField(default=None)),
                ('user_test_question_id', models.IntegerField(default=None)),
                ('user_test_answer_id', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]

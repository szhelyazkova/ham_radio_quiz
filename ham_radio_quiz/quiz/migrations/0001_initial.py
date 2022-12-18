# Generated by Django 4.1.3 on 2022-11-13 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('TECHNICAL', 'Електротехника и радиотехника'), ('RULES', 'Кодове и радиолюбителски съкращения, правила и процедури'), ('REGULATIONS', 'Нормативна уредба')], max_length=15)),
                ('amateur_class', models.CharField(choices=[('1', '1'), ('2', '2')], max_length=15)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('is_correct', models.BooleanField(default=False)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='quiz.question')),
            ],
        ),
    ]

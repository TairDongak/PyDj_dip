# Generated by Django 3.2 on 2021-05-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210529_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

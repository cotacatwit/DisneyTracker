# Generated by Django 3.2.8 on 2021-10-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(default='', max_length=200)),
                ('start_date', models.DateField(default='')),
                ('end_date', models.DateField(default='')),
            ],
        ),
    ]

# Generated by Django 3.1.7 on 2021-12-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_meterreading_weekly_consumption'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyConsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_ending', models.DateField()),
                ('consumption', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]

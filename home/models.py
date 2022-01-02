from django.db import models


class Printer(models.Model):
    hours_used = models.DecimalField(max_digits=5, decimal_places=2)
    daily_cost = models.DecimalField(max_digits=9, decimal_places=2)


class HandDryer(models.Model):
    hours_used = models.DecimalField(max_digits=5, decimal_places=2)
    daily_cost = models.DecimalField(max_digits=9, decimal_places=2)


class FluorescentTube(models.Model):
    hours_used = models.DecimalField(max_digits=5, decimal_places=2)
    daily_cost = models.DecimalField(max_digits=9, decimal_places=2)


class Floodlight(models.Model):
    hours_used = models.DecimalField(max_digits=5, decimal_places=2)
    daily_cost = models.DecimalField(max_digits=9, decimal_places=2)


class Amplifier(models.Model):
    hours_used = models.DecimalField(max_digits=5, decimal_places=2)
    daily_cost = models.DecimalField(max_digits=9, decimal_places=2)


class Computers(models.Model):
    hours_used = models.DecimalField(max_digits=5, decimal_places=2)
    daily_cost = models.DecimalField(max_digits=9, decimal_places=2)


class Photocopier(models.Model):
    hours_used = models.DecimalField(max_digits=5, decimal_places=2)
    daily_cost = models.DecimalField(max_digits=9, decimal_places=2)


class MeterReading(models.Model):
    date = models.DateField()
    meter_location = models.CharField(max_length=100)
    reading = models.DecimalField(max_digits=5, decimal_places=2)


class Meter1(models.Model):
    date = models.DateField()
    meter_location = models.CharField(max_length=100)
    reading = models.DecimalField(max_digits=5, decimal_places=2)
    consumption = models.DecimalField(max_digits=5, decimal_places=2)


class Meter2(models.Model):
    date = models.DateField()
    meter_location = models.CharField(max_length=100)
    reading = models.DecimalField(max_digits=5, decimal_places=2)
    consumption = models.DecimalField(max_digits=5, decimal_places=2)


class Meter3(models.Model):
    date = models.DateField()
    meter_location = models.CharField(max_length=100)
    reading = models.DecimalField(max_digits=5, decimal_places=2)
    consumption = models.DecimalField(max_digits=5, decimal_places=2)




















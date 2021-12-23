from django.db import models


class Printer(models.Model):
    hours_used = models. PositiveBigIntegerField()
    daily_cost = models. PositiveBigIntegerField()

class HandDryer(models.Model):
    hours_used = models. PositiveBigIntegerField()
    daily_cost = models. PositiveBigIntegerField()

class FluorescentTube(models.Model):
    hours_used = models. PositiveBigIntegerField()
    daily_cost = models. PositiveBigIntegerField()

class Floodlight(models.Model):
    hours_used = models. PositiveBigIntegerField()
    daily_cost = models. PositiveBigIntegerField()

class Amplifier(models.Model):
    hours_used = models. PositiveBigIntegerField()
    daily_cost = models. PositiveBigIntegerField()

class Computers(models.Model):
    hours_used = models. PositiveBigIntegerField()
    daily_cost = models. PositiveBigIntegerField()

class Photocopier(models.Model):
    hours_used = models. PositiveBigIntegerField()
    daily_cost = models. PositiveBigIntegerField()








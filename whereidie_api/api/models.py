# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PlantLocations(models.Model):
    queueid = models.CharField(max_length=32)
    mapid = models.CharField(max_length=32)
    rank_id = models.IntegerField()
    red_team_econ = models.CharField(max_length=32)
    blue_team_econ = models.CharField(max_length=32)
    location_x = models.IntegerField()
    location_y = models.IntegerField()

    class Meta:
        db_table = 'PLANT_LOCATIONS'


class KdCollectorAscent(models.Model):
    queueid = models.CharField(max_length=32)
    rank_id = models.IntegerField()
    red_team_econ = models.CharField(max_length=32)
    blue_team_econ = models.CharField(max_length=32)
    attacker_team = models.CharField(max_length=32)
    victim_team = models.CharField(max_length=32)
    attacker_location_x = models.IntegerField()
    attacker_location_y = models.IntegerField()
    victim_location_x = models.IntegerField()
    victim_location_y = models.IntegerField()
    plant_status = models.CharField(max_length=32)

    class Meta:
        db_table = 'kd_collector_ASCENT'


class KdCollectorBind(models.Model):
    queueid = models.CharField(max_length=32)
    rank_id = models.IntegerField()
    red_team_econ = models.CharField(max_length=32)
    blue_team_econ = models.CharField(max_length=32)
    attacker_team = models.CharField(max_length=32)
    victim_team = models.CharField(max_length=32)
    attacker_location_x = models.IntegerField()
    attacker_location_y = models.IntegerField()
    victim_location_x = models.IntegerField()
    victim_location_y = models.IntegerField()
    plant_status = models.CharField(max_length=32)

    class Meta:
        db_table = 'kd_collector_BIND'


class KdCollectorBreeze(models.Model):
    queueid = models.CharField(max_length=32)
    rank_id = models.IntegerField()
    red_team_econ = models.CharField(max_length=32)
    blue_team_econ = models.CharField(max_length=32)
    attacker_team = models.CharField(max_length=32)
    victim_team = models.CharField(max_length=32)
    attacker_location_x = models.IntegerField()
    attacker_location_y = models.IntegerField()
    victim_location_x = models.IntegerField()
    victim_location_y = models.IntegerField()
    plant_status = models.CharField(max_length=32)

    class Meta:
        db_table = 'kd_collector_BREEZE'


class KdCollectorFracture(models.Model):
    queueid = models.CharField(max_length=32)
    rank_id = models.IntegerField()
    red_team_econ = models.CharField(max_length=32)
    blue_team_econ = models.CharField(max_length=32)
    attacker_team = models.CharField(max_length=32)
    victim_team = models.CharField(max_length=32)
    attacker_location_x = models.IntegerField()
    attacker_location_y = models.IntegerField()
    victim_location_x = models.IntegerField()
    victim_location_y = models.IntegerField()
    plant_status = models.CharField(max_length=32)

    class Meta:
        db_table = 'kd_collector_FRACTURE'


class KdCollectorHaven(models.Model):
    queueid = models.CharField(max_length=32)
    rank_id = models.IntegerField()
    red_team_econ = models.CharField(max_length=32)
    blue_team_econ = models.CharField(max_length=32)
    attacker_team = models.CharField(max_length=32)
    victim_team = models.CharField(max_length=32)
    attacker_location_x = models.IntegerField()
    attacker_location_y = models.IntegerField()
    victim_location_x = models.IntegerField()
    victim_location_y = models.IntegerField()
    plant_status = models.CharField(max_length=32)

    class Meta:
        db_table = 'kd_collector_HAVEN'


class KdCollectorIcebox(models.Model):
    queueid = models.CharField(max_length=32)
    rank_id = models.IntegerField()
    red_team_econ = models.CharField(max_length=32)
    blue_team_econ = models.CharField(max_length=32)
    attacker_team = models.CharField(max_length=32)
    victim_team = models.CharField(max_length=32)
    attacker_location_x = models.IntegerField()
    attacker_location_y = models.IntegerField()
    victim_location_x = models.IntegerField()
    victim_location_y = models.IntegerField()
    plant_status = models.CharField(max_length=32)

    class Meta:
        db_table = 'kd_collector_ICEBOX'


class KdCollectorSplit(models.Model):
    queueid = models.CharField(max_length=32)
    rank_id = models.IntegerField()
    red_team_econ = models.CharField(max_length=32)
    blue_team_econ = models.CharField(max_length=32)
    attacker_team = models.CharField(max_length=32)
    victim_team = models.CharField(max_length=32)
    attacker_location_x = models.IntegerField()
    attacker_location_y = models.IntegerField()
    victim_location_x = models.IntegerField()
    victim_location_y = models.IntegerField()
    plant_status = models.CharField(max_length=32)

    class Meta:
        db_table = 'kd_collector_SPLIT'

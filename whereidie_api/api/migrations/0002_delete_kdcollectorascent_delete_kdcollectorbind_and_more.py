# Generated by Django 4.0.1 on 2022-01-23 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KdCollectorAscent',
        ),
        migrations.DeleteModel(
            name='KdCollectorBind',
        ),
        migrations.DeleteModel(
            name='KdCollectorBreeze',
        ),
        migrations.DeleteModel(
            name='KdCollectorFracture',
        ),
        migrations.DeleteModel(
            name='KdCollectorHaven',
        ),
        migrations.DeleteModel(
            name='KdCollectorIcebox',
        ),
        migrations.DeleteModel(
            name='KdCollectorSplit',
        ),
        migrations.DeleteModel(
            name='PlantLocations',
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-20 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cross_section', models.IntegerField(choices=[(1.5, '1.5mm2'), (2.5, '2.5mm2'), (4, '4mm2'), (6, '6mm2'), (10, '10mm2'), (16, '16mm2'), (25, '25mm2'), (35, '35mm2'), (50, '50mm2'), (70, '70mm2'), (95, '95mm2'), (120, '120mm2'), (150, '150mm2'), (185, '185mm2'), (240, '240mm2'), (300, '300mm2')])),
                ('insulation', models.CharField(choices=[('PVC', 'PVC'), ('XLPE', 'XLPE'), ('PILC', 'PILC')], max_length=5)),
                ('conductor', models.CharField(choices=[('copper', 'Copper'), ('aluminium', 'Aluminium')], max_length=15)),
                ('voltage_rating', models.CharField(choices=[('600/1000 V', '600/1000 V'), ('6.35/11 kV', '6.35/11 kV')], max_length=20)),
            ],
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-02 01:12

from django.db import migrations


def default_user(apps, schema_editor):
    user = apps.get_model('inoa_site', 'User')
    user_detail = apps.get_model('inoa_site', 'UserDetail')
    user.username = 'caio'
    user.password = 'caio'

    user_detail.first_name = user
    user_detail.first_name = 'Caio Ohman'
    user_detail.last_name = 'Balthazar Gaudêncio'


class Migration(migrations.Migration):

    dependencies = [
        ('inoa_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(default_user),
    ]

# Generated by Django 2.2.4 on 2019-08-22 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20190822_0830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='items',
            new_name='item',
        ),
    ]

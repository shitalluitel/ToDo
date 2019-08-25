# Generated by Django 2.2.4 on 2019-08-21 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Todo', 'Todo'), ('Doing', 'Doing'), ('Done', 'Done')], max_length=6)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['modified_at'],
            },
        ),
    ]

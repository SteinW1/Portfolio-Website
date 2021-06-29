# Generated by Django 3.2.4 on 2021-06-29 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_name', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('short_description', models.CharField(max_length=200)),
                ('long_description', models.TextField(blank=True)),
                ('github_link', models.URLField(blank=True)),
                ('status', models.CharField(choices=[('complete', 'complete'), ('incomplete', 'incomplete')], default='incomplete', max_length=10)),
            ],
        ),
    ]

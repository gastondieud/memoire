# Generated by Django 4.1.7 on 2023-06-01 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='matelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=200)),
                ('prix', models.FloatField(default=0)),
                ('type', models.CharField(max_length=100)),
                ('dimension', models.CharField(max_length=200)),
            ],
        ),
    ]

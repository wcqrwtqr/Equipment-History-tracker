# Generated by Django 3.1.2 on 2022-02-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_num', models.CharField(max_length=200, unique=True)),
                ('serial_num', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=800, null=True)),
                ('equ_type', models.CharField(blank=True, max_length=200, null=True)),
                ('BU', models.CharField(blank=True, max_length=4, null=True)),
            ],
            options={
                'ordering': ['equ_type'],
            },
        ),
    ]
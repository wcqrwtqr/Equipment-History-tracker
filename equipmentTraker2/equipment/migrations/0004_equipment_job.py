# Generated by Django 3.1.2 on 2022-02-18 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20220218_2039'),
        ('equipment', '0003_auto_20220218_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jobs.jobs'),
        ),
    ]

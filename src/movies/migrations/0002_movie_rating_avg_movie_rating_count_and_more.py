# Generated by Django 5.2.4 on 2025-07-14 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating_avg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating_last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

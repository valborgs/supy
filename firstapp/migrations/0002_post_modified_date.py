# Generated by Django 2.2.4 on 2021-07-02 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='modified_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

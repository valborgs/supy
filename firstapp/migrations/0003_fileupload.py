# Generated by Django 3.2.8 on 2021-10-07 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_post_modified_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=40, null=True)),
                ('imgfile', models.ImageField(blank=True, null=True, upload_to='')),
                ('memo', models.TextField()),
            ],
        ),
    ]

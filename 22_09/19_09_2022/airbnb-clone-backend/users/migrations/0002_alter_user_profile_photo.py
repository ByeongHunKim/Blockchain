# Generated by Django 4.1.1 on 2022-09-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_photo",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]

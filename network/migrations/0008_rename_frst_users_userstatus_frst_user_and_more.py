# Generated by Django 4.2 on 2023-05-12 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0007_rename_status_userstatus"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userstatus",
            old_name="frst_users",
            new_name="frst_user",
        ),
        migrations.RenameField(
            model_name="userstatus",
            old_name="scnd_users",
            new_name="scnd_user",
        ),
    ]
# Generated by Django 4.2.2 on 2023-08-03 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0002_rename_teammember_members_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='member_email',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]

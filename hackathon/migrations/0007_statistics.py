# Generated by Django 3.2.19 on 2023-08-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0006_alter_members_member_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('called_count', models.PositiveIntegerField(default=0)),
                ('post_called_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]

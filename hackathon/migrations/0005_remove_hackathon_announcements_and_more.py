# Generated by Django 4.2.2 on 2023-08-04 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0004_members_member_register_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hackathon',
            name='announcements',
        ),
        migrations.RemoveField(
            model_name='hackathon',
            name='organizers',
        ),
        migrations.RemoveField(
            model_name='hackathon',
            name='round1_date',
        ),
        migrations.RemoveField(
            model_name='hackathon',
            name='round2_date',
        ),
        migrations.RemoveField(
            model_name='hackathon',
            name='round3_date',
        ),
        migrations.RemoveField(
            model_name='hackathon',
            name='rules_and_guidelines',
        ),
        migrations.AddField(
            model_name='hackathon',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.PositiveIntegerField()),
                ('round_date', models.DateField()),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.hackathon')),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizer_info', models.TextField()),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.hackathon')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement_text', models.TextField()),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.hackathon')),
            ],
        ),
    ]

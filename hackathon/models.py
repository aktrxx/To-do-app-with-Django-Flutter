from django.db import models

class Hackathon(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    registration_start_date = models.DateField()
    registration_end_date = models.DateField()
    contact_number = models.CharField(max_length=20)

class Round(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    round_number = models.PositiveIntegerField()
    round_date = models.DateField()

class Announcement(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    announcement_text = models.TextField()

class Organizer(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    organizer_info = models.TextField()


class Team(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100)

class Members(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=100)
    member_department = models.CharField(max_length=100)
    member_phone = models.CharField(max_length=30)
    member_email = models.CharField(max_length=80)
    member_register_number = models.CharField(max_length=50)


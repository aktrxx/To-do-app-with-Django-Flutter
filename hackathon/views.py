from django.shortcuts import render, redirect
# from .models import Hackathon, Team, TeamMember
# from django.shortcuts import render, redirect
from .models import Hackathon, Team, Members
from django.contrib.admin.views.decorators import user_passes_test, staff_member_required

# hackathon_app/views.py

def registration_view(request):
    if request.method == 'POST':
        hackathon = Hackathon.objects.first()  # Assuming there's at least one hackathon in the database
        team_name = request.POST.get('team_name')

        # Create the team and fetch the team leader data
        team = Team.objects.create(hackathon=hackathon, team_name=team_name)
        team_leader_name = request.POST.get('team_member_1_name')
        team_leader_department = request.POST.get('team_member_1_department')
        team_leader_phone = request.POST.get('team_member_1_phone')
        team_leader_email = request.POST.get('team_member_1_email')
        team_leader_register_number = request.POST.get('team_member_1_register_number')

        # Create the team leader
        Members.objects.create(
            team=team,
            member_name=team_leader_name,
            member_department=team_leader_department,
            member_phone=team_leader_phone,
            member_email=team_leader_email,
            member_register_number=team_leader_register_number
        )

        # Fetch and create team members (if any)
        for i in range(2, 5):
            member_name = request.POST.get(f'team_member_{i}_name')
            if member_name:
                member_department = request.POST.get(f'team_member_{i}_department')
                member_phone = request.POST.get(f'team_member_{i}_phone')
                member_email = request.POST.get(f'team_member_{i}_email')
                member_register_number = request.POST.get(f'team_member_{i}_register_number')
                Members.objects.create(
                    team=team,
                    member_name=member_name,
                    member_department=member_department,
                    member_phone=member_phone,
                    member_email=member_email,
                    member_register_number=member_register_number
                )
            else:
                break

        return redirect('registration_success')

    return render(request, 'registration.html')

def registration_success_view(request):
    return render(request, 'registration_success.html')
# hackathon_app/views.py



# hackathon_app/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hackathon, Team, Members

@api_view(['POST'])
def api_registration_view(request):
    if request.method == 'POST':
        Statistics.increase_post()
        hackathon = Hackathon.objects.first()  # Assuming there's at least one hackathon in the database
        team_name = request.data.get('team_name')

        # Check if team with the given register number already exists
        team_leader_register_number = request.data.get('team_member_1_register_number')
        if Members.objects.filter(member_register_number=team_leader_register_number).exists():
            return Response({'error': 'Team leader with this register number is already registered.'}, status=400)

        # Create the team and fetch the team leader data
        team = Team.objects.create(hackathon=hackathon, team_name=team_name)
        team_leader_name = request.data.get('team_member_1_name')
        team_leader_department = request.data.get('team_member_1_department')
        team_leader_phone = request.data.get('team_member_1_phone')
        team_leader_email = request.data.get('team_member_1_email')
        team_leader_register_number = request.data.get('team_member_1_register_number')

        # Create the team leader
        Members.objects.create(
            team=team,
            member_name=team_leader_name,
            member_department=team_leader_department,
            member_phone=team_leader_phone,
            member_email=team_leader_email,
            member_register_number=team_leader_register_number
        )

        # Fetch and create team members (if any)
        for i in range(2, 5):
            member_name = request.data.get(f'team_member_{i}_name')
            if member_name:
                member_department = request.data.get(f'team_member_{i}_department')
                member_phone = request.data.get(f'team_member_{i}_phone')
                member_email = request.data.get(f'team_member_{i}_email')
                member_register_number = request.data.get(f'team_member_{i}_register_number')

                # Check if team member with the given register number already exists
                if Members.objects.filter(member_register_number=member_register_number).exists():
                    return Response({'error': f'Team member {i-1} with this register number is already registered.'}, status=400)

                Members.objects.create(
                    team=team,
                    member_name=member_name,
                    member_department=member_department,
                    member_phone=member_phone,
                    member_email=member_email,
                    member_register_number=member_register_number
                )
            else:
                break

        return Response({'success': 'Registration successful!'})

    return Response({'error': 'Invalid request method.'}, status=405)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hackathon, Statistics

class HackathonDetailView(APIView):
    def get(self, request):
        try:
            hackathon = Hackathon.objects.first()  # Retrieve the first hackathon
        except Hackathon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data = {
            "name": hackathon.name,
            "start_date": hackathon.start_date,
            "end_date": hackathon.end_date,
            "registration_start_date": hackathon.registration_start_date,
            "registration_end_date": hackathon.registration_end_date,
            "contact_number": hackathon.contact_number,
            "rounds": [],
            "announcements": [],
            "organizers": []
        }

        rounds = hackathon.round_set.all()
        for round in rounds:
            data["rounds"].append({
                "round_number": round.round_number,
                "round_date": round.round_date
            })

        announcements = hackathon.announcement_set.all()
        for announcement in announcements:
            data["announcements"].append({
                "announcement_text": announcement.announcement_text
            })

        organizers = hackathon.organizer_set.all()
        for organizer in organizers:
            data["organizers"].append({
                "organizer_info": organizer.organizer_info
            })
        Statistics.increase()
        return Response(data)



import openpyxl
from django.http import HttpResponse, JsonResponse
# from .models import Team, TeamMember

# hackathon_app/views.py

import openpyxl
from django.http import HttpResponse
from .models import Team, Members


def export_registered_students(request):
    teams = Team.objects.all()

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="registered_students.xlsx"'

    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Write header row
    header = [
        'Team Name', 'Team Leader Name', 'Team Leader Email',
        'Team Leader Department', 'Team Leader Register Number',
        'Team Member 1 Name', 'Team Member 1 Department',
        'Team Member 1 Email', 'Team Member 1 Register Number',
        'Team Member 2 Name', 'Team Member 2 Department',
        'Team Member 2 Email', 'Team Member 2 Register Number',
        'Team Member 3 Name', 'Team Member 3 Department',
        'Team Member 3 Email', 'Team Member 3 Register Number',
    ]
    sheet.append(header)

    for team in teams:
        # Get team leader from the team members
        team_leader = Members.objects.filter(team=team).first()

        # Initialize team data with team leader information
        team_data = [team.team_name]

        if team_leader:
            team_data.extend([
                team_leader.member_name, team_leader.member_email, team_leader.member_department,
                team_leader.member_register_number
            ])
        else:
            team_data.extend(['', '', '', ''])

        # Fetch team members and add them to the team_data list
        team_members = Members.objects.filter(team=team).exclude(pk=team_leader.pk) if team_leader else None
        for i in range(2, 5):  # Assuming a maximum of 3 additional team members
            if team_members and i - 2 < len(team_members):
                member = team_members[i - 2]
                team_data.extend([
                    member.member_name, member.member_department, member.member_email, member.member_register_number
                ])
            else:
                team_data.extend(['', '', '', ''])

        # Append the team_data list as a row in the Excel sheet
        sheet.append(team_data)

    workbook.save(response)
    return response

@staff_member_required
def statistics_json(request):
    # Retrieve the Statistics object
    statistics, _ = Statistics.objects.get_or_create(pk=1)
    data = {
        'GET_req_called_count': statistics.called_count,
        'POST_req_called_count': statistics.post_called_count,
        'POST_saved_count' : 24
    }

    return JsonResponse(data)

@staff_member_required
def statistics_view(request):
    # Retrieve the Statistics object
    statistics, _ = Statistics.objects.get_or_create(pk=1)
    data = {
        'GET_req_called_count': statistics.called_count,
        'POST_req_called_count': statistics.post_called_count,
        'POST_saved_count' : 24
    }

    return Response(data)
from django.shortcuts import render
from .models import Employee, Stack

# Define mock_db data
mock_db = [
    {'id': 1, 'name': 'John', 'surname': 'Doe', 'stack': 'Python', 'team_lead': 'David'},
    {'id': 2, 'name': 'Jane', 'surname': 'Smith', 'stack': 'Java', 'team_lead': 'Joana'},
    {'id': 3, 'name': 'Mike', 'surname': 'Johnson', 'stack': 'JavaScript', 'team_lead': 'Smith'},
    {'id': 4, 'name': 'Emily', 'surname': 'Williams', 'stack': 'C#', 'team_lead': 'Sarah'},
    {'id': 5, 'name': 'Alex', 'surname': 'Brown', 'stack': 'Ruby', 'team_lead': 'Philip'},
    {'id': 6, 'name': 'Sarah', 'surname': 'Miller', 'stack': 'Python', 'team_lead': 'David'},
    {'id': 7, 'name': 'Daniel', 'surname': 'Jones', 'stack': 'Java', 'team_lead': 'Joana'},
    {'id': 8, 'name': 'Sophia', 'surname': 'Davis', 'stack': 'JavaScript', 'team_lead': 'Smith'},
    {'id': 9, 'name': 'Matthew', 'surname': 'Garcia', 'stack': 'C#', 'team_lead': 'Sarah'},
    {'id': 10, 'name': 'Olivia', 'surname': 'Martinez', 'stack': 'Ruby', 'team_lead': 'Philip'},
]

def employees(request):
    employees = []

    for employee in mock_db:
        employees.append({
            'id': employee['id'],
            'name': employee['name'],
            'surname': employee['surname'],
            'stack': employee['stack'],
            'team_lead': employee['team_lead']
        })

    return render(request, 'employees.html', {'employees': employees})


def stacks(request):
    stacks_set = set()
    stacks = []

    for employee in mock_db:
        if employee['stack'] not in stacks_set:
            stacks_set.add(employee['stack'])
            stacks.append({
                'name': employee['stack']
            })

    return render(request, 'stacks.html', {'stacks': stacks})

def team_leads(request):
    team_leads_set = set()
    team_leads = []

    for employee in mock_db:
        if employee['team_lead'] not in team_leads_set:
            team_leads_set.add(employee['team_lead'])
            team_leads.append({
                'name': employee['team_lead'], 
                'stack': employee['stack']
            })

    return render(request, 'team_leads.html', {'team_leads': team_leads})

def home(request):
    return render(request, 'home.html')

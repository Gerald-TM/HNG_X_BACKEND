from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.contrib import messages
import json

# Create your views here.


def get_endpoint_view(request):
    slack_name = request.GET.get("slack_name")
    track = request.GET.get("track")

    if slack_name == 'gerald__tm' and track == 'backend':

        current_day = datetime.now().strftime('%A')
        utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

        response_data = {
            'slack_name': slack_name,
            'current_day': current_day,
            'utc_time': utc_time,
            'track': track,
            'github_file_url': 'https://www.google.com',
            'github_repo_url': 'https://www.google.com',
            'status': 200,

        }

        return HttpResponse('\t\tHNG_X Task: Create and host an endpoint.\n\n' + json.dumps(response_data, indent=3), content_type="application/json")

    else:
        response_data = {
            'Error': "You have to pass in GET query parameters 'slack_name' and 'track' e.g URL?slack_name=your_slack_name&track=your_track"
        }

        return HttpResponse(json.dumps(response_data, indent=3), content_type="application/json")

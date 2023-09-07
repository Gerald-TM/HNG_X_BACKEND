from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.contrib import messages
import json

# Create your views here.


def get_endpoint_view(request):
    # The GET request query parameters; slack_name and track
    slack_name = request.GET.get("slack_name")
    track = request.GET.get("track")

    # validate the GET query parameters for slack_name and track.
    if slack_name == 'gerald__tm' and track == 'backend':

        # Current day of the week.
        current_day = datetime.utcnow().strftime("%A")

        # Current UTC time (with validation of +/-2)
        utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

        # Response data in the form of a python dictionary
        response_data = {
            'slack_name': slack_name,
            'current_day': current_day,
            'utc_time': utc_time,
            'track': track,
            'github_file_url': 'https://github.com/Gerald-TM/HNG_X_BACKEND/blob/main/endpoint/views.py',
            'github_repo_url': 'https://github.com/Gerald-TM/HNG_X_BACKEND',
            'status': 200,

        }

        # Convert the python dictionary to a JSON formatted string and return the data as a regular HttpResponse.
        return HttpResponse('\t\tHosted endpoint taking in two GET request query parameter, and returning specific information in JSON format.\n\n' +
                             json.dumps(response_data, indent=3), content_type="application/json")

    else:
        # Return an error if the GET request query parameters fail to be validated or correct.
        response_data = {
            'Error': "You have to pass in GET query parameters 'slack_name' and 'track' e.g URL?slack_name=your_slack_name&track=your_track"
        }

        # Return the error message as HttpResponse of a JSON formatted string.
        return HttpResponse(json.dumps(response_data, indent=3), content_type="application/json")

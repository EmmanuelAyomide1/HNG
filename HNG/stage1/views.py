from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
# Create your views here.
def Jsonresp(request):
    slack_name = request.GET.get('slack_name')
    track=request.GET.get('track')
    day,utc_time=datetime.utcnow().strftime("%A %Y-%m-%DT:%M:%SZ").split()
    return JsonResponse({"slack_name":slack_name,
            "current_day":day,
            "utc_time":utc_time,
            "track":track,
            "github_repo_url":"https://github.com/EmmanuelAyomide1/HNG",
            "github_file_url":"https://github.com/EmmanuelAyomide1/HNG/tree/main/HNG",
            "status-code":200})


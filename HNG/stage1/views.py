from datetime import datetime
from django.http import JsonResponse
# Create your views here.
def Jsonresp(request):
    slack_name = request.GET.get('slack_name')
    track=request.GET.get('track')
    day,utc_time=datetime.utcnow().strftime("%A %Y-%m-%dT%H:%M:%SZ").split()
    return JsonResponse({"slack_name":slack_name,
            "current_day":day,
            "utc_time":utc_time,
            "track":track,
            "github_file_url":"https://github.com/EmmanuelAyomide1/HNG/blob/main/HNG/manage.py",
            "github_repo_url":"https://github.com/EmmanuelAyomide1/HNG",
            "status-code":200})

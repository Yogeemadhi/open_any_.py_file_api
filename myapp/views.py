from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess


# Create your views here.

def home(request):
    return render(request,"home.html")


@csrf_exempt
def run_script(request):
    if request.method == 'POST':
        # Get the path of the .py file from the request
        path = request.POST.get('path')
        
        # Run the file using subprocess
        result = subprocess.run(['python', path], stdout=subprocess.PIPE)
        
        # Return the output as a JSON response
        return JsonResponse({'output': result.stdout.decode()})
    else:
        # Return an error message if the request is not a POST request
        return JsonResponse({'error': 'Invalid request method'})

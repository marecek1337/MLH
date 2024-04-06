from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import os

# Assuming your script is named 'evaluate_assignment_script.py' and is in the same directory as your views.py
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'script/evaluate.py')

@require_http_methods(["POST"])
@csrf_exempt
def evaluate_assignment(request):
    try:
        data = json.loads(request.body)
        description = data['description']
        max_score = data['maxScore']
    except (KeyError, json.JSONDecodeError) as e:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    
    # Sanitize inputs if necessary before using in os.system or consider using subprocess with proper argument handling
    command = f'python {SCRIPT_PATH} "{description}" "{max_score}"'
    
    os.system(command)
    
    # Since os.system does not capture output, this is just a placeholder response
    return JsonResponse({'status': 'Script executed'})

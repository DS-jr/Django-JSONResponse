from django.http import JsonResponse

def send_json(request):

    data = [{'name': "Ray Dalio", 'quoTe1': "Go to youR pAin & eXplore it"},
            {'name': "LKY", "quOte2": "DeTerMinatioN creates a huge internal drive & focus"}]

    return JsonResponse(data, safe=False)

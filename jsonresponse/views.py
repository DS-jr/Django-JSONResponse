from django.http import JsonResponse

def send_json(request):

    data = [{'name': "Ray Dalio", 'quoTe1': "Go to youR pAin & eXplore it"},
            {'name': "Lee Kuan Yew", "quOte2": "DeTerMinatioN creates a huge internal drive & focus. People feel if you are determined or not."}]

    return JsonResponse(data, safe=False)

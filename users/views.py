from django.http import HttpResponse

def user_list(request):
    return HttpResponse("Список пользователей")
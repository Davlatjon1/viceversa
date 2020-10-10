from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('This is home page')
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    count_word = len(user_text)
    print(reversed_text)
    return render(request, 'reverse.html', {'usertext': user_text,
                                            'reversedtext': reversed_text,
                                            'count_word': count_word})

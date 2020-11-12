from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {'wellcome':'Good time to say wellcome'})

def reverse(request):
	text = request.GET['usertext']
	txt = text[::-1]
	len_value = len(text.split())
	return render(request, 'reverse.html', {'usertext':text, 'reversedtext':txt, 'lentext':len_value})

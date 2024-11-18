import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse

def post_list(request):
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    posts = response.json()

    context = {
        'posts': posts,
    }
    return render(request, 'posts/post_list.html', context)

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        data = {
            'title': title,
            'body': body,
            'userId': 1,
        }
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
        if response.status_code == 201:
            return redirect('post_list')
        else:
            return JsonResponse({'error': 'Failed to create post'}, status=400)

    return render(request, 'posts/post_create.html')

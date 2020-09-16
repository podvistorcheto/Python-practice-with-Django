from django.shortcuts import render

posts = [
    {
        'author': 'Niall Ferguson',
        'title': 'The Square and The Tower',
        'content': 'History of The Social Networks',
        'date_posted': 'March 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Second Blog II',
        'content': 'Posted Content',
        'date_posted': 'August 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

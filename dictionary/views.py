from django.shortcuts import render


def article(request):
    return render(
        request,
        "dictionary/article.html",
        {}
    )

def home(request):
    return render(
        request,
        "dictionary/home.html",
        {}
    )

def book(request):
    return render(
        request,
        "dictionary/booktable.html",
        {}
    )

def society(request):
    return render(
        request,
        "dictionary/society.html",
        {}
    )

def qna(request):
    return render(
        request,
        "dictionary/qna.html",
        {}
    )
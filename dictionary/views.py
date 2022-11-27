from django.shortcuts import render, redirect
from dictionary.forms import PostForm, CommentForm, DonateForm
from django.contrib.auth.decorators import login_required
from . import models
from dictionary.models import Post, Post_Comment, Dictionganada, Article
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
def article(request):
    art_all = Article.objects.all()
    return render(
        request,
        "dictionary/article.html",
        {'art_all': art_all}
    )


@method_decorator(csrf_exempt, name="dispatch")
def home(request):
    return render(
        request,
        "dictionary/home.html",
        {}
    )


from django.http import JsonResponse
import json


@method_decorator(csrf_exempt, name="dispatch")
def book(request):
    if request.method == "POST":
        data = json.loads(request.body)
        book_all = Dictionganada.objects.filter(lang_initial='니은')
    else:
        book_all = Dictionganada.objects.filter(lang_initial='기역')
    return render(
        request,
        "dictionary/booktable.html",
        {'book_all': book_all}
    )


@method_decorator(csrf_exempt, name="dispatch")
def society(request):
    post_all = Post.objects.all()
    return render(
        request,
        "dictionary/society.html",
        {'post_all': post_all}
    )


@method_decorator(csrf_exempt, name="dispatch")
@login_required  # 함수위에 씌워주면 로그인시에만 확인 가능
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post = form.save()
            redirect_url = f"/dictionary/society/"
            return redirect(redirect_url)
    else:
        form = PostForm()
    return render(
        request,
        "dictionary/new_post.html",
        {'form': form})


@method_decorator(csrf_exempt, name="dispatch")
def single_post(request, pk):
    post = Post.objects.get(id=pk)
    comment = Post_Comment.objects.filter(post_id=pk)
    comment_form = CommentForm
    return render(
        request,
        "dictionary/single_post.html",
        {'post': post, 'commentform': comment_form, 'comment_list': comment}
    )


@method_decorator(csrf_exempt, name="dispatch")
@login_required  # 함수위에 씌워주면 로그인시에만 확인 가능
def post_comment(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            redirect_url = "/dictionary/society/{}".format(pk)
            return redirect(redirect_url)
    else:
        form = CommentForm()
    return render(
        request,
        "dictionary/new_comment.html",
        {
            "form": form,
        },
    )


@method_decorator(csrf_exempt, name="dispatch")
@login_required
def donate(request):
    if request.method == "POST":
        filename = request.POST["lang_name"]
        filetext = request.POST['lang_text']
        user = request.user
        uploadedFile = request.FILES["donate_video"]

        document = models.SignDonate(
            lang_name=filename,
            lang_text=filetext,
            user=user,
            donate_video=uploadedFile
        )
        document.save()
        redirect_url = "/dictionary/home"
        return redirect(redirect_url)

    return render(
        request,
        "dictionary/donate.html",
        {})


@method_decorator(csrf_exempt, name="dispatch")
def test(request):
    return render(
        request,
        "dictionary/test.html",
        {}
    )

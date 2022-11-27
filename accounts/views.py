from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from accounts.forms import SignupForm, UsereditForm
from accounts.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from dictionary.models import Post, SignDonate

login = LoginView.as_view(
    template_name="accounts/login_form.html",
    next_page="/dictionary/home"
)

logout = LogoutView.as_view(next_page="/dictionary/home")


@method_decorator(csrf_exempt, name="dispatch")
@login_required  # 함수위에 씌워주면 로그인시에만 확인 가능
def profile(request):
    user = request.user
    user_name = request.user.username
    post_all = Post.objects.filter(user=request.user)
    donate_all = SignDonate.objects.filter(user=request.user)

    return render(
        request,
        "accounts/profile.html",
        {
            "user": user, 'post_all': post_all, 'donate_all': donate_all
        },
    )


signup = CreateView.as_view(
    form_class=SignupForm,
    success_url="/accounts/login/",  # 회원가입시 login화면으로 ㄱㄱ
    template_name="accounts/signup_form.html",
)

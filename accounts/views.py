from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from accounts.forms import SignupForm, UsereditForm
from accounts.models import User

login = LoginView.as_view(
    template_name="accounts/login_form.html",
)

logout = LogoutView.as_view(next_page="/recommand/")


@login_required  # 함수위에 씌워주면 로그인시에만 확인 가능
def profile(request):
    user = request.user
    user_name = request.user.username

    return render(
        request,
        "accounts/profile.html",
        {
            "user": user,
        },
    )


signup = CreateView.as_view(
    form_class=SignupForm,
    success_url="/accounts/login/",  # 회원가입시 login화면으로 ㄱㄱ
    template_name="accounts/signup_form.html",
)

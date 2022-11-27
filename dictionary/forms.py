from django import forms
from dictionary.models import Post, Post_Comment, SignDonate


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["post_name", 'post_text']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Post_Comment
        # 유저에게 입력받은 field만
        fields = ["comment"]


class DonateForm(forms.ModelForm):
    class Meta:
        model = SignDonate
        fields = ["lang_name", 'lang_text', 'donate_video']
from django import forms

from blog.models import CommentModel


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('name', 'email', 'phone', 'comment')

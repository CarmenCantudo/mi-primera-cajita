from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import News


class NewsForm(forms.ModelForm):
    """
    News Articles Form
    """
    class Meta:
        model = News
        fields = [
            "title",
            "content",
            "image",
        ]

        widgets = {
            'content': SummernoteWidget(),
        }

        def __init__(self, *args, **kwargs):
            super(NewsForm, self).__init__(*args, **kwargs)

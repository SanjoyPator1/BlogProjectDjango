from django import forms
from .models import Post, Category, Privacy

# summernote
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField



# Collecting category choices from database
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

# Collecting privacy choices from database
choices_privacy = Privacy.objects.all().values_list('name', 'name')

choice_list_privacy = []

for item in choices_privacy:
    choice_list_privacy.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author',
                  'category', 'privacy', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'title_tag': forms.TextInput(attrs={'class': 'form-control', 'value': 'titletag', 'type': 'hidden'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'privacy': forms.Select(choices=choice_list_privacy, attrs={'class': 'form-control'}),
            #            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'body':  SummernoteWidget(),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    # body = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ('title', 'category', 'privacy',
                  'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control input-sm'}),
            # 'title_tag': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'privacy': forms.Select(choices=choice_list_privacy, attrs={'class': 'form-control'}),

            'body':  SummernoteWidget(),
            # 'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),

        }

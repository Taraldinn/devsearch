from django.forms import ModelForm
from tinymce.widgets import TinyMCE
from  crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field , HTML , Submit
from .models import Project
from django import forms


class ProjectForm(ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'demo_link', 'source_link', 'tags']

        widgets = {'tags': forms.CheckboxSelectMultiple()}

    def __int__(self, *args, **kwargs):
        super(ProjectForm,self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'input_title'})

from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post
class PostCreateForm(forms.ModelForm):
	content=forms.CharField(widget=PagedownWidget(show_preview=False))
	class Meta:
		model=Post
		fields=['title','description','content','image']
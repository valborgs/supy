from django import forms

from .models import Post, FileUpload

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        
        
class FileUploadForm(forms.ModelForm):

    class Meta:
        model = FileUpload
        fields = ('title', 'imgfile', 'memo')
from django import forms
from django.contrib.auth.models import User
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        
    def clean_title(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"\"{title}\" is already used. Please pick another title.")
        return title  # Return only the title, not the entire data dictionary







# class ArticleFormOld(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()
    
    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get("title")
    #     if title.lower().strip() == "Django Class": 
    #         raise forms.ValidationError("This title is taken.")
    #     return title

    # def clean_content(self):
    #     cleaned_data = self.cleaned_data
    #     content = cleaned_data.get("content")
    #     return content
    
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get("title")
    #     content = cleaned_data.get("content")
    #     if title.lower().strip() == "Django Class":
    #         self.add_error("title", "This title is taken.")

    #     if "Django" in content or "Django" in title.lower():
    #         self.add_error("content", "Content cannot contain the word 'Django'.")
    #         raise forms.ValidationError("Content cannot contain the word 'Django'.")
    #     return cleaned_data
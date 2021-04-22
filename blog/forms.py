from django import forms


class CommentForm(forms.Form):
    com_cont = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return f"{self.comment_text} by User"


class SearchForm(forms.Form):
    title = forms.CharField(max_length=20)

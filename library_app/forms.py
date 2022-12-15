from django import forms
from .models import Book

class BorrowBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['borrower']
        widgets = {'borrower': forms.HiddenInput()}

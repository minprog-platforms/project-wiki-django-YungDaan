from django import forms

class newpage(forms.Form):
    pagename = forms.CharField (label = "title", required =  True, widget = forms.TextInput
    (attrs = {'placeholder' : 'title', 'classs' : 'col-sm-10', 'style' : 'bottom:1rem'}))
    body = forms.CharField(label = 'Markdown', required = False, widget = forms.Textarea
    (attrs = {'placeholder' : 'markdown', 'class' : 'col-sm-10', 'style' : 'top:1rem'}))

class newsearch(forms.Form):
    search = forms.CharField(label = 'search', required = False, widget = forms.TextInput
    (attrs = {'placeholder' : 'search'}))

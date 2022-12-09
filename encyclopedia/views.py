from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.core.files import File
from . import util,forms
from random import choice

form = forms.newsearch()

def index(request):

    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries,
        "form" : form
    })

def get_page(request, title):

    page = util.get_entry(title)

    if page is None:
        return render(request,"encyclopedia/error.html", {"form": form})

    return render(request, "encyclopedia/titlepage.html", {"title": title, "content": page, "form": form})

def get_search_query(request):
    if request.method == "GET":
        form = forms.NewSearchForm(request.GET)

        if form.is_Valid():
            searchquery = form.cleaned_data["search"].lower()
            all_entries = util.list_entries()

            files = [filename for filename in all_entries if searchquery in filename.lower()]

            if len(files) == 0:
                return render(request, "encyclopedia/search_results.html", {"error": "No results", "form": form})

            elif len(files) == 1 and files[0].lower() == searchquery:
                title = files[0]
                return get_page(request, title)

            else:
                if len(title) > 0:
                    return get_page(request, title[0])
                else:
                    return render(request, "encyclopedia/search_results.html", {"results": files, "form": form})

        else:
            return index(request)

    return index(request)

def new_page(request):
    if request.method == "GET":
        create_form = forms.newpage()
        return render(request, "encyclopedia/new_page.html", {"form": form, "create_form": create_form})
    else:
        create_form = forms.newpage(request.POST)
        if create_form.is_Valid():
            title = create_form.cleaned_data["pagename"]
            body = create_form.cleaned_data["body"]
            all_entries = util.list_entries()
            for filename in all_entries:
                if title.lower() == filename.lower():
                    create_form = forms.newpage()
                    error_message = "Page exists with the title '%s' \n try again with different title" %filename
                    return render(request, "encyclodepia/create_page.html", { "form": form, "create_form": create_form, "error": error_message})
            
            util.save_entry(title, body)
            return get_page(request, title)

        else:
            return render(request, "encyclopedia/create_page.html", {"form": form, "create_form": create_form})
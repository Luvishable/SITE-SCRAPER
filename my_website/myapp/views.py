from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link

# Create your views here.

def scrape(request):

    if request.method == "POST":
        # remember! the name of the 'id' and the 'name' attributes in the input field is site!!
        site = request.POST.get("site", "")

        # Getting the page
        page = requests.get("https://www.google.com")

        # Getting the html of the page
        soup = BeautifulSoup(page.text, "html.parser")

        for link in soup.find_all("a"):
            link_address = link.get("href")
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)

        return HttpResponseRedirect("/")

    else:
        data = Link.objects.all()

    # Render the result.html and give the html context which is the last parameter of the render method
    return render(request, "myapp/result.html", {"data": data})

def clear(request):
    Link.objects.all().delete()
    return render(request, "myapp/result.html")





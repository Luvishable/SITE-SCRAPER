from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.

def scrape(request):

    # Getting the page
    page = requests.get("https://www.google.com")

    # Getting the html of the page
    soup = BeautifulSoup(page.text, "html.parser")

    link_addresses = []
    for link in soup.find_all("a"):

        # Adding the contents of the href attributes into the list
        link_addresses.append(link.get("href"))

    # Render the result.html and give the html context which is the last parameter of the render method
    return render(request, "myapp/result.html", {"link_addresses": link_addresses})






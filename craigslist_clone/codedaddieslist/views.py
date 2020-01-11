import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from . import models
# Create your views here.

BASE_CRAIGSLIST_URL = 'https://pune.craigslist.org/search/?query={}'

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search)) 
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('a',{'class': 'result-title'})

    final_postings = []
    
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if(pos.find(class_='result-price')):
            post_price = pos.find(class_='result-price').text
        else:
            post_price = 'N/A'
        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
            print(post_image_url)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'

        
        final_postings.append((post_title, post_url, post_price, post_image_url))

    context = {
        'search':search,
        'final_postings': final_postings,
    }
    return render(request, 'codedaddieslist/new_search.html', context)
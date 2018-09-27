from django.shortcuts import render
from django.http import HttpResponse

import json
from .form import urlForm
import feedparser

def reader(request):

    form = urlForm(request.GET)
    if form.is_valid():
        url = form.cleaned_data['urlField']
        feeds = feedparser.parse(url)
        feed_list = []
        feed_list.append(feeds['feed']['title'])
        print (feed_list)
        for i in range(0,len(feeds['entries'])):
            feed_list.append([feeds['entries'][i]['title'], feeds['entries'][i]['summary'], feeds['entries'][i]['id']])
        return HttpResponse(json.dumps({"feed" : feed_list}))
    return render(request, "home.html", {"form" : form})

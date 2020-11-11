from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt
from django.http import HttpResponse, Http404
from .models import Article, Editor, tags

# Create your views here.
def news_today(request):
    date=dt.datetime.today()
    news=Article.todays_news()
    return render(request, 'all-news/today-news.html', {"date": date,"news":news})
    
def convert_dates(dates):
    day_number=dt.date.weekday(dates)
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day=days[day_number]
    return day


def news_of_day(request):
    date=dt.date.today()
    day=convert_dates(date)
    return render(request, 'all-news/today-news.html', {"date": date,})

def past_days_news(request, past_date):
    try:
        date=dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except:
        raise Http404()

    date=dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    day=convert_dates(date)
    if date==dt.datetime.today():
        return redirect(news_of_day)

    news= Article.days_news(date)
    return render(request,  'all-news/past-news.html', {"date": date, "news":news})

def searchResults(request):
    if 'article' in request.GET and request.GET['article']:
        searchTerm=request.GET.get('article')
        searchedArticles=Article.search_by_title(searchTerm)
        message=f"{searchTerm}"
        return render(request, 'all-news/search.html',{"message":message,"articles": searchedArticles})
    else:
        message= "You haven't searched for any term"

        return render(request, 'all-news/search.html', {"message":message})

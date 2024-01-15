from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


monthly_challenges = {
    "january":"Eat no meat for the entire month!",
    "february":"Walk for at least 20 minutes every day!",
    "march":"Learn Django for at least 20 minutes every day!",
    "april":"Eat no meat for the entire month!",
    "may":"Walk for at least 20 minutes every day!",
    "june":"Learn Django for at least 20 minutes every day!",
    "july":"Eat no meat for the entire month!",
    "august":"Learn Django for at least 20 minutes every day!",
    "september":"Walk for at least 20 minutes every day!",
    "october":"Learn Django for at least 20 minutes every day!",
    "november":"Eat no meat for the entire month!",
    "december": "Learn Django for at least 20 minutes every day!"
}

def index(request):
    # list_item = ''
    months = list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        "months":months
    })



def months_challenges_by_number(request,month):
        months = list(monthly_challenges.keys())
        if month > len(monthly_challenges):
            return HttpResponseNotFound('Invalid month')
        month_redirect = months[month-1]
        redirect_path = reverse("month-challenge",args = [month_redirect])
        return HttpResponseRedirect(redirect_path)
    
def months_challenges(request,month):
    #  try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html",{
            "text":challenge_text,
            "month":month
        })
    #  except:
        error_page = render_to_string("404.html")
        return HttpResponseNotFound(error_page)
   
    
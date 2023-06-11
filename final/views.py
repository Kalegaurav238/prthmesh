from django.shortcuts import render
from django.http import HttpResponse
import joblib


def home(request):
    return render(request, "home.html")


def result(request):

    classifier = joblib.load('finalized_stack_model.sav')

    lis = []



    lis.append(int(request.GET['Enter Age']))
    lis.append(int(request.GET['Gender']))
    lis.append(int(request.GET['Enter cp']))
    lis.append(int(request.GET['Enter trestbps']))
    lis.append(int(request.GET['Enter chol']))
    lis.append(int(request.GET['Enter fbs']))
    lis.append(int(request.GET['Enter restecg']))
    lis.append(int(request.GET['Enter thalach']))
    lis.append(int(request.GET['Enter exang']))
    lis.append(int(request.GET['Enter oldpeak']))
    lis.append(int(request.GET['Enter slope']))
    lis.append(int(request.GET['Enter ca']))
    lis.append(int(request.GET['Enter thal']))

    ans = classifier.predict([lis])
    #a = int(request.GET['Gender'])
    #print("gender is : "+str(a))
    fans=""
    
    if(ans==0):
        fans="negative"
    else:
        fans="positive"
    return render(request, "result.html", {'ans': fans})

    

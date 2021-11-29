from django.shortcuts import render
from django.http import HttpResponse
import pickle


file=open('G:\covid detector\model.pkl','rb')
model=pickle.load(file)
file.close()

def vik(request):
    s="working web"
    return render(request,'home.html')

def result(request):
    # if request.method=="GET":
        fever = int(request.GET["fever"])
        age = int(request.GET["age"])
        pain = int(request.GET["pain"])
        runnyNose = int(request.GET["runnyNose"])
        diffBreath = int(request.GET["diffBreath"])
        # Code for inference
        inputFeatures = [fever, pain, age, runnyNose, diffBreath]
        infProb =model.predict([inputFeatures])
        s=infProb*100
        return render(request,'result.html',{'s':s})
    # else:
    #     return render(request,'home.html')

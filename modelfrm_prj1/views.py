from django.contrib import messages
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics




def homefunction(request):
    return render(request, "index.html")


def userreg(request):
    if request.method == 'POST':
        Aadhar = request.POST['Aadhar']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password,email=Aadhar, first_name=first_name, last_name=last_name)
        user.save()
        print("user created")
        return redirect('login')
    else:
        return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, "login.html")
def mainhome(request):
    return render(request, "home.html")

def agriculturefunction(request):
    return render(request, "agriculture.html")


def aquaculturefunction(request):
    return render(request, "aquacluture.html")

def timeline(request):
    return render(request, "timeline.html")






def agriEquipmentfunction(request):
    return render(request, "AgriEquipment.html")


def agriseedsfunction(request):
    return render(request, "AgriSeeds.html")


def agriirrigationfunction(request):
    return render(request, "AgriIrrigation.html")
def aquaEquipmentfunction(request):
    return render(request, "aquaEquipment.html")
def aquaWaterfunction(request):
    return render(request, "aquaWater.html")
def agriOrganicfunction(request):
    return render(request, "agriOrganic.html")
def agriInOrganicfunction(request):
    return render(request, "agriInOrganic.html")
def agriAgricultureWastefunction(request):
    return render(request, "organicAgricultureWaste.html")
def agriIndutrialWastefunction(request):
    return render(request, "organicIndutrialWaste.html")
def agriLivestockfunction(request):
    return render(request, "organicLivestock.html")
def agriMunicipalSludgefunction(request):
    return render(request, "organicMunicipalSludge.html")
def agriSoilfunction(request):
    return render(request, "agriSoil.html")
def aquaFreshfunction(request):
    return render(request, "aquaFresh.html")
def aquaLakefunction(request):
    return render(request, "aquaLake.html")
def aquaResevoirfunction(request):
    return render(request, "aquaResevoir.html")
def aquaStreamfunction(request):
    return render(request, "aquaStream.html")
def agriweatherfunction(request):
    return render(request, "agriweather.html")
def aquafertilizersfunction(request):
    return render(request, "aquafertilizers.html")

def predict(request):
    return render(request, "pedict.html")

def result(request):
    data = pd.read_csv(r"C:\Users\bhava\Desktop\sdp 2\state_wise_crop_success.csv")
    X = data.drop('crop_success', axis=1)
    Y = data['crop_success']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
    model = LinearRegression()
    model.fit(X_train, Y_train)

    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])


    pred = model.predict(np.array([var1, var2]).reshape(1,- 1))

    price ="The sucess rate is " + str(pred)




    return render(request,"pedict.html",{"result2":price})
def team(request):
    return render(request, "team.html")
def team1(request):
    return render(request, "teammain.html")
def fertilizer(request):
    return render(request, "crop.html")

def showdata(request):
    #return render(request, 'hello.html')
    from modelfrm_prj.app.models import Fertilizer
    data = Fertilizer.objects.all()
    return render(request, 'crop.html',{'data':data})

def predictfertilizer(request):
    form='Select The Option'
    if request.method == 'POST':
        soil = request.POST['soil']
        Crop = request.POST['Crop']
        WaterAvailability = request.POST['WaterAvailability']
        farmers=[['Alluvialsoil','Rice','low','alkaline'],
                 ['Alluvialsoil','Rice','High','iron'],
                 ['Alluvialsoil', 'wheat', 'High', 'NPKM '],
                 ['Alluvialsoil', 'wheat', 'low', 'iron'],
                 ['Alluvialsoil', 'millets', 'High', 'not suitable for the soil'],
                 ['Alluvialsoil', 'millets', 'low', 'not suitable for the soil'],
                 ['Alluvialsoil', 'sugarcane', 'High', 'iron'],
                 ['Alluvialsoil', 'sugarcane', 'low', 'NPKM '],
                 ['Alluvialsoil', 'groundnut', 'High', 'Nitrogen'],
                 ['Alluvialsoil', 'groundnut', 'low', 'iron'],
                 ['Alluvialsoil', 'coffee', 'High', 'iron'],
                 ['Alluvialsoil', 'coffee', 'low', 'Nitrogen'],
                 ['Alluvialsoil', 'maize', 'High', 'iron'],
                 ['Alluvialsoil', 'maize', 'low', 'NPKM '],
                 ['Alluvialsoil', 'pulses', 'High', 'Nitrogen'],
                 ['Alluvialsoil', 'pulses', 'low', 'iron'],
                 ['Alluvialsoil', 'cotton', 'High', 'phosphorus'],
                 ['Alluvialsoil', 'cotton', 'low', 'Azophos'],
                 ['blacksoil', 'Rice', 'low', 'alkaline'],
                 ['blacksoil', 'Rice', 'High', 'iron'],
                 ['blacksoil', 'wheat', 'High', 'potassium '],
                 ['blacksoil', 'wheat', 'low', 'iron'],
                 ['blacksoil', 'millets', 'High', 'not suitable for the soil'],
                 ['blacksoil', 'millets', 'low', 'not suitable for the soil'],
                 ['blacksoil', 'sugarcane', 'High', 'iron'],
                 ['blacksoil', 'sugarcane', 'low', 'potassium '],
                 ['blacksoil', 'groundnut', 'High', 'Nitrogen'],
                 ['blacksoil', 'groundnut', 'low', 'iron'],
                 ['blacksoil', 'coffee', 'High', 'zinc'],
                 ['blacksoil', 'coffee', 'low', 'Nitrogen'],
                 ['blacksoil', 'maize', 'High', 'iron'],
                 ['blacksoil', 'maize', 'low', 'not suitable for the soil '],
                 ['blacksoil', 'pulses', 'High', 'Nitrogen'],
                 ['blacksoil', 'pulses', 'low', 'iron'],
                 ['blacksoil', 'cotton', 'High', 'not suitable for the soil'],
                 ['blacksoil', 'cotton', 'low', 'Azophos'],
                 ['RedandYeallowsoil', 'Rice', 'low', 'alkaline'],
                 ['RedandYeallowsoil', 'Rice', 'High', 'Azophos'],
                 ['RedandYeallowsoil', 'wheat', 'High', 'potassium '],
                 ['RedandYeallowsoil', 'wheat', 'low', 'iron'],
                 ['RedandYeallowsoil', 'millets', 'High', 'not suitable for the soil'],
                 ['RedandYeallowsoil', 'millets', 'low', 'zinc'],
                 ['RedandYeallowsoil', 'sugarcane', 'High', 'iron'],
                 ['RedandYeallowsoil', 'sugarcane', 'low', 'Azophos '],
                 ['RedandYeallowsoil', 'groundnut', 'High', 'Nitrogen'],
                 ['RedandYeallowsoil', 'groundnut', 'low', 'iron'],
                 ['RedandYeallowsoil', 'coffee', 'High', 'zinc'],
                 ['RedandYeallowsoil', 'coffee', 'low', 'Nitrogen'],
                 ['RedandYeallowsoil', 'maize', 'High', 'iron'],
                 ['RedandYeallowsoil', 'maize', 'low', 'not suitable for the soil '],
                 ['RedandYeallowsoil', 'pulses', 'High', 'Azophos'],
                 ['RedandYeallowsoil', 'pulses', 'low', 'iron'],
                 ['RedandYeallowsoil', 'cotton', 'High', 'not suitable for the soil'],
                 ['RedandYeallowsoil', 'cotton', 'low', 'Azophos'],
                 ['Lateritesoil', 'Rice', 'low', 'alkaline'],
                 ['Lateritesoil', 'Rice', 'High', 'Azophos'],
                 ['Lateritesoil', 'wheat', 'High', 'potassium '],
                 ['Lateritesoil', 'wheat', 'low', 'iron'],
                 ['Lateritesoil', 'millets', 'High', 'not suitable for the soil'],
                 ['Lateritesoil', 'millets', 'low', 'not suitable for the soil'],
                 ['Lateritesoil', 'sugarcane', 'High', 'iron'],
                 ['Lateritesoil', 'sugarcane', 'low', 'Azophos '],
                 ['Lateritesoil', 'groundnut', 'High', 'Nitrogen'],
                 ['Lateritesoil', 'groundnut', 'low', 'iron'],
                 ['Lateritesoil', 'coffee', 'High', 'iron'],
                 ['Lateritesoil', 'coffee', 'low', 'Nitrogen'],
                 ['Lateritesoil', 'maize', 'High', 'iron'],
                 ['Lateritesoil', 'maize', 'low', 'not suitable for the soil '],
                 ['Lateritesoil', 'pulses', 'High', 'Azophos'],
                 ['Lateritesoil', 'pulses', 'low', 'iron'],
                 ['Lateritesoil', 'cotton', 'High', 'not suitable for the soil'],
                 ['Lateritesoil', 'cotton', 'low', 'Azophos'],
                 ['Aridsoil', 'Rice', 'low', 'alkaline'],
                 ['Aridsoil', 'Rice', 'High', 'magnesium'],
                 ['Aridsoil', 'wheat', 'High', 'potassium '],
                 ['Aridsoil', 'wheat', 'low', 'iron'],
                 ['Aridsoil', 'millets', 'High', 'ammonium sulphate'],
                 ['Aridsoil', 'millets', 'low', 'urea'],
                 ['Aridsoil', 'sugarcane', 'High', 'iron'],
                 ['Aridsoil', 'sugarcane', 'low', 'magnesium '],
                 ['Aridsoil', 'groundnut', 'High', 'Nitrogen'],
                 ['Aridsoil', 'groundnut', 'low', 'iron'],
                 ['Aridsoil', 'coffee', 'High', 'iron'],
                 ['Aridsoil', 'coffee', 'low', 'Nitrogen'],
                 ['Aridsoil', 'maize', 'High', 'iron'],
                 ['Aridsoil', 'maize', 'low', 'ammonium sulphate '],
                 ['Aridsoil', 'pulses', 'High', 'magnesium'],
                 ['Aridsoil', 'pulses', 'low', 'iron'],
                 ['Aridsoil', 'cotton', 'High', 'ammonium sulphate'],
                 ['Aridsoil', 'cotton', 'low', 'magnesium'],
                 ['Salinesoil', 'Rice', 'low', 'alkaline'],
                 ['Salinesoil', 'Rice', 'High', 'magnesium'],
                 ['Salinesoil', 'wheat', 'High', 'not suitable for the soil '],
                 ['Salinesoil', 'wheat', 'low', 'iron'],
                 ['Salinesoil', 'millets', 'High', 'ammonium sulphate'],
                 ['Salinesoil', 'millets', 'low', 'zinc'],
                 ['Salinesoil', 'sugarcane', 'High', 'iron'],
                 ['Salinesoil', 'sugarcane', 'low', 'magnesium '],
                 ['Salinesoil', 'groundnut', 'High', 'Nitrogen'],
                 ['Salinesoil', 'groundnut', 'low', 'iron'],
                 ['Salinesoil', 'coffee', 'High', 'calcium'],
                 ['Salinesoil', 'coffee', 'low', 'Nitrogen'],
                 ['Salinesoil', 'maize', 'High', 'iron'],
                 ['Salinesoil', 'maize', 'low', 'ammonium sulphate '],
                 ['Salinesoil', 'pulses', 'High', 'magnesium'],
                 ['Salinesoil', 'pulses', 'low', 'iron'],
                 ['Salinesoil', 'cotton', 'High', 'ammonium sulphate'],
                 ['Salinesoil', 'cotton', 'low', 'magnesium'],
                 ['Peatysoils', 'Rice', 'low', 'alkaline'],
                 ['Peatysoils', 'Rice', 'High', 'magnesium'],
                 ['Peatysoils', 'wheat', 'High', 'not suitable for the soil '],
                 ['Peatysoils', 'wheat', 'low', 'iron'],
                 ['Peatysoils', 'millets', 'High', 'ammonium sulphate'],
                 ['Peatysoils', 'millets', 'low', 'urea'],
                 ['Peatysoils', 'sugarcane', 'High', 'iron'],
                 ['Peatysoils', 'sugarcane', 'low', 'magnesium '],
                 ['Peatysoils', 'groundnut', 'High', 'Nitrogen'],
                 ['Peatysoils', 'groundnut', 'low', 'iron'],
                 ['Peatysoils', 'coffee', 'High', 'calcium'],
                 ['Peatysoils', 'coffee', 'low', 'Nitrogen'],
                 ['Peatysoils', 'maize', 'High', 'iron'],
                 ['Peatysoils', 'maize', 'low', 'ammonium sulphate '],
                 ['Peatysoils', 'pulses', 'High', 'magnesium'],
                 ['Peatysoils', 'pulses', 'low', 'iron'],
                 ['Peatysoils', 'cotton', 'High', 'ammonium sulphate'],
                 ['Peatysoils', 'cotton', 'low', 'urea'],

                 ]
        print(soil,Crop,WaterAvailability)
        for i in range(len(farmers)):
            if soil==farmers[i][0] and Crop==farmers[i][1] and WaterAvailability ==farmers[i][2]:
                form=farmers[i][3]




    return render(request,'farmer.html',{'form':form})


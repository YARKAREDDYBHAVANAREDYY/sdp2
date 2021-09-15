from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
	path('admin/', admin.site.urls),
	path('login/', views.login, name="login"),
	path('', views.homefunction),

	path('agriculture/', views.agriculturefunction),
	path('aquaculture/', views.aquaculturefunction),
	path('mainhome/', views.mainhome,name="home"),
    path('agriEquipment/', views.agriEquipmentfunction),
    path('agriseeds/', views.agriseedsfunction),
    path('agriirrigation/', views.agriirrigationfunction),
	path('userreg/', views.userreg),
    path('timeline/', views.timeline),
	path('aquaEquipment/', views.aquaEquipmentfunction),
    path('aquaWater/', views.aquaWaterfunction),
	path('agriOrganic/', views.agriOrganicfunction),
	path('agriInOrganic/', views.agriInOrganicfunction),
	path('AgricultureWaste/', views.agriAgricultureWastefunction),
	path('IndutrialWaste/', views.agriIndutrialWastefunction),
	path('Livestock/', views.agriLivestockfunction),
	path('MunicipalSludge/', views.agriMunicipalSludgefunction),
	path('agriSoil/', views.agriSoilfunction),
	path('aquaFresh/', views.aquaFreshfunction),
	path('aquaLake/', views.aquaLakefunction),
	path('aquaResevoir/', views.aquaResevoirfunction),
	path('aquaStream/', views.aquaStreamfunction),
	path('agriweather/', views.agriweatherfunction),
	path('aquafertilizers/', views.aquafertilizersfunction),
	path('predict/', views.predict),
    path('predict/result', views.result),
	path('team/', views.team),
	path('team1/', views.team1),
    path("",include("image.urls")),
    path("", include("app.urls")),
	path('Fpredict/', views.predictfertilizer, name="predictfertilizer"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
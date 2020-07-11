from django.urls import path
from django.conf.urls import url
from studentsection.views import Home,Add,display,Update,delete,search,college,Main,register,Elogin,Elogout,profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
	path('Home',Home),
	path('Add',Add),
	path('display',display),
	url(r'^update([A-Za-z0-9].*[A-Za-z0-9])',Update),
	url(r'^delete([0-9]+)',delete),
	path('search',search),
	path('college',college),
	path('Main',Main),
	path('register',register),
	path('login',Elogin),
	path('logout',Elogout),
	path('profile',profile)
]



if settings.DEBUG :

	urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
from .models import CarOwner
from .models import LandOwner
from .models import Security
from django.http import Http404
# from caralgo import main
# Create your views here.
# def search(request):
# 	return render(request, 'parking/search.html')

# places = ['bharath','bayleaf','star','ming','mist']

# vacant['bharath']=True;
# vacant['star']=True;
# vacant['ming']=False;
# vacant['bayleaf']=False;
# vacant['mist']=True;

def search(request):
	# main.start([(300, 0), (1200, 0), (1200, 400), (1000, 400), (1000, 600), (0, 600), (0, 300)])
	return render(request,'parking/search.html',{'carowner_id':carowner_id})

def loc(request,carowner_id):
	return render(request,'parking/loc.html')

def namelist(request,carowner_id):
	return render(request, 'parking/namelist.html',{'places':Place.objects.all()})

def home(request):
	return render(request,'parking/home.html')


def name(request, carowner_id, place_name):
	places = [e.Name for e in Place.objects.all()]
	vacant ={}
	for i in Place.objects.all():
		vacant[i.Name]=i.Vacant
	l = len(places)
	for i in range(l):
		if(place_name==places[i] and vacant[place_name]!=0):
			return render(request,'parking/name.html',{'carowner_id':carowner_id,'place_name':place_name})
	return render(request,'parking/search.html')	


def book(request, carowner_id, place_name):
	places = [e.Name for e in Place.objects.all()]
	vacant ={}
	for i in Place.objects.all():
		vacant[i.Name]=i.Vacant
	if request.method=='POST':
		vacant_earlier = vacant[place_name]
		vacant[place_name]=vacant[place_name]-1
		vacant_now = vacant[place_name]
		p = Place.objects.get(Name=place_name)
		p.Vacant = vacant_now
		p.save()
		return render(request,'parking/book.html',{'place_name':place_name,'vacant_earlier':vacant_earlier,'vacant_now':vacant_now})
	else:
		return render(request,'parking/book.html',{'place_name':place_name,'vacant_earlier':Place.objects.get(Name=place_name).Vacant,'vacant_now':Place.objects.get(Name=place_name).Vacant})
			

def carowner(request, carowner_id):
	if CarOwner.objects.all().get(pk=carowner_id):
		return render(request,'parking/carowner.html',{'carowner':CarOwner.objects.all().get(pk=carowner_id)})
	else:
		return HttpResponse('<h1>User does not exist</h1>')	

def security(request, place_name):
	try:
		z = Place.objects.all().get(Name=place_name).pk
		s = [i for i in Security.objects.all()]
		for i in s:
			if(i.sid.pk==z):
				return render(request,'parking/security.html',{'sid':i.sid})
	except:		
		return HttpResponse('<h1>Security for this place does not exist</h1>')		


def security_update(request, place_name):
	if request.method=='POST':
		p = Place.objects.get(Name=place_name)
		p.Vacant = p.Vacant+1
		p.save()
		return render(request, 'parking/security_update.html',{'place_name':p})
	else:
		return render(request, 'parking/security_update.html',{'place_name':Place.objects.get(Name=place_name)})	

def security_list(request):
	slist = [i.sid.Name for i in Security.objects.all()]	
	return render(request, 'parking/security_list.html',{'security':slist})

def carowner_list(request):
	slist = [i for i in CarOwner.objects.all()]	
	slist1 = [i for i in CarOwner.objects.all()]	
	return render(request, 'parking/carowner_list.html',{'carowner':slist})

def landowner_list(request):
	slist = [i for i in LandOwner.objects.all()]	
	return render(request, 'parking/landowner_list.html',{'landowner':slist})

def landowner(request,landowner_id):
	if request.method=='POST':
		Place.objects.create(Name=request.POST.get('Name'),Vacant=request.POST.get('Slots'))
		LandOwner.objects.create(Name=request.POST.get('Name'),Slots=request.POST.get('Slots'))
		# LandOwner.objects.create(Name=request.POST.get('Name'),Vertices=request.POST.get('Vertices'))
		print(request.POST)
	x = LandOwner.objects.get(pk=landowner_id)
	return render(request, 'parking/landowner_id.html',{'landowner':x})

def landowner_id(request,landowner_id):
	x = LandOwner.objects.get(pk=landowner_id)
	return render(request, 'parking/landowner_id.html',{'landowner':x})

def security_login(request):
	return render(request,'parking/security_login.html')
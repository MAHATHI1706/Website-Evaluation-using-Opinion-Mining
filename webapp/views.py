from django.shortcuts import render
from django.http import HttpResponse, request
#from .models import user
from django.db.models import Avg
from .models import *

import xlrd
import matplotlib.pyplot as plt
import numpy as np


from .NB import nbclassfy
from .SVM import svmclassfy
from .RF import rfclassfy
from .NN import nnclassfy
from .Testing import Testing
from .Predict import Predict


# Create your views here.
def home(request):
	return render(request, 'index.html')
# Create your views here.
def alogin(request):
	return render(request, 'admin.html')
def adminlogin(request):
	if request.method=='POST':
		uid=request.POST['uid']
		pwd=request.POST['pwd']
		
		if uid=='admin' and pwd=='admin':
			request.session['adminid']='admin'
			return render(request, 'admin_home.html')

		else:
			return render(request, 'admin.html',{'msg':"Login Fail"})

	else:
		return render(request, 'admin.html')

def adminhomedef(request):
	if "adminid" in request.session:
		uid=request.session["adminid"]
		return render(request, 'admin_home.html')

	else:
		return render(request, 'admin.html')
def adminlogoutdef(request):
	try:
		del request.session['adminid']
	except:
		pass
	return render(request, 'admin.html')	
	


def search(request):
	if request.method=='POST':
		keys=request.POST['keys']

		d2=webres.objects.all()
		d2.delete()
		from .Search import Search
		d=Search.main(keys)
		d=list(d)

		for d1 in d:
			r=comments.objects.filter(url=d1)
			tot=0;p=0;neg=0;neu=0;
			for r1 in r:
				tot=tot+1
				if r1.sentiment=='positive':
					p=p+1
				if r1.sentiment=='negative':
					neg=neg+1
				if r1.sentiment=='neutral':
					neu=neu+1
			d4=webres(url=d1,num=tot, pos=p,neg=neg, neu=neu)
			d4.save()

		dd=webres.objects.all()

		return render(request, 'ugetlist.html',{'data':dd})

		
	else:
		return render(request, 'search.html')



def signup(request):
	if request.method=='POST':
		email=request.POST['mail']
		pwd=request.POST['pwd']
		zip=request.POST['zip']
		name=request.POST['name']
		gen=request.POST['gen']

		d=user.objects.filter(email__exact=email).count()
		if d>0:
			return render(request, 'signup.html',{'msg':"Email Already Registered"})
		else:
			d=user(name=name,email=email,pwd=pwd,zip=zip,gender=gen)
			d.save()
			return render(request, 'signup.html',{'msg':"Register Success, You can Login.."})
	else:
		return render(request, 'signup.html')


	
def loginaction(request):
	if request.method=='POST':
		uid=request.POST['mail']
		pwd=request.POST['pwd']
		d=user.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()
		
		if d>0:
			d=user.objects.filter(email__exact=uid)
			request.session['email']=uid
			return render(request, 'user_home.html',{'data': d[0]})

		else:
			return render(request, 'user.html',{'msg':"Login Fail"})

	else:
		return render(request, 'user.html')

def userlogout(request):
	try:
		del request.session['email']
	except:
		pass
	return render(request, 'user.html')
def userhome(request):
	if "email" in request.session:
		email=request.session["email"]
		d=user.objects.filter(email__exact=email)
		return render(request, 'user_home.html',{'data': d[0]})

	else:
		return redirect('slogout')


def viewcomments(request):
	if "email" in request.session:
		
		
		data=websites.objects.all()
		return render(request, 'ugetlist.html',{'data':data})



def postcomments(request):
	if request.method=='POST':
		email=request.session["email"]
		url=request.POST["url"]
		review=request.POST["review"]
		rating=request.POST['rating']
		sent=Predict.main(review)
		d=comments(url=url,user=email,comment=review,rating=rating,sentiment=sent)
		d.save()


		data=webres.objects.all()

		return render(request, 'ugetlist.html',{'data': data, 'msg':'Comment Posted Successfully'})
	else:
		url=request.GET["url"]
		data=comments.objects.filter(url=url).all()

		return render(request, 'feedback.html',{'data': data,  'url':url})		
		
		

def viewpprofile(request):
	if "email" in request.session:
		uid=request.session["email"]
		d=user.objects.filter(email__exact=uid)
		return render(request, 'viewpprofile.html',{'data': d[0]})

	else:
		return render(request, 'user.html')




def trainingpage(request):
    if "adminid" in request.session:

        return render(request, 'trainingpage.html')

    else:
        return render(request, 'admin.html')



def nbtrain(request):
    if "adminid" in request.session:

        nbclassfy()

        return render(request, 'trainingpage.html', {'msg': "Naive Bayes Algorithm classified Successfully.."})

    else:
        return render(request, 'admin.html')



def svmtrain(request):
    if "adminid" in request.session:

        svmclassfy()

        return render(request, 'trainingpage.html', {'msg': "SVM Algorithm classified Successfully.."})

    else:
        return render(request, 'admin.html')


def rftrain(request):
    if "adminid" in request.session:

        rfclassfy()

        return render(request, 'trainingpage.html', {'msg': "Random Forest Algorithm classified Successfully.."})

    else:
        return render(request, 'admin.html')


def nntrain(request):
    if "adminid" in request.session:

        nnclassfy()

        return render(request, 'trainingpage.html', {'msg': "Neural Network Algorithm classified Successfully.."})

    else:
        return render(request, 'admin.html')

def testing(request):
	if request.method=='POST':
		file='testset.csv'
		
		accuracy.objects.all().delete()


		nb=Testing.detecting(file, 'nb_model.sav')
		r=accuracy(algo='Naive Bayees',accuracyv=nb)
		r.save()
		
		nn=Testing.detecting(file, 'nn_model.sav')
		r=accuracy(algo='Nueral Network',accuracyv=nn)
		r.save()
		
		svm=Testing.detecting(file, 'svm_model.sav')
		r=accuracy(algo='SVM',accuracyv=svm)
		r.save()
		
		rf=Testing.detecting(file, 'rf_model.sav')
		r=accuracy(algo='Random Forest',accuracyv=rf)
		r.save()
		
		return render(request, 'testing.html',{'msg':"Testing of all algorithm completed successfully.."})


	else:
		return render(request, 'testing.html')




def accuracyview(request):
    if "adminid" in request.session:
        d = accuracy.objects.all()
        
        return render(request, 'viewaccuracy.html', {'data': d})

    else:
        return render(request, 'admin.html')


def viewgraph(request):
    if "adminid" in request.session:
        algos = []
        row = accuracy.objects.all()
        rlist = []
        for r in row:
            algos.append(r.algo)
            rlist.append(r.accuracyv)


        height = rlist
        # print(height)
        bars = algos
        y_pos = np.arange(len(bars))
        plt.bar(bars, height, color=['purple','blue','green','yellow', 'cyan'])
        # plt.plot( bars, height )
        plt.xlabel('Algorithms')
        plt.ylabel('Accuracy ')
        plt.title('Accuracy Measure')
        from PIL import Image 
        plt.savefig('E:\\g1.jpg')
        im = Image.open(r"E:\\g1.jpg") 
          
        im.show()
        d = accuracy.objects.all()
        return render(request, 'viewaccuracy.html', {'data': d})


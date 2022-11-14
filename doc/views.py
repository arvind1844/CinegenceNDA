from os import path
import tempfile
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from CinegenceDoc.settings import MEDIA_ROOT
from doc.models import *
from tkinter import Image
from urllib.request import urlopen
from doc.utils_client import pdf2
from doc.utils_staff import pdf1
from doc.utils_visitor import pdf3
from PIL import Image as PilImage
import io
import base64
import os
from django.core.files.storage import FileSystemStorage
from tempfile import NamedTemporaryFile
from django.core.mail import EmailMessage

# Create your views here.

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def staff(request):
    if request.method=="POST":
        name=request.POST.get('name')
        print(name)
        email=request.POST.get('email')
        print(email)
        contact=request.POST.get('phone')
        aadhar=request.POST.get('aadhar')
        pan_number=request.POST.get('pan')
        
        staff=Staff.objects.create(name=name,aadhar=aadhar,pan_number=pan_number,email=email,contact=contact)
        staff_id=staff.id
        messages.success(request,'Registered successfully!') 
        context={'user':staff,'staff_id':staff_id}   
        return redirect(f'/image_upload_staff/{staff_id}')
    else:
       print('staff not created')
       return render(request,'staff.html')
    

def visitor(request):
    if request.method=='POST':
        name=request.POST.get('name')
        contact=request.POST.get('phone')
        address=request.POST.get('address')
        
        visitor=Visitor.objects.create(name=name,contact=contact,address=address)
        visitor_id=visitor.id
        messages.info(request,'Registered successfully!')   
        
        context={'user':visitor,'visitor_id':visitor_id}   
        return redirect('/image_upload_visitor/'+str(visitor_id),context=context)
      
    else:
          return render(request,'visitor.html')
        

def client(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        aadhar=request.POST.get('aadhar')
        pan_number=request.POST.get('pan')
        
        client=Client.objects.create(name=name,email=email,aadhar=aadhar,pan_number=pan_number,address=address)
        client_id=client.id
        print(client_id)
        messages.info(request,'Registered successfully!')   
        
        context={'user':client,'client_id':client_id}   
        return redirect('/image_upload_client/'+str(client_id),context=context)
      
    else:
          return render(request,'client.html')
      
      
      
def image_upload_staff(request,id):
    id = int(id)
    context = dict()
    context['id'] = id
    if request.method == 'POST':
        print('id: ',id)
        img = request.FILES.get('image')
        print(img)
        staff=Staff.objects.get(id=id)
        print(staff)
        staff.image=img
        staff.save(update_fields=["image"]) 

        if img is not None:
            print('image')
            fileStorage = FileSystemStorage(location=MEDIA_ROOT/'UserImage')
            image_file = fileStorage.save(img.name, img)
            staff.image = 'UserImage/' + str(image_file)
            staff.save(update_fields=["image"])
            context["path"] = staff.image.url         #url to image stored in my server/local device
        else :
            return redirect('/image_upload_staff/'+str(id))
    return render(request, 'staff_img.html', context=context)          

def image_upload_client(request,id):
    id = int(id)
    context = dict()
    context['id'] = id
    if request.method == 'POST':
        print('id: ',id)
        img = request.FILES.get('image')
        print(img)
        client= Client.objects.get(id=id)
        client.image=img
        client.save(update_fields=["image"]) 

        if img is not None:
            print('image')
            fileStorage = FileSystemStorage(location=MEDIA_ROOT/'UserImage')
            image_file = fileStorage.save(img.name, img)
            client.image = 'UserImage/' + str(image_file)
            client.save(update_fields=["image"])
            context["path"] = client.image.url         #url to image stored in my server/local device
        else :
            return redirect('/image_upload_client/'+str(id))
    return render(request, 'client_img.html', context=context)

def image_upload_visitor(request,id):
    id = int(id)
    context = dict()
    context['id'] = id
    if request.method == 'POST':
        print('id: ',id)
        img = request.FILES.get('image')
        # obj = Staff.objects.create(image=img)  # create a object of Image type defined in your model
        visitor=Visitor.objects.get(id=id)
        print(visitor)
        visitor.image=img
        visitor.save(update_fields=["image"]) 

        if img is not None:
            print('image')
            fileStorage = FileSystemStorage(location=MEDIA_ROOT/'UserImage')
            image_file = fileStorage.save(img.name, img)
            visitor.image = 'UserImage/' + str(image_file)           
            visitor.save(update_fields=["image"])
            context["path"] = visitor.image.url         #url to image stored in my server/local device
        else :
            return redirect('/image_upload_visitor/'+str(id))
    return render(request, 'visitor_img.html', context=context)

def pdf_staff(request,id):
    nda_staff = Staff.objects.filter(id=id).first()
    pdf1(nda_staff)
    context = {'nda_staff': nda_staff,'id':id}
    return render(request, 'pdf_staff.html',context=context)

def pdf_client(request,id):
    nda_client = Client.objects.filter(id=id).first()
    print(nda_client)
    pdf2(nda_client)
    context = {'nda_client': nda_client,'id':id}
    return render(request, 'pdf_client.html',context=context)

def pdf_visitor(request,id):
    nda_visitor = Visitor.objects.filter(id=id).first()
    pdf3(nda_visitor)
    # if request.method == 'POST':
    #     submit_file = request.FILES.get('myfile',None)
    #     print('hello')
    #     send_mail('Hey pdf signature','Subject', '', [''], fail_silently=False)
    context = {'nda_visitor': nda_visitor,'id':id}
    return render(request, 'pdf_visitor.html',context=context)

def pdf_upload_staff(request):
    if request.method == 'POST':
        submit_file = request.FILES['myfile']
        id=request.POST.get('id')
        staff=Staff.objects.get(id=id)
        staff.nda=submit_file
        staff.save(update_fields=["nda"])
        submit=staff.nda
        print('hello')
        pdf_file=submit.file
        print(pdf_file)
        email = EmailMessage(
        'CINEGENCE', 'We are finally done!!!!', '', [''])
        email.attach("nda.pdf",pdf_file.read())
        email.send()
        return redirect('/')
    else:
        print('failed')
        
def pdf_upload_client(request):
    if request.method == 'POST':
        print(request.FILES)
        submit_file = request.FILES['myfile']
        id=request.POST.get('id')
        client=Client.objects.get(id=id)
        client.nda=submit_file
        client.save(update_fields=["nda"])
        submit=client.nda
        print('hello')
        pdf_file=submit.file
        print(pdf_file)
        email = EmailMessage('CINEGENCE', 'We are finally done!!!!', '', [''])
        email.attach("nda.pdf",pdf_file.read())
        email.send()
        return redirect('/')
    else:
        print('failed')
        
        
def pdf_upload_visitor(request):
    if request.method == 'POST':
        submit_file = request.FILES['myfile']
        id=request.POST.get('id')
        visitor=Visitor.objects.get(id=id)
        visitor.nda=submit_file
        visitor.save(update_fields=["nda"])
        submit=visitor.nda
        print('hello')
        pdf_file=submit.file
        print(pdf_file)
        email = EmailMessage(
        'CINEGENCE', 'We are finally done!!!!', '', [''])
        email.attach("nda.pdf",pdf_file.read())
        email.send()
        return redirect('/')
    else:
        print('failed')
    
    
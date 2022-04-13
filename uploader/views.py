from django.shortcuts import render, redirect
from uploader.forms import FileForm
from uploader.models import File
import os
from django.contrib import messages



def home(request):
    file_data = dict()
    file_form = FileForm(request.POST or None, request.FILES or None)

    if(file_form.is_valid()):
        if(str(request.FILES['file']).endswith('.pdf')):
            file=file_form.save()
            file.pdf_to_doc()
            redirect('home')
        elif(str(request.FILES['file']).endswith('.jpeg')):
            image = file_form.save()
            image.execute_img_and_save_ocr()
            redirect('home')
        elif(str(request.FILES['file']).endswith('.png')):
            image = file_form.save()
            image.execute_img_and_save_ocr()
            redirect('home')
        elif(str(request.FILES['file']).endswith('.jpg')):
            image = file_form.save()
            image.execute_img_and_save_ocr()
            redirect('home')
        else:
            File.objects.all().delete()
            context={}
            msg='Please re-upload all your files with acceptable extension (.jpeg/.jpg/.png/.pdf), after reloading the site'
            context['message']=msg
            messages.success(request,msg)
            return render(request,'uploader/index.html',context)
    


    file_list = File.objects.all().order_by('-id')


    file_data['file_form']=file_form
    file_data['file_list']=file_list
    return render(request, "uploader/index.html", file_data)

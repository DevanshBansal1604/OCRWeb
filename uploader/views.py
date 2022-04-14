# django file for handeling web-requests and responses

from django.shortcuts import render, redirect
from uploader.forms import FileForm
from uploader.models import File
import os
from django.contrib import messages

# main function to check the constraints satisfaction of the uploaded image/pdf, and call for its suitable function according to the test case.
def home(request):
    # data and form initialization (input)
    file_data = dict()
    file_form = FileForm(request.POST or None, request.FILES or None)

    # checking constraints
    if(file_form.is_valid()):
        #Deleting previous uploaded files
        File.objects.all().delete()
        # choosing the processing method based on use case
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
            # if incorrect file is uploaded, then do not upload to database.
            File.objects.all().delete()
            context={}
            # return an error message
            msg='Please re-upload all your files with acceptable extension (.jpeg/.jpg/.png/.pdf), after reloading the site'
            context['message']=msg
            messages.success(request,msg)
            # clear logs
            return render(request,'uploader/index.html',context)

    file_list = File.objects.all().order_by('-id')
    # save the processed file into database, and return urls
    file_data['file_form']=file_form
    file_data['file_list']=file_list
    return render(request, "uploader/index.html", file_data)

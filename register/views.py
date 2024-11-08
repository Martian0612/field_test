from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import CustomUserModel
from .forms import RegisterForm
from  django.contrib import messages
from PIL import Image
import os
# import magic



# general file format checker
# def validate_file_format(file_s)
#     def find_extension(file_s):
#         extension = ""
#         start = len(file_s)-1
#         end = 0
#         step = -1
#         for i in range(start,end,step):

#             if file_s[i] == ".":
#                 break
#             extension += file_s[i]
#         # print(extension[::-1])
#         file_type = extension[::-1]
#         return file_type
    
#     file_type = find_extension(file_s)

#     if file_type == "img":
#          img_file = ["jpg","png","gif","jpeg"]
         
         

#     elif file_type == "doc":
#         doc_file = ["pdf","rtf","odt","tex","txt","doc","docx","wpd"]

#     elif file_type == "ppt":
#         ppt_file = ["ppt","pptx","pptm"]

#     elif file_type == "audio":
#         audio_file = ["mp3","aac","wav","flac","ogg","pcm","alac"]

#     elif file_type == "video":
#         video_file = ["mp4","mov","avi","mkv"]

#     elif file_type == "excel":
#         excel_file = ["xlsx","xls","xltx","xlsb","xlsm"]

# # Create your views here.

# def register(response):
#     if response.method == "POST":
#         form = RegisterForm(response.POST,response.FILES)
#         # print(response.FILES)
#         custom_user= CustomUserModel(profile_photo = response.FILES['profile_photo'])
#         file = response.FILES['profile_photo']
        
#         file_s = str(file)
#         image = Image.open(file)
#         # width and height are in pixels
#         # for inches -> pixels/96 -> here width_inches = width/96
#         # for cm -> pixels/2.54 -> width_cm = width/2.54
#         width , height = image.size
#         print("width is ", width)
#         print("height is ", height)

#         width_inch = width/96
#         height_inch = height/96
#         ## thsi is not the way to find the size of file in bytes, as we don't have the actual path, we are getting it from url.
#         # size = os.path.getsize(file_s)
#         # print("file size in bytes", size)

        
#         # print("version is ",magic.__version__)
        
       
#         # file_type = magic.from_file(f"{file}",mime = True)
#         # print("file is ",file_type)
#         img_format = ["jpg","png","gif","jpeg"]
#         # if file_type in  :
#         extension = ""
#         start = len(file_s)-1
#         end = 0
#         step = -1
#         for i in range(start,end,step):

#             if file_s[i] == ".":
#                 break
#             extension += file_s[i]
#         # print(extension[::-1])
#         file_type = extension[::-1]
#         # only darshan pic is valid, how to make it more flexible like in neet application form
#         # if file_type in img_format and (width == 550) and (height == 550):

#         if file_type in img_format:
#             custom_user.save()
#             messages.success(response,"Image uploaded successfully!")
#         else:
#             messages.warning(response,"Invalid file format.")
#         form = RegisterForm()

#     else:
#         form = RegisterForm()
#     return render(response,'register/register.html',{"form":form})



## Exact or correct handling of the size of image is remaining, but it will work in this way.

## original code

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST,response.FILES)
        # print(response.FILES)
        custom_user= CustomUserModel(profile_photo = response.FILES['profile_photo'], resume = response.FILES['resume'])
        file1 = response.FILES['profile_photo']
        file1_s = str(file1)
        print(file1_s)

        file2 = response.FILES['resume']
        file2_s = str(file2)
        print(file2_s)
        
        # print("id is", id)
        

        image = Image.open(file1)
        # width and height are in pixels
        # for inches -> pixels/96 -> here width_inches = width/96
        # for cm -> pixels/2.54 -> width_cm = width/2.54
        width , height = image.size
        print("width is ", width)
        print("height is ", height)

        # width_inch = width/96
        # height_inch = height/96
        ## thsi is not the way to find the size of file in bytes, as we don't have the actual path, we are getting it from url.
        # size = os.path.getsize(file_s)
        # print("file size in bytes", size)

        
        # print("version is ",magic.__version__)
        
       
        # file_type = magic.from_file(f"{file}",mime = True)
        # print("file is ",file_type)
        img_format = ["jpg","png","gif","jpeg"]
        doc_format = ["pdf","rtf","odt","tex","txt","doc","docx","wpd"]

        # if file_type in  :
        extension = ""
        file_s = ""
        if file1:
            start = len(file1_s) - 1
            file_s = file1_s
        elif file2:
            start = len(file2_s)
            file_s = file2_s
        
        end = 0
        step = -1
        for i in range(start,end,step):

            if file_s[i] == ".":
                break
            extension += file_s[i]
        # print(extension[::-1])
        file_type = extension[::-1]
        # only darshan pic is valid, how to make it more flexible like in neet application form
        # if file_type in img_format and (width == 550) and (height == 550):
        # doc_file = ["pdf","rtf","odt","tex","txt","doc","docx","wpd"]
        # if file_type in doc_file:
        if file_type in img_format:
            custom_user.save()
            messages.success(response,"image uploaded successfully!")
        if file_type in doc_format:
            custom_user.save()
            messages.success(response,"resume uploaded successfully!")
        else:
            messages.warning(response,"Invalid file format.")
        form = RegisterForm()

    else:
        form = RegisterForm()
    return render(response,'register/register.html',{"form":form})

def show(response):
    print(response)
    return render(response,"register/show.html",{})

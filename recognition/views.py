from django.shortcuts import render
from django.core.mail import send_mail

from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from .utils import is_ajax, classify_face
import base64
from django.core.files.base import ContentFile
from django.urls import reverse
from pages.models import Profile,Log,persons
from django.contrib.auth.decorators import login_required

# Create your views here.
#def index (request):
#    return render (request, 'pages/index.html')

@login_required
def face_view(request):
    return render(request, 'pages/detectFace.html', {})

@login_required
def find_user_view(request):
   if is_ajax(request):
        photo = request.POST.get('photo')
        number = request.POST.get('number')  # Get the number from the request
      
        _, str_img = photo.split(';base64')

        decoded_file = base64.b64decode(str_img)

        x = Log()
        x.photo.save('upload.png', ContentFile(decoded_file))
        x.save()
        
        res = classify_face(x.photo.path)

        if res:
            person_exists = persons.objects.filter(name=res, nationalId=number).exists()
            print(person_exists)
            print(person_exists)
            if person_exists:
                print(person_exists)
                user = persons.objects.get(name=res)
                profile = Profile.objects.get(user=user)
                x.profile = profile
                x.save()
                redirect_url = reverse('election')
                return JsonResponse({'success': True, 'redirect_url': redirect_url}) 
            else:
              print(person_exists)
              redirect_url = reverse('faild-recognition')
              return JsonResponse({'success': False, 'redirect_url': redirect_url}) 

        redirect_url = reverse('faild-recognition')
        return JsonResponse({'success': False, 'redirect_url': redirect_url}) 
      

   else:
        return render(request, 'success/recognition_Faild.html')
   

def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'your_email@gmail.com',  # Sender's email address
        recipient_list,
        fail_silently=False,
    )
# Create your views here.
@login_required
def recognition_Faild(request):
  return render(request, 'success/recognition_Faild.html')

      

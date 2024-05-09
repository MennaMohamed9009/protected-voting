from django.shortcuts import render
from django.shortcuts import render
from recognition.views import send_email
from django.contrib.auth.decorators import login_required

# Create your views here.
#def index (request):
#    return render (request, 'pages/index.html')
@login_required
def election(request):
    if request.method == 'POST':
        subject = 'Hello from Django!'
        message = 'تمت عمليه الانتخاب بنجاح'
        recipient_list = [request.user.email]
        try:
            send_email(subject, message, recipient_list)
            return render(request, 'success/enail_sent.html')
        except Exception as e:
            print("There is a problem in the connection:", e)
    return render(request, 'pages/election.html')


def DiagramView(request):
    return render(request, 'diagram/diagram.html')

def index(request):
     return render (request, 'pages/index.html')

def info(request):

     return render (request, 'pages/info.html')

def sisi(request):

     return render (request, 'pages/sisi.html')

def hazem(request):

     return render (request, 'pages/hazem.html')

def abd_el_sanad (request):

     return render (request, 'pages/abd el sanad.html')


def mohamed (request):

     return render (request, 'pages/mohamed.html')



def getPhoneNumber (request):

      return render (request, 'pages/getPhoneNumber.html')

def newPassword (request):

     return render (request, 'pages/newPassword.html')

def getCode (request):

     return render (request, 'pages/getCode.html')


def startElection (request):

     return render (request, 'pages/startElection.html')


def sendMassege (request):

     return render (request, 'pages/sendMassege.html')










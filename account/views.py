from django.shortcuts import render
from .forms import ctreateuserform,LoginForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout 

# Create your views here.
def createAcc(request):
     if request.method=='POST':
        form=ctreateuserform(request.POST)
        if form.is_valid():
            print("form 11")
            form.is_superuser=False
            user = form.save()
            # Authenticate the newly created user
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            if user is not None:
                auth_login(request, user)
                return redirect('face')
      
     else:
        print("form 111")
        form=ctreateuserform()
   
     context={
        'form':form,
      }
     return render (request, 'pages/createAcc.html',context)
def login_view(request):
     if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:  
                auth_login(request, user)
                # Redirect to a success page or homepage
                return redirect('face')
     else:
        form = LoginForm()
     return render(request, 'pages/login.html', {'form': form})

def getPhoneNumber (request):

      return render (request, 'pages/getPhoneNumber.html')

def newPassword (request):

     return render (request, 'pages/newPassword.html')

def getCode (request):

     return render (request, 'pages/getCode.html')

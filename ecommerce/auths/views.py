from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

def signup(request):
    if request.method== "POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password != confirm_password:
            HttpResponse('Incorrect password')
        try:
            if User.objects.get(username=email):
                HttpResponse('Email already exists')
        except Exception as identifier:
            pass
        user=User.objects.create_user(email,email,password)
        user.save()
        return HttpResponse("user created",email)
        
    return render(request, 'authentication/signup.html')

def handlelogin(request):
    return render(request, 'authentication/login.html')

def handlelogout(request):
    return redirect('/auths/login')
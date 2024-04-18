from django.conf import settings
from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.


User=settings.AUTH_USER_MODEL
def register_view(request):
    form = UserRegisterForm()  # Define form outside the if-else block
    if request.method == 'POST':
        form = UserRegisterForm(request.POST )
        if form.is_valid():
            
            print('registered successfully')
            new_user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"Hey {username},sign-up successfully")
            new_user=authenticate(username=form.cleaned_data['email'],
                                  password=form.cleaned_data['password1'])
            login(request,new_user)
            return redirect('index')
    else:
        print('user cannot be register')

    context = {
        'form': form
    }

    return render(request, 'userauths/sign_up.html', context)

# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('index')
#     if request.method=='POST':
#         email=request.POST.get('email')
#         password=request.POST.get('passsword')
    
#         try:
#         # user=User.object.all()
#             user=User.object.get(email=email)

#         except:
#             messages.warning(request,f"User with {email} Already exisr")
    
#         user=authenticate(request,email=email, password=password)
#         if user.is_not_None:
#             login(request,user)
#             messages.success(request,'You Are Logged in Successfully')
#             return redirect('index')
#         else:
#             messages.warning(request,"Incorrect Username Or Password")
#     context={

#     }
    
#     return redirect(request,'userauths/login.html',context)



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in.')
                return redirect('index')  # Redirect to the index page after successful login
            # else:
            #     messages.error(request, 'Invalid email or password. Please try again.')
                
        except:
            messages.warning(request,f"user with {email} does not exist")
    return render(request, 'userauths/login.html', {})



def logout_view(request):
    logout(request)

    return redirect("login")




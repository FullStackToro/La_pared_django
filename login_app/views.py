from django.shortcuts import render, HttpResponse, redirect
from .models import Usuario, Cuenta
from django.contrib import messages

def home(request):
    request.session['log_name'] = ""
    request.session['log_email'] = ""
    request.session['log_user'] = 0
    return render(request, 'index.html')

#Registro de Usuarios
def registrar(request):
    error = Usuario.objects.validacion_registro(request.POST)
    if len(error) > 0:
        request.session['mensaje'] = 0
        for key, value in error.items():
            request.session['error_registro'] = messages.error(request, value)
            print(key, value)
        return redirect('/')
    else:
        password = Usuario.objects.password_hash(request.POST)
        temp = Cuenta.objects.create(email=request.POST['email'], password=password)
        Usuario.objects.create(name=request.POST['nombre'], apellido=request.POST['apellido'], cuenta=temp)
    return redirect("/registrado")

def registrado(request):
    return render(request, 'registro_success.html')

#Login de Usuarios
def login(request):
    error=Usuario.objects.validacion_login(request.POST)
    if len(error) > 0:
        request.session['mensaje'] = 1
        for key, value in error.items():
            request.session['error_login']=messages.error(request, value)
            print(key, value)

        return redirect('/')
    else:
        request.session['log_user'] = request.POST['login_email']
        users=Usuario.objects.get(cuenta__email__icontains=request.POST['login_email'])
        request.session['log_name']=f"{users.name} {users.apellido}"
        request.session['log_email'] = f"{users.cuenta.email}"
        request.session['log_id'] = f"{users.cuenta.id}"
        return redirect(f"/wall/{Cuenta.objects.get(email=request.POST['login_email']).id}")


#def logeado(request):
#    if request.session['log_user'] != 0:
#        return render(request, "login.html")
#    else:
#        return redirect('/')

#Desconectar

def logout(request):
    request.session['log_name'] = ""
    request.session['log_email'] = ""
    request.session['log_user'] = 0
    return redirect('/')

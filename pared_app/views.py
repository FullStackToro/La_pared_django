from django.shortcuts import render, HttpResponse, redirect
from login_app.models import Usuario, Cuenta
from pared_app.models import Mensajes, Comentarios

def success(request, op):
    if request.session['log_user'] != 0:
        context= {
            'opcion': op
        }
    else:
        return redirect('/')
    return render(request, "success.html", context)

def muro(request):
    if request.session['log_user'] != 0:
        temp=Usuario.objects.all()
        for user in temp:
            print(user.users_comentario)
        context= {
            'mnsj': Mensajes.objects.all().order_by('-id'),
            'cmntr': Comentarios.objects.all()
        }
    else:
        return redirect('/')
    return render(request, "muro.html", context)

def mensaje(request, _op):
    if request.session['log_user'] != 0:
        mnsj=Mensajes.objects.create(mensaje=request.POST['wall_post'], mensaje_usuario_id=Usuario.objects.get(id=_op))
        print(mnsj)
    else:
        return redirect('/')
    return redirect("/wall")


def comentario(request, _op, _mensaje_id):
    if request.session['log_user'] != 0:
        cmntr=Comentarios.objects.create(comentario=request.POST['wall_comment'], comentario_mensaje_id = Mensajes.objects.get(id=_mensaje_id), comentario_usuario_id =Usuario.objects.get(id=_op))
    else:
        return redirect('/')
    return redirect("/wall")

def delete_comment(request,_op,_comentario_id):
    if request.session['log_user'] != 0:
        if request.session['log_id'] == _op:
            temp = Comentarios.objects.get(id=_comentario_id)
            temp.delete()
            return redirect('/wall')
    else:
        return redirect('/')
    return redirect('/wall')

def delete_mensaje(request,_op,_mensaje_id):
    if request.session['log_user'] != 0:
        if request.session['log_id'] == _op:
            temp=Mensajes.objects.get(id=_mensaje_id)
            temp.delete()
            return redirect('/wall')
    else:
        return redirect('/')
    return redirect('/wall')


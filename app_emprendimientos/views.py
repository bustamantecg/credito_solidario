from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from app_emprendimientos.models import Emprendimiento
from app_emprendimientos.forms import FormEmprendimiento


def emprendimientos(request):
    emprendimientos = Emprendimiento.objects.all()
    return render(request, "app_emprendimientos/emprendimientos.html", {'emprendimientos': emprendimientos})


def Emprendimiento_detalle(request, id):
    emprendimiento = get_object_or_404(Emprendimiento, pk=id)
    return render(request, "app_emprendimientos/emprendimiento_detalle.html", {'emprendimiento':emprendimiento})


def emprendimiento_nuevo(request):
    if request.method == 'POST':
        formEmprendiNuevo = FormEmprendimiento(request.POST)
        if formEmprendiNuevo.is_valid():
            formEmprendiNuevo.save()
            return redirect('emprendimientos')
    else:
        formEmprendiNuevo = FormEmprendimiento()
    return render(request, 'app_emprendimientos/emprendimiento_nuevo.html', {'formEmprendiNuevo': formEmprendiNuevo})        


@login_required
def emprendimiento_editar(request, id):
    emprendi = get_object_or_404(Emprendimiento, pk=id)    
    if request.method == 'POST':
        formEmprendi_editar = FormEmprendimiento(request.POST, instance=emprendi)
        if formEmprendi_editar.is_valid():
            formEmprendi_editar.save()
            return redirect('emprendimientos')
    else:
        formEmprendi_editar = FormEmprendimiento(instance=emprendi)
    return render(request, 'app_emprendimientos/emprendimiento_editar.html', {'formEmprendi_editar': formEmprendi_editar})

"""
@login_required
def bookmark_edit(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if bookmark.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = BookmarkForm(instance=bookmark, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('marcador_bookmark_user',
                username=request.user.username)
    else:
        form = BookmarkForm(instance=bookmark)
    context = {'form': form, 'create': False}
    return render(request, 'marcador/form.html', context)

    
def bookmark_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        bookmarks = user.bookmarks.all()
    else:
        bookmarks = Bookmark.public.filter(owner__username=username)
    context = {'bookmarks': bookmarks, 'owner': user}
    return render(request, 'marcador/bookmark_user.html', context)

class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', blank=True)
    is_public = models.BooleanField('public', default=True)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    owner = models.ForeignKey(User, verbose_name='owner', related_name='bookmarks')        
"""    
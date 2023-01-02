from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from . import models
from time import gmtime, strftime


def index(request):
 
    return render(request,"basic.html")



def addshow(request):
    shows=request.POST
    result=models.add_show(shows['title'],shows['network'],shows['releasedate'],shows['description'])
    return redirect('/showtwo/'+str(result.id))

def showtwo(request,id):
    context={
        'show':models.get_showbyid(id)
        
    }
    return render(request,'show.html',context)

def shows(request):
    context={
        'shows':models.get_all_shows()
    }
    return render(request,'template.html',context)

def delete(request,id):
        models.delete_show(id)
        return redirect('/shows')

def edit(request,id):
        show = models.get_showbyid(id)
        # rel_date_formatted = show.releasedate.strftime("%Y-%m-%d  %H:%M", gmtime())
        
        context = {
            'id':id,
            'title' : show.title,
            'network' : show.network,
            'releasedate' : show.releasedate,
            'description' : show.description,
        
        }
        return render(request,"edit_sh.html",context)


def editshow(request,id):
    shows=request.POST
    show=models.update_show(id,shows['title'],shows['network'],shows['releasedate'],shows['description'])
    return redirect('/shows')


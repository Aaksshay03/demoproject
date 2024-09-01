from django.shortcuts import render,get_object_or_404,redirect
from myapp.models import Study

# Create your views here.

def welcome(request):
    data=Study.objects.all()
    return render(request,'welcome.html',{'data':data})

def view_detail(request,id):
    data=get_object_or_404(Study,id=id)
    return render(request,'view_detail.html',{'data':data})

def edit_detail(request,id):
    data=get_object_or_404(Study,id=id)
    return render(request,'edit_detail.html',{'data':data})

def update(request,id):
    data=get_object_or_404(Study,id=id)
    
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        phase=request.POST.get('phase')
        sponsor_name=request.POST.get('sponsor_name')

        

        if name:
            data.name=name
        
        if description:
            data.description=description
        
        if phase:
            data.phase=phase
        
        if sponsor_name:
            data.sponsor_name=sponsor_name
        
        
        data.save()

        return redirect('welcome')
        



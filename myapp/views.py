from django.shortcuts import redirect, render
from .models import student
from .forms import studentform
# Create your views here.

def welcome(reguest):
    return render(reguest,'welcome.html')


def loadform(reguest):
    form=studentform
    return render(reguest,'index.html',{'form':form})
# add data
def add(reguest):
    form=studentform(reguest.POST)
    form.save() 
    return redirect('/show')

# show data
def datashow(reguest):
    st=student.objects.all
    return render(reguest,'show.html',{'data':st})


# edit data
def edit(reguest, id):
    st=student.objects.get(id=id)
    return redirect(reguest,'edit.html',{'data':st})

#update data
def update(reguest, id):
    st=student.objects.get(id=id)
    form=studentform(reguest.POST,instance=st)
    form.save() 
    return redirect(reguest,'/show')   

#delete data
def delete(reguest, id):
    st=student.objects.get(id=id)
    st.delete() 
    return redirect(reguest,'/show')     

#search data
def search(reguest):
    names=reguest.POST['name']   
    st=student.objects.filter(name=names)
    return redirect(reguest,'show.html',{'data':st})
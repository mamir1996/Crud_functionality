from django.shortcuts import render,redirect
from CRUD.forms import Profile
from CRUD.models import Registration
from django.contrib import messages
# Create your views here.
def home(req):
    if req.method == "POST":
            form = Profile(req.POST)
            if form.is_valid():
                form.save()
                messages.success(req,"Form submit successfully !")
                return redirect('display_data')  # redirect only if saved

    else:
        form = Profile()

    return render(req, 'CRUD/home.html', {'form': form})

# display data 
def display_data(req):
    get_data=Registration.objects.all()
    return render(req,'CRUD/display_data.html',{'get_data':get_data})


# edit data 
def edit_page(req, pk):
    edit_data = Registration.objects.get(pk=pk)
    
    if req.method == "POST":
        form = Profile(req.POST, instance=edit_data)
        if form.is_valid():
            form.save()
            return redirect('display_data')
    else:
        form = Profile(instance=edit_data)
    
    return render(req, 'CRUD/edit_page.html', {'form': form})
 
# delete data 
def delete_page(req,pk):
    del_data=Registration.objects.get(pk=pk)
    if req.method=="POST":
        del_data.delete()
        messages.success(req,"Data deleted successfully !")
        return redirect('display_data')
    return render(req,'CRUD/delete_confirm.html',{'del_data':del_data})

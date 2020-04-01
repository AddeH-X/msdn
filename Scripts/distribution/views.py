from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required

from .models import Hospital,M_material
from .forms import HospitalForm,M_materialForm

def index(request):
    """分配网站的首页"""
    return render(request,'distribution/index.html')

@login_required
def hospitals(request):
    """显示所有已经注册的医院"""
    hospitals=Hospital.objects.order_by('last_login')
    context={'hospitals':hospitals}
    return render(request,'distribution/hospitals.html',context)

@login_required
def hospital(request,hospital_id):
    """显示某一医院所需的医疗物资"""
    hospital=Hospital.objects.get(id=hospital_id)
    needs=hospital.m_material_set.order_by('-urgency')
    context={'hospital':hospital,'needs':needs}
    return render(request,'distribution/hospital.html',context)

@login_required
def new_hospital(request):
    """添加新的医院信息"""
    if request.method !='POST':
        form = HospitalForm()
    else:
        form = HospitalForm(request.POST)
        if form.is_valid():
            new_hospital = form.save(commit=False)
            new_hospital.owner =request.user
            new_hospital.save()
            return redirect(reverse('distribution:hospitals'))

    context ={'form':form}
    return render(request,'distribution/new_hospital.html',context)

@login_required
def add_need(request,hospital_id):
    """添加新的物资信息"""
    hospital = Hospital.objects.get(id=hospital_id)
    if hospital.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = M_materialForm()
    else:
        form = M_materialForm(data=request.POST)
        if form.is_valid():
            new_need = form.save(commit=False)
            new_need.hospital = hospital
            new_need.save()
            return redirect(reverse('distribution:hospital',args=[hospital_id]))

    context={'form':form,'hospital':hospital}
    return render(request,'distribution/add_need.html',context)

@login_required
def edit_need(request,need_id):
    need = M_material.objects.get(id=need_id)
    hospital = need.hospital
    if hospital.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = M_materialForm(instance=need)
    else:
        form = M_materialForm(instance=need,data=request.POST)
        if form.is_valid():
            now_need = form.save(commit=True)
            now_need.hospital = hospital
            now_need.save()
            return redirect(reverse('distribution:hospital',args=[hospital.id]))

    context={'form':form,'need':need,'hospital':hospital}
    return render(request,'distribution/edit_need.html',context)







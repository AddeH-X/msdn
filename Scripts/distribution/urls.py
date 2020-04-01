from django.urls import path

from . import views

#应用的名称
app_name='distribution'

urlpatterns=[
    #主页
    path('',views.index,name='index'),
    #显示所有已经注册的医院
    path('hospitals/',views.hospitals,name='hospitals'),
    #显示某所医院所需医疗物资
    path('hospitals/<int:hospital_id>/',views.hospital,name='hospital'),
    #用于添加新的医院信息
    path('new_hospital',views.new_hospital,name='new_hospital'),
    #用于添加新的所需物资
    path('add_need/<int:hospital_id>/',views.add_need,name='add_need'),
    #修改所需物资
    path('edit_need/<int:need_id>/',views.edit_need,name='edit_need'),
]
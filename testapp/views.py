

from functools import partial
from tokenize import Token
from urllib import response
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from testapp.models import Mymodel
from testapp.forms import Myform
# Create your views here.
def mybase(request):
    return render(request,'testapp/base.html')

def f1(request,id=None):
    if id is not None:
        print('***',id)
        obj=Mymodel.objects.filter(id=id)
        return render(request,'testapp/wish.html',{'obj':obj})
    obj=Mymodel.objects.all()
    return render(request,'testapp/wish.html',{'obj':obj})



def f2(request):
    frmobj=Myform()
    if request.method=='POST':
        frm=Myform(request.POST)
        if frm.is_valid():
            frm.save(commit=True)
            return redirect('/hello')
    return render(request,'testapp/frm.html',{'frmobj':frmobj})
def updt(request,id=None):
    print('hi im updating')
    if id is not None:
        obj=Mymodel.objects.get(id=id)
    if request.method=='POST':
        updtfrm=Myform(request.POST,instance=obj)
        if updtfrm.is_valid():
            updtfrm.save(commit=True)
            return redirect('/hello')
    # obj=Myform.objects.all()
    return render(request,'testapp/update.html',{'obj':obj})
def dlt(request,id=None): 
    print('*******delete')  
    if id is not None:
        obj=Mymodel.objects.get(id=id)
        obj.delete()
        return redirect('/hello')
    return HttpResponse('thnks')

import json
from django.core import serializers
from django.views.generic import View
# from testapp.mixins import Support_mixin
# class CBV_View(View,Support_mixin):
#     def get(self,request,*args,**kwargs):
#         msg=json.dumps({'msg':'this is from get method'})
#         return self.render_httpresp(msg)
#     def post(self,request,*args,**kwargs):
#         msg=json.dumps({'msg':'this is from post method'})
#         return self.render_httpresp(msg)
#     def put(self,request,*args,**kwargs):
#         msg=json.dumps({'msg':'this is from put method'})
#         return self.render_httpresp(msg)
#     def delete(self,request,*args,**kwargs):
#         msg=json.dumps({'msg':'this is from delete method'})
#         return self.render_httpresp(msg)
    



def f1(request,id=None):
    if id is not None:
        print('***',id)
        obj=Mymodel.objects.filter(id=id)
        return render(request,'testapp/wish.html',{'obj':obj})
    obj=Mymodel.objects.all()
    return render(request,'testapp/wish.html',{'obj':obj})

from django.core.serializers import serialize
from testapp.mixins import Field_mixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class CBV3_View(View,Field_mixin):
    def get(self,request,id=None,*args,**kwargs):
        f_list=[]
        if id is not None:
            try:
                obj=Mymodel.objects.get(id=id)
            except Mymodel.DoesNotExist:
                return HttpResponse(json.dumps({'msg':'please provide valid id'}),status=404)
            else:
                j_data=serialize('json',[obj,])
                return self.field_resp(j_data)
        obj=Mymodel.objects.all()
        j_data=serialize('json',obj)
        return self.field_resp(j_data)
    def post(self,request,*args,**kwargs):
        data=request.body
        emp_data=json.loads(data)
        e_form=Myform(emp_data)
        if e_form.is_valid():
            e_form.save(commit=True)
            json_data=json.dumps({'msg':'this is post method'})
            return HttpResponse(json_data,content_type='application/json',status=200)    
        json_data=json.dumps({'msg':'something went wrong'})
        return HttpResponse(json_data,content_type='application/json',status=400)
    def put(self,request,id,*args,**kwargs):
        emp=Mymodel.objects.get(id=id)
        emp_data={
            'name':emp.name,
            'role':emp.role,
            'project':emp.project,
            'email':emp.email,
            'location':emp.location
        } 
        # or_data=serialize('json',[emp,])
        # emp_data=json.loads(or_data)
        pr_json=request.body
        pr_dict=json.loads(pr_json)    
        emp_data.update(pr_dict)
        frm=Myform(emp_data,instance=emp)
        if frm.is_valid():
            frm.save(commit=True)
            json_data=json.dumps({'msg':'updated sucessfully'})
            return HttpResponse(json_data,content_type='application/json',status=200)
        json_data=json.dumps({'msg':'updation falied pls check'})
        return HttpResponse(json_data,content_type='application/json',status=400)



class CBV4(View,Field_mixin):
    def get(self,request,*args,**kwargs):
        data=request.body
        py_dict=json.loads(data)
        print(py_dict)
        eid=py_dict.get('id',None)
        print('----',eid)
        if eid is not None:
            obj=Mymodel.objects.get(id=eid)
            json_data=serialize('json',[obj,])
            return self.field_resp(json_data)
        obj=Mymodel.objects.all()
        json_data=serialize('json',obj)
        return self.field_resp(json_data)
    def post(self,request,*args,**kwargs):
        data=request.body
        py_dict=json.loads(data)
        e_form=Myform(py_dict)
        if e_form.is_valid():
            e_form.save(commit=True)
            json_data=json.dumps({'msg':'data updated sucessfully'})
            return HttpResponse(json_data,content_type='application/json',status=200)    
        json_data=json.dumps({'msg':'something went wrong'})
        return HttpResponse(json_data,content_type='application/json',status=400)
    def put(self,request,*args,**kwargs):
        data=request.body
        f_list=[]
        provided_dict=json.loads(data)
        eid=provided_dict.get('id',None)
        original_data=Mymodel.objects.get(id=eid)
        pj_data=serialize('json',[original_data,])
        pyo_dict=json.loads(pj_data)
        for edata in pyo_dict:
            emp_data=edata['fields']
            f_list.append(emp_data)
        f_list[0].update(provided_dict)
        eform=Myform(f_list[0],instance=original_data)
        if eform.is_valid():
            eform.save(commit=True)
            return HttpResponse(json.dumps({'msg':'updated'}))  
        return HttpResponse(json.dumps({'msg':'thnq'}))
    def delete(self,request,*args,**kwargs):
        data=request.body
        provided_dict=json.loads(data)
        eid=provided_dict.get('id',None)
        if eid is not None:
            obj=Mymodel.objects.get(id=eid)
            obj.delete()
            return HttpResponse(json.dumps({'msg':'deleted pls check'}))
        return HttpResponse(json.dumps({'msg':'pls provide a valid id'}))

from rest_framework.renderers import JSONRenderer
from testapp.serializers import EmployeeSerializer
class Rest(View):
    def get(self,request,*args,**kwargs):
        data=request.body
        py_data=json.loads(data)
        eid=py_data.get('id',None)
        if eid is not None:
            obj=Mymodel.objects.get(id=eid)
            py_dict=EmployeeSerializer(obj)
            print('*****',py_dict.data)
            json_data=JSONRenderer().render(py_dict.data)
            return HttpResponse(json_data,content_type='application/json')
        obj=Mymodel.objects.all()
        py_dict=EmployeeSerializer(obj,many=True)
        json_data=JSONRenderer().render(py_dict.data)
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        data=request.body
        py_data=json.loads(data)
        serializer=EmployeeSerializer(data=py_data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'record created successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    def put(self,request,*args,**kwargs):
        data=request.body
        py_data=json.loads(data)
        eid=py_data.get('id',None)
        if eid is not None:
            eobj=Mymodel.objects.get(id=eid)
            serializer=EmployeeSerializer(eobj,data=py_data,partial=True)
            if serializer.is_valid():
                serializer.save()
                msg={'msg':'record updated successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
from rest_framework.views import APIView
from rest_framework.response import Response
class TestApi(APIView):
    def get(self,request,*args,**kwargs):
        eid=self.request.GET.get('id')
        if eid is not None:
            qsobj=Mymodel.objects.get(id=eid)
            py_dict=EmployeeSerializer(qsobj)
            return Response(py_dict.data)
        qsobj=Mymodel.objects.all()
        py_dict=EmployeeSerializer(qsobj,many=True)
        return Response(py_dict.data)
        
    def post(self,request,*args,**kwargs):
        data=request.body
        pry_data=json.loads(data)
        serializer=EmployeeSerializer(data=pry_data)
        if serializer.is_valid():
            serializer.save()
            py_dict={'msg':'resource created successfully'}
            return Response(py_dict)
        py_dict={'msg':'APIVIEW from post method something wrong'}
        return Response(py_dict)
    def put(self,request,*args,**kwargs):
        pr_data=request.body
        pr_dict=json.loads(pr_data)
        # try:
        #     eid=self.request.GET.get('id')
        # except:
        #     eid=pr_dict.get('id',None)
        #     print('**********',eid)
        eid=pr_dict.get('id',None)
        if eid is not None:
            eobj=Mymodel.objects.get(id=eid)
            serializer=EmployeeSerializer(eobj,data=pr_dict)
            if serializer.is_valid():
                serializer.save()
                py_dict={'msg':'resource updated successfully'}
                return Response(py_dict)
        py_dict={'msg':'resource something wrong'}
        return Response(py_dict)
    def patch(self,request,*args,**kwargs):
        pr_data=request.body
        pr_dict=json.loads(pr_data)
        eid=pr_dict.get('id',None)
        if eid is not None:
            eobj=Mymodel.objects.get(id=eid)
            serializer=EmployeeSerializer(eobj,data=pr_dict,partial=True)
            print('****',eid)
            if serializer.is_valid():
                serializer.save()
                py_dict={'msg':'resource updated successfully'}
                return Response(py_dict)
        py_dict={'msg':'resource something wrong'}
        return Response(py_dict)
    def delete(request,*args,**kwargs):
        py_dict={'msg':'APIVIEW from delete method'}
        return Response(py_dict)
from rest_framework.viewsets import ViewSet
class TestViewset(ViewSet):
    def list(request,*args,**kwargs):
        py_dict={'msg':'Viewsets from list method'}
        return Response(py_dict)
    def create(request,*args,**kwargs):
        py_dict={'msg':'Viewsets from create method'}
        return Response(py_dict)
    def retrieve(self,request,pk=None,*args,**kwargs):
        py_dict={'msg':'Viewsets from retrive method'}
        return Response(py_dict)
    def update(self,request,pk=None,*args,**kwargs):
        py_dict={'msg':'Viewsets from update method'}
        return Response(py_dict)
    def partial_update(self,request,pk=None,*args,**kwargs):
        py_dict={'msg':'viewset from patila_method'}
        return Response(py_dict)
    def destroy(self,request,pk=None,*args,**kwargs):
        py_dict={'msg':'Viewsets from destroye method'}
        return Response(py_dict)

from rest_framework.views import APIView
from rest_framework.response import Response
class Myapi(APIView):
    def get(self,request,*args,**kwargs):
        # data=request.body
        # pj_dict=json.loads(data)   
        # eid=pj_dict.get('id',None)
        eid=self.request.GET.get('id')
        if eid is not None:
            eobj=Mymodel.objects.get(id=eid)
            py_dict=EmployeeSerializer(eobj)
            return Response(py_dict.data)
        eobj=Mymodel.objects.all()
        py_dict=EmployeeSerializer(eobj,many=True)
        return Response(py_dict.data)

from rest_framework.generics import ListAPIView,CreateAPIView
class listapi(ListAPIView):
    # queryset=Mymodel.objects.all()
    serializer_class=EmployeeSerializer
    def get_queryset(self):
        qs=Mymodel.objects.all()
        ename=self.request.GET.get('name')
        if ename is not None:
            qs=qs.filter(name__contains='sikindar')
            return qs
        return qs
class createapi(CreateAPIView):
    queryset=Mymodel.objects.all()
    serializer_class=EmployeeSerializer
from rest_framework.generics import RetrieveAPIView
class retrieve(RetrieveAPIView):
    queryset=Mymodel.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'
from rest_framework.generics import UpdateAPIView
class updateapi(UpdateAPIView):
    queryset=Mymodel.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'
from rest_framework.generics import DestroyAPIView
class destroy(DestroyAPIView):
    queryset=Mymodel.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
class Allcls(ListCreateAPIView):
    serializer_class=EmployeeSerializer
    queryset=Mymodel.objects.all()
class Allcls2(RetrieveUpdateDestroyAPIView):
    serializer_class=EmployeeSerializer
    queryset=Mymodel.objects.all()
    lookup_field='id'
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet
class Mdlviewset(ModelViewSet):
    queryset=Mymodel.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]







            




        










        


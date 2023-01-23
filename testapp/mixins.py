
from django.http import HttpResponse
# class Support_mixin(object):
#     def render_httpresp(self,json_data):
#         return HttpResponse(json_data,content_type='apllicaton/json')
from django.core.serializers import serialize
import json

from django.views import View
from testapp.models import Mymodel
class Field_mixin(object):
    def field_resp(self,j_data):
        f_list=[]
        p_dict=json.loads(j_data)
        for data in p_dict:
            emp_data=data['fields']
            f_list.append(emp_data)
        j_data=json.dumps(f_list) 
        return HttpResponse(j_data,content_type='application/json',status=200)
    def getobject(self,id):
        try:
            emp_obj=Mymodel.objects.get(id=id)
        except BaseException:
            emp_obj={'msg':'please provide valid id'}
        return emp_obj




























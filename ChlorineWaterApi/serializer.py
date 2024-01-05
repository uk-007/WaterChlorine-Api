from rest_framework import serializers, fields
from .models import  UserMaster

class UserMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMaster
        #fields = "__all__"  
        exclude = ['id']
        
        
class validate_Stateid_param(serializers.Serializer):
    state_id = fields.IntegerField(min_value=0)        
    
    
    
class validate_siteStatus(serializers.Serializer):
    state_id = fields.IntegerField(min_value=0)
    district_id = fields.IntegerField(min_value=0)
    
    
    
    
class validate_statusPanel(serializers.Serializer):
    stateId = fields.IntegerField(min_value=0)
    districtId = fields.IntegerField(min_value=0)
    deviceNo = fields.CharField(allow_blank=False)                     #empty string will raise validation error
    
    
    
class validate_Map(serializers.Serializer):
    stateId = fields.IntegerField(min_value=0)
    districtId = fields.IntegerField(min_value=0)
    deviceNo = fields.CharField(allow_blank=False)
    orgId = fields.IntegerField(min_value=0) 
    
    
class validate_updateSetting(serializers.Serializer):
    commId = fields.IntegerField(min_value=0)
    device = fields.IntegerField(min_value=0)
    str1  =  fields.CharField(max_length=200)
    str2  =  fields.CharField(max_length=200)
      
            
            
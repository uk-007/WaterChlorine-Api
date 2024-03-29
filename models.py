# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class ChlorineapiLogin(models.Model):
#     userid = models.AutoField(db_column='Userid', primary_key=True)  # Field name made lowercase.
#     username = models.CharField(db_column='UserName', max_length=100)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'ChlorineApi_login'


# class ChlorinewaterChlorinedata(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
#     loginid = models.CharField(max_length=20)
#     pwd = models.CharField(db_column='Pwd', max_length=10)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'ChlorineWater_chlorinedata'


# class CommandList(models.Model):
#     id = models.IntegerField()
#     command_name = models.TextField(db_column='Command_Name', blank=True, null=True)  # Field name made lowercase.
#     value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
#     default_value = models.TextField(db_column='Default_Value', blank=True, null=True)  # Field name made lowercase.
#     dbdatetime = models.DateTimeField(db_column='DBDateTime', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Command_List'


# class Data(models.Model):
#     row_id = models.IntegerField(db_column='Row_id', blank=True, null=True)  # Field name made lowercase.
#     imei_no = models.CharField(db_column='IMEI_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     chlorine = models.CharField(db_column='Chlorine', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     waterpressure = models.CharField(db_column='WaterPressure', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     datasend = models.CharField(db_column='DataSend', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     pressure_limit = models.CharField(db_column='Pressure_Limit', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     signal_strength = models.CharField(db_column='Signal_Strength', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     rtctime = models.CharField(db_column='RTCTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     rtcdate = models.CharField(db_column='RTCDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     rtcdayno = models.CharField(db_column='RTCDayNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     battery_percentage = models.CharField(db_column='Battery_Percentage', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     battery_voltage = models.CharField(db_column='Battery_Voltage', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     mobile_no = models.CharField(db_column='Mobile_no', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dbdate = models.DateTimeField(db_column='DbDate', blank=True, null=True)  # Field name made lowercase.
#     localaddress = models.TextField(db_column='LocalAddress', blank=True, null=True)  # Field name made lowercase.
#     remoteaddress = models.TextField(db_column='RemoteAddress', blank=True, null=True)  # Field name made lowercase.
#     socktid = models.TextField(db_column='SocktID', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Data'


# class DeviceCommandMaster(models.Model):
#     site_id = models.IntegerField(db_column='Site_id', blank=True, null=True)  # Field name made lowercase.
#     device_id = models.IntegerField(db_column='Device_id', blank=True, null=True)  # Field name made lowercase.
#     command_id = models.IntegerField(db_column='Command_id', blank=True, null=True)  # Field name made lowercase.
#     command_value = models.CharField(db_column='Command_Value', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     dbdatetime = models.DateTimeField(db_column='DBDateTime', blank=True, null=True)  # Field name made lowercase.
#     socketid = models.CharField(db_column='SocketID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     flag = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Device_Command_Master'


# class DeviceCommandMaster2(models.Model):
#     site_id = models.IntegerField(db_column='Site_id', blank=True, null=True)  # Field name made lowercase.
#     device_id = models.IntegerField(db_column='Device_id', blank=True, null=True)  # Field name made lowercase.
#     command_id = models.IntegerField(db_column='Command_id', blank=True, null=True)  # Field name made lowercase.
#     command_value = models.CharField(db_column='Command_Value', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     dbdatetime = models.DateTimeField(db_column='DBDateTime', blank=True, null=True)  # Field name made lowercase.
#     socketid = models.CharField(db_column='SocketID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     flag = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Device_Command_Master2'


# class DeviceMaster(models.Model):
#     serial = models.CharField(db_column='Serial', max_length=20)  # Field name made lowercase.
#     char_per_unit = models.FloatField(blank=True, null=True)
#     devui = models.CharField(max_length=20, blank=True, null=True)
#     mul_factor = models.IntegerField(blank=True, null=True)
#     water_false_gas_true = models.SmallIntegerField(blank=True, null=True)
#     po_code = models.IntegerField(blank=True, null=True)
#     stateid = models.IntegerField(db_column='Stateid', blank=True, null=True)  # Field name made lowercase.
#     districid = models.IntegerField(db_column='Districid', blank=True, null=True)  # Field name made lowercase.
#     orgid = models.IntegerField(blank=True, null=True)
#     active = models.SmallIntegerField(blank=True, null=True)
#     dbdate = models.DateTimeField(db_column='DBDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Device_Master'


# class Districtmaster(models.Model):
#     name = models.CharField(max_length=50, blank=True, null=True)
#     region_id = models.IntegerField(blank=True, null=True)
#     active = models.BooleanField(blank=True, null=True)
#     dbdatetime = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'DistrictMaster'


# class Quickview(models.Model):
#     site_id = models.IntegerField(db_column='Site_id', blank=True, null=True)  # Field name made lowercase.
#     device_id = models.IntegerField(db_column='Device_id', blank=True, null=True)  # Field name made lowercase.
#     imei_number = models.CharField(db_column='IMEI_Number', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     chlorine = models.TextField(db_column='Chlorine', blank=True, null=True)  # Field name made lowercase.
#     waterpressure = models.TextField(db_column='WaterPressure', blank=True, null=True)  # Field name made lowercase.
#     datasend = models.TextField(db_column='DataSend', blank=True, null=True)  # Field name made lowercase.
#     pressure_limit = models.TextField(db_column='Pressure_Limit', blank=True, null=True)  # Field name made lowercase.
#     signal_strength = models.TextField(db_column='Signal_Strength', blank=True, null=True)  # Field name made lowercase.
#     rtctime = models.TextField(db_column='RTCTime', blank=True, null=True)  # Field name made lowercase.
#     rtcdate = models.TextField(db_column='RTCDate', blank=True, null=True)  # Field name made lowercase.
#     rtcdayno = models.TextField(db_column='RTCDayNo', blank=True, null=True)  # Field name made lowercase.
#     battery_percentage = models.TextField(db_column='Battery_Percentage', blank=True, null=True)  # Field name made lowercase.
#     battery_voltage = models.TextField(db_column='Battery_Voltage', blank=True, null=True)  # Field name made lowercase.
#     dbdate = models.DateTimeField(db_column='DbDate', blank=True, null=True)  # Field name made lowercase.
#     socketid = models.TextField(db_column='SocketID', blank=True, null=True)  # Field name made lowercase.
#     datareceive = models.DateTimeField(db_column='Datareceive', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'QuickView'


# class RoleMaster(models.Model):
#     role_id = models.AutoField(db_column='Role_id', primary_key=True)  # Field name made lowercase.
#     role_name = models.CharField(db_column='Role_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dbdatetime = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Role_Master'


# class RowData(models.Model):
#     data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
#     dbdate = models.DateTimeField(db_column='DBDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Row_Data'


# class RowDataFail(models.Model):
#     row_id = models.IntegerField(db_column='Row_id', blank=True, null=True)  # Field name made lowercase.
#     msg = models.TextField(db_column='MSG', blank=True, null=True)  # Field name made lowercase.
#     localaddress = models.CharField(db_column='LocalAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     remoteaddress = models.CharField(db_column='RemoteAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     socktid = models.CharField(db_column='SocktID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     dbdatetime = models.DateTimeField(db_column='DBDateTime', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Row_Data_fail'


# class SiteMaster(models.Model):
#     name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     device_id = models.IntegerField(db_column='Device_id', blank=True, null=True)  # Field name made lowercase.
#     orgid = models.IntegerField(blank=True, null=True)
#     lat = models.CharField(db_column='Lat', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     lon = models.CharField(db_column='Lon', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     mobileno = models.CharField(db_column='MobileNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
#     stateid = models.IntegerField(db_column='Stateid', blank=True, null=True)  # Field name made lowercase.
#     districid = models.IntegerField(db_column='Districid', blank=True, null=True)  # Field name made lowercase.
#     address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     active = models.SmallIntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
#     dbdatetime = models.DateTimeField(db_column='DBDateTime', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Site_Master'


# class Statemaster(models.Model):
#     name = models.CharField(max_length=50, blank=True, null=True)
#     orgid = models.IntegerField(blank=True, null=True)
#     active = models.BooleanField(blank=True, null=True)
#     dbdatetime = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'StateMaster'


# class TableRawdata(models.Model):
#     id = models.BigAutoField()
#     msg = models.TextField(db_column='MSG', blank=True, null=True)  # Field name made lowercase.
#     localaddress = models.CharField(db_column='LocalAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     remoteaddress = models.CharField(db_column='RemoteAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     socketid = models.CharField(db_column='SocketID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     timestamp = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Table_RawData'


# class UserMaster(models.Model):
#     name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     loginid = models.CharField(max_length=50, blank=True, null=True)
#     pwd = models.CharField(max_length=50, blank=True, null=True)
#     roleid = models.IntegerField(blank=True, null=True)
#     orgid = models.IntegerField(blank=True, null=True)
#     region = models.IntegerField(blank=True, null=True)
#     portion = models.IntegerField(blank=True, null=True)
#     user_group = models.IntegerField(blank=True, null=True)
#     stock_alltr = models.IntegerField(blank=True, null=True)
#     active = models.BooleanField(blank=True, null=True)
#     dbdatetime = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'User_Master'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class GlobalException(models.Model):
#     method_name = models.CharField(max_length=50, blank=True, null=True)
#     err_no = models.CharField(max_length=50, blank=True, null=True)
#     err_severity = models.CharField(max_length=50, blank=True, null=True)
#     err_state = models.CharField(max_length=50, blank=True, null=True)
#     err_procedure = models.CharField(max_length=50, blank=True, null=True)
#     err_line = models.CharField(max_length=50, blank=True, null=True)
#     err_msg = models.CharField(max_length=500, blank=True, null=True)
#     dbdatetime = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'global_exception'


# class HomeGeeksmodel(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     title = models.CharField(max_length=200)
#     description = models.TextField()

#     class Meta:
#         managed = False
#         db_table = 'home_geeksmodel'

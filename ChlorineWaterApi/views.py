
from django.shortcuts import render
from django.db import connections
from django.shortcuts import render , HttpResponse, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserMasterSerializer, validate_Stateid_param, validate_siteStatus, validate_statusPanel, validate_Map, validate_updateSetting
from rest_framework import status
from rest_framework.authentication import  BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes


# Create your views here.
@api_view(['GET'])
@authentication_classes([BasicAuthentication]) #giving this api basic auth security
@permission_classes([IsAuthenticated])     #isAuthenticated means only authenticated user with username and pswrd can use this api
def login_user(request):          #username and password for authentication is admin and admin
    return Response({"message":"this is home page"})
    


#api for user registration in which name,loginid, password is mandatory. other params such as roleid, portion, orgid is
#optional with default value of 1.
@api_view(['POST'])           #decorator that is making this function an api
def user_register(request):     
    try:
        data = request.data                          #request.data returns the parsed content of the request body
        serializer = UserMasterSerializer(data=data)
        print(data)
        if serializer.is_valid():
            print("inside if searizer. is valid")
            cursor = connections['default'].cursor()
            loginid = data['loginid']
            
            query= f"Exec UserRegistration_Py @loginid={loginid}"  #to check if loginid is not taken before
            
            cursor.execute(query)
           
            result = cursor.fetchone()
            
            if cursor.rowcount == 0:     
                
                
                print("*********")      
                
                
                serializer.save()
                serialized_data = serializer.data     #copying data of serializer into another dict serialized_data then deleting pswrd
                cursor.close()                        #from it and sendind serialized_data as resposne
                del serialized_data['pwd']       
                return Response({
                "message": "success",
                "data": serialized_data
                },status=200)
            else:
                return Response({"meassge":"loginid already taken."},status=409)    
        else:
            return Response({
                "message":"failed",
                "data":serializer.errors
            },status=400)    
        
    except Exception as e:
        print("%%%%%%%")
        return Response({"status":False,  
                         "message": str(e)
                        },status=500)
        
        
        

#api for login through loginid and password
@api_view(['POST'])         
def UserLogin(request):
    try:
        cursor = connections['default'].cursor()
        loginid = request.GET.get('LoginId')
        pwd =  request.GET.get('Password')
        if loginid==None or pwd==None :         #if wrong key is given while giving input
            print("incorrect parameter")         
            cursor.close()
            return Response({"message":"enter correct param"},status=417)
        if loginid == "" or pwd == "":        #if loginid or pswrd is left blank
            cursor.close()
            return Response({"message":"userid or password cannot be left blank"},status=400)
        
        print(loginid,pwd)
        
    
        
        
        query=f"Exec UserLogin_Py @loginid={loginid},@Password={pwd}"
        cursor.execute(query)
        result = cursor.fetchone()
        if cursor.rowcount == 0:
            return Response({"message":"Please enter valid loginid and password"
                            },status=401)
        else:
               
                return Response({"Name":result[0],
                                "Roleid":result[1],
                                "orgid":result[2],
                                "region":result[3],
                                "portion":result[4],
                                "user_group":result[5]},status=200)    
                
    except Exception as e:
        return Response({"message":str(e)},status=500) 
    
    

#api to get list of total states in database   
@api_view(['GET'])
def Get_state(request):
    try:
        cursor = connections['default'].cursor()
        query = "exec [dbo].[get_State_Py];"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        print(result)
   
        state_list = []
        for list in result:
            state_dict={}
            state_dict["name"]=list[1]
            state_dict["id"]= list[0]
            state_list.append(state_dict)
    
        print(state_list)
    
        return Response(state_list,status=200)
    except Exception as e:
        print("in exception block")
        return Response({"message":str(e)},status=404)  
    
    
    
    
#api to get list of cities which falls under particular state(state_id)     
@api_view(['POST'])   
def Get_City_List(request):
    try:
        state_id = request.GET.get("state_id")
        if state_id == None:
            return Response({"message":"Please enter correct parameter key."},status=400)
        if state_id == "":
            # if sateid is left blank by user
            return Response({"message":"state_id cannot be left blank"},status=400)
        
        serializer = validate_Stateid_param(data=request.query_params)    #using serializer to validate incoming query param.if valid state_id then
                                                                          #only send it for query execution
                                                                  
        if serializer.is_valid():
            print("sserializer is valid")
            print(state_id)
            cursor = connections['default'].cursor()
            query = f"exec [dbo].[GetCityList_Py] {state_id};"      
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) != 0:
                state_list = []
                for list in result:
                    state_dict={}
                    state_dict["name"]=list[1]
                    state_dict["id"]= list[0]
                    state_list.append(state_dict)
                 
                cursor.close()   
                return Response(state_list,status=200)
            else:
                return Response({"message":"No data found"},status=400)
            
            
        else:
            print("serializer not valid")    
           
            return Response({"message":"enter valid stateid"},status=400)
       
        
    except Exception as e:
        print(e)
        return Response({"mesaage":str(e)},status=400)
    
    


#api to get site status with arguments stateid and district id
@api_view(['POST'])
def Get_Site_Status(request):
    try:
        
        stateid = request.GET.get('state_id')
        districtid = request.GET.get('district_id')
            
        if stateid == None or districtid == None:
            return Response({"message":"please enter correct argument key"},status=400)
        serializer = validate_siteStatus(data = request.query_params)
        #print(serializer)
        if serializer.is_valid():
            print("serializer is valid")
            cursor = connections['default'].cursor()
            query = f"exec [dbo].[Get_Site_Status] {stateid}, {districtid};"      
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
            status_list = []
            
            for list in result:
                status_dict={}
                status_dict['Total'] = list[0]
                status_dict['Active'] = list[1]
                status_dict['NonActive'] = list[2]
                status_dict['Pending'] = list[3]
                status_list.append(status_dict)
                
                
            return Response(status_list,status=200)
            
        else:
            print("not valid")
            return  Response({"message":serializer.errors},status=400)   
        
    except Exception as e:
        return Response({"message":str(e)},status=500)   
    
    
    
    
#api to get command  list
@api_view(['GET'])
def Get_Command_List(request):
    try:
        # Get a database cursor from the 'default' database connection
        cursor = connections['default'].cursor()

        # Define the SQL query to execute the stored procedure
        query = "exec [dbo].[Get_Command_List];"

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the result rows
        result = cursor.fetchall()
        print("*****")
        print(result)
        print("%%%%%%%%%%%%%")

        # Close the cursor
        cursor.close()

        # Initialize a dictionary to store command data with Command_id as the key
        Command_dict = {}

        # Iterate through the result rows and create a dictionary for each command
        data = result
        hint_list = []
        n = len(data)  

        for row in result:
            Command_id = row[0]
            Command_Name = row[1]
            Number = row[4]


            if Command_id not in Command_dict:
                # Create a new entry in the dictionary for the Command_id
                Command_dict[Command_id] = {
                    "Command_id": Command_id,
                    "Command_Name": Command_Name,
                    "EditType": row[3],
                    "Number":Number,
                    "animation": "link",
                    "Text": {
                        "title": Command_Name,  # Use Command_Name as the title
                        # "hint1": "",
                        # "hint2": "",
                        "InputType": ""
                    }
                }


        # cursor = connections['default'].cursor()

        # # Define the SQL query to execute the stored procedure
        # query = f"exec [dbo].[Get_Command_Hint_List] {Command_id};"

        # # Execute the SQL query
        # cursor.execute(query)

        # # Fetch all the result rows
        # result = cursor.fetchall()
        # print("*****")
        # print(result)

        # # Close the cursor
        # cursor.close()

        # # Initialize a dictionary to store command data with Command_id as the key
        # Command_dict = {}

        # # Iterate through the result rows and create a dictionary for each command
        # data = result
        # hint_list = []
        # n = len(data)        
        # for i in range (0,n+1):
        #     Command_dict={
        #         "Text": {
        #             "title": Command_Name,  # Use Command_Name as the title
        #             "hint1": "",
        #             "hint2": "",
        #             "InputType": ""
        #         } 
        #     }          

            # Check if Number is 0, and update hint1
            if Number != 0:
                # You may need to replace this with the actual hint values from your result
                # for Number in result:
                #     Command_dict[Command_id]["Text"]["hint1"] = row[5]
                print(f"no is {Number}")
                cursor = connections['default'].cursor()
                query = f"select Hint_Name from [dbo].[Command_Hint_List] where Comd_list_Id = {Command_id};"  
                print(f"command id is {Command_id}")    
                cursor.execute(query)
                result = cursor.fetchall()
                print(result)
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
                l = len(result)
                #print(result[1][0])
                Command_dict[Command_id]["Text"]["hint"] = []
                print(f"l is {l}")
                ans_list = []
                for i in range(0,l):
                    #print(result[i][0])
                    ans_list.append(result[i][0])
                    
                #print(result[0][0])
                # for i in range(0,l):
                #     Command_dict[Command_id]["Text"]["hint"] = result[i]
                #     print(result[i])
                #Command_dict[Command_id]["Text"]["hint1"] = result
                # for ans in result:
                #     Command_dict[Command_id]["Text"]["hint"].append(ans)
                Command_dict[Command_id]["Text"]["hint"] = ans_list
                
            if Number == 0:
                del Command_dict[Command_id]["Text"]   
                          
                    

        # Convert the dictionary values to a list to match the desired format
        Command_list = list(Command_dict.values())

        # Return the command list as a JSON response with a 200 status code
        return Response(Command_list, status=200)

    except Exception as e:
        # Handle exceptions and return an error response with a 404 status code
        return Response({"message": str(e)}, status=404)
    
    
    
    
@api_view(['POST'])
def Get_Device_Status(request):
    try:
        
        stateid = request.GET.get('state_id')
        districtid = request.GET.get('district_id')
            
        if stateid == None or districtid == None:
            return Response({"message":"please enter correct argument key"},status=400)
        serializer = validate_siteStatus(data = request.query_params)
        #print(serializer)
        if serializer.is_valid():
            print("serializer is valid")
            cursor = connections['default'].cursor()
            query = f"exec [dbo].[Get_Device_Status] {stateid}, {districtid};"      
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
            status_list = []
            
            for list in result:
                status_dict={}
                status_dict['Total'] = list[0]
                status_dict['Active'] = list[1]
                status_dict['NonActive'] = list[2]
                status_dict['Pending'] = list[3]
                status_list.append(status_dict)
                
                
            return Response(status_list,status=200)
            
        else:
            print("not valid")
            return  Response({"message":serializer.errors},status=400)   
        
    except Exception as e:
        return Response({"message":str(e)},status=500) 
    
    
    
    
@api_view(['POST'])   
def getstatusPanel(request):
    stateId  = request.GET.get('stateId')  
    districtId  = request.GET.get('districtId')
    deviceNo  = request.GET.get('deviceNo')
    print(type(deviceNo))   
    
    print(stateId)
    print(districtId)
    print(deviceNo)
    
    if stateId==None or districtId==None or deviceNo==None:
        return Response({"message":"please enter valid parameter key"},status=400)
    
    serializer = validate_statusPanel(data = request.query_params)  
    if serializer.is_valid():
        print(serializer)
        print("serializer is valid")
        cursor = connections['default'].cursor()
        query = f"exec [dbo].[Show_Status_Panel] {stateId},{districtId},'{deviceNo}';"      
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        print(result)
        print(len(result))
        if len(result)==0:
            return Response({"message":"No data found"})
        else:
            panel_list=[]
            for list in result:
                panel_dict = {}
                panel_dict["id"] = list[0]
                panel_dict["name"] = list[1]
                panel_dict["serial"] = list[2]
                panel_dict["chlorine"] = list[3]
                panel_dict["waterPressure"] = list[4]
                panel_dict["batteryPercentage"] = list[5]
                panel_dict["batteryVoltage"] = list[6]
                panel_dict["signalStrength"] = list[7]
                panel_dict["mobileNo"] = list[8]
                
            panel_list.append(panel_dict)    
            
            return Response(panel_list)
        print(result)
        return Response({"message":"hello there"})
        
    else:
        print("serializer is not valid")
        return Response({"message":serializer.errors},status=400)
    
    
@api_view(['POST'])
def showMap(request):
    stateId = request.GET.get('stateId')
    districtId = request.GET.get('districtId')
    deviceNo = request.GET.get('deviceNo')
    orgId = request.GET.get('orgId')
    
    if stateId==None or districtId==None or deviceNo==None or orgId==None:
        return Response({"message":"please enter correct argument keys"},status=406)
    
    
    try:
        serializer = validate_Map(data = request.query_params)
        if serializer.is_valid():
            cursor = connections['default'].cursor()
            query = f"exec [dbo].[Show_Map] {stateId}, {districtId}, '{deviceNo}', {orgId};"
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
            print(len(result))
            if len(result) != 0:
                map_list = []
                for list in result:
                    map_dict = {}
                    map_dict['s_id'] = list[0]
                    map_dict['name'] = list[1]
                    map_dict['address'] = list[2]
                    map_dict['lat'] = list[3]
                    map_dict['lon'] = list[4]
                    map_dict['serial'] = list[5]
                    map_dict['chlorine'] = list[6]
                    map_dict['waterPressure'] = list[7]
                    map_dict['batteryVoltage'] = list[8]
                    map_dict['uptime'] = list[9]
                
                map_list.append(map_dict)
                return Response(map_list, status=200)
            else:
                return Response({"message":"No data found"},status=200)
        
        else:
            return Response({"message":serializer.errors},status=406)
        
    except Exception as e :
        return Response({"message": str(e)},status=417)   
    
    
    
     
    
    
@api_view(['GET'])    
def getSiteDevice(request):
    try:
        cursor = connections['default'].cursor()
        query = "exec [dbo].[Get_Site_Device]"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        print(len(result))
        siteDeviceList = []
        for list in result:
            ans_dict = {}
            ans_dict['id'] = list[0]
            ans_dict['name'] = list[1]
            siteDeviceList.append(ans_dict)
            
        return Response(siteDeviceList)
    
    except Exception as e:
        return Response({"message":str(e)},status=417)
    
    
 
 
@api_view(['POST'])   
def updateDeviceSetting(request):
    commId = request.GET.get('commId')
    device = request.GET.get('device')
    str1 =  request.GET.get('str1')  
    str2 = request.GET.get('str2')  
    
    if commId==None or device==None or str1==None or str2==None:
        return Response({"message":"Please spell correct argument key"},status=400)
    
    try:
        serializer = validate_updateSetting(data = request.query_params)
        if serializer.is_valid():
            cursor = connections['default'].cursor()
            query = f"exec Update_Device_Setting_Py {commId},{device},{str1},{str2};"
            cursor.execute(query)
            result = cursor.fetchone()
            return Response(result)
            
        else:
            return Response({"message":serializer.errors},status=400)
        
    except Exception as e :
        return Response({"message":str(e)},status=417)    
        
    
    
        
        
      
    
    

                  

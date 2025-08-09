from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Create your views here.

class IncomingDataView(APIView):
    # only recieves a post data sent's to particular destination
    def post(self , request ) :
        token = request.headers.get("cL-X-TOKEN")
        if not token:
            return Response({"message":"unautherized"},status=401)
        
        data = request.data
        
        if not isinstance(data , dict):
            return Response({"message": "Invalid Data"})
        
        try:
            account = Account.objects.get(secret_token=token)
        except Account.DoesNotExist :
            return Response({"message": "Invalid Token"}, status=404)
        
        for destination in account.destinations.all() :
            url = destination.url
            method = destination.method.upper()
            headers = destination.headers

            try:
                
                if method == "GET":
                    requests.get(url , params=data , headers=headers)
                elif method == "POST" :
                    res = requests.post(url , json=data , headers=headers)
                elif method == "PUT":
                    requests.put(url , json=data , headers=headers)
                    
            except Exception as e :
                print(f"failed to send message : {str(e)}")
        
        return Response({'message': 'data pushed successfully' } , status=status.HTTP_200_OK)

# create a user account with security tokens
class SaveAccount(APIView):
    def post(self , request):
        
        try:
            data = request.data
            email = data.get("email")
            name = data.get("name")
            
            account = Account.objects.create(
                email=email,
                name=name,
            )
            
            data = {
                "account_id" : account.account_id ,
                "secret_key" : account.secret_token
            }
            
            return Response({'message' : 'request for user Account saved successfully' , 'data' : data },status=200)
        
        except Exception as e :
            return Response({'error':str(e)},status=500)

# create destinations for the particular account
class CreateDestination(APIView):
    def post(self , request):
        try:
            account_id = request.data.get('account')
            url = request.data.get('url')
            method = request.data.get('method')
            headers = request.data.get('headers')

            if not all([account_id, url, method, headers]):
                return Response({'error': 'All fields (account, url, method, headers) are required.'}, status=400)

            try:
                account = Account.objects.get(account_id=account_id)
            except ObjectDoesNotExist:
                return Response({'error': 'Account not found.'}, status=404)

            destination = Destination.objects.create(
            
                account=account,
                url=url,
                method=method.upper(),
                headers=headers
            )

            return Response({
                'message': 'Destination created successfully',
                'destination_id': destination.id
            }, status=201)

        except Exception as e:
            return Response({'error': str(e)}, status=500)
        
# find destinations of account with account id
class GetDestinations(APIView):
    def get(self , reqeust , account_id):
        try: 
            print(account_id)
            account = Account.objects.get(account_id=account_id)
            destinations = account.destinations.all()
            
            data = [] 
            for d in destinations:
                data.append({
                    "id" : d.id,
                    "url": d.url,
                    "method": d.method,
                    "headers": d.headers
                })
                
            return Response({'account': account.email, 'destinations': data} , status=200)
        except Exception as e:
            return Response({'error': f"error while fetching destination : {str(e)}"},status=500)
        
# delete account along with all it's destinations
class DeleteAccount(APIView):
    def delete(self , request , account_id):
        try:
            
            account = Account.objects.get(account_id=account_id)
            account.delete()
            return Response({"message": "Account and its destinations deleted"}, status=200)
        
        except Account.DoesNotExist:
            return Response({"error": "Account not found"}, status=404)

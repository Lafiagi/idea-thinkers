from django.http import response
from authy.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


def login_user(data) -> list: 
  email = data['email']
  password= data['password']
  user = authenticate(email=email, password=password)
  status = 404
  if not user:
    return ['Wrong Email or Password', status]
  token, _ = Token.objects.get_or_create(user=user)
  user.save()
  status = 200
  return [{"token":token.key,"name": user.name.title()}, status]

def vailidate_user(email, phone)-> list:
  if(User.objects.filter(email = email)):
    status = 403
    return ['User with this Email Already Exist', status]

  if(User.objects.filter(phone_number =  phone)):
    status = 403
    return ['User with this Phone Number Already Exist', status]
  
  return True


def logout_user(request)-> None: 
    request.user.auth_token.delete()
    message = "Your now logged out, you can proceed to login"
    return message


def welcome_user(request)-> str: 
    welcome_msg = f"Welcome {request.user.name}, you are now logged in!"
    return welcome_msg



def create_user(request)-> list:
    data = request.data
    msg = vailidate_user(data['email'], data['phone_number'].replace(" ", ""))
    if(msg == True):
      user = User()
      user.email = data['email']
      user.first_name = data['first_name']
      user.last_name = data['last_name']
      user.phone_number = data['phone_number'].replace(" ", "")
      user.set_password(data['password'])
      user.save()
      token, _ = Token.objects.get_or_create(user=user)
      return [token.key, user.first_name, user.last_name, user.email, user.phone_number]
    else:
      return msg
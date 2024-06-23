from django.db import models

# Create your models here.
class user1:
    userid:int
    username:str
    password:str
    email:str
    mobile:int    
    address:str
    

class land1:
    land_id:int
    survey_number:str
    land_image:str
    land_size:str
    land_price:int   
    land_location:str
    land_seller:str
    seller_mobile:int
    

class seller1:
    seller_id:int
    Name:str
    Email:str
    Gender:str
    Dob:str
    Mobile:int
    City:str
    Password:str


class sellerland1:
    LAND_ID:id
    SELLER_ID:id
    SURVEY_NUMBER:str
    LAND_SIZE:str
    LAND_PRICE:str
    LAND_LOCATION:str
    LAND_SELLER:str
    SELLER_MOBILE:str
    LAND_IMAGE:str


class complaint1:
    id:int
    Full_Name:str
    Email_Address:str
    Telephone_Number:int
    Complaint:str







from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector
import smtplib
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
from django.core.files.storage import FileSystemStorage
from .models import *
#return HttpResponse("<h3> welcome</h3>")

# Create your views here.
#def index (request):
    #return HttpResponse("<h3> welcome</h3>")
    #return render(request,"registration.html")
#def registration (request):
    #return render(request,"registration.html")
#def login (request):
    #return render(request,"login.html")
def about (request):
    if "email" in request.session:
        return render(request,"about.html")
    else:
        return render(request,'userlogin.html')
def contact (request):
    if "email" in request.session:
        return render(request,"contact.html")
    else:
        return render(request,'userlogin.html')
def home (request):
    return render(request,"home.html")
def gallery (request):
        return render(request,"gallery.html")
def index (request):
    if "email" in request.session:
        return render(request,"index.html")
    else:
        return render(request,'userlogin.html')
def properties (request):
    if "email" in request.session:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        )
        mycursor = mydb.cursor()
        #retrive post details       
        mycursor.execute("select * from landdetails")
        result=mycursor.fetchall()
        landdetails=[]
        for x in result:
            land=land1()
            land.land_id=x[0]
            land.survey_number=x[1]
            land.land_image=x[2]
            land.land_size=x[3]
            land.land_price=x[4]
            land.land_location=x[5]
            land.land_seller=x[6]
            land.seller_mobile=x[7]
            landdetails.append(land)
        return render(request,"properties.html",{'landdetails':landdetails})
    else:
        return render(request,'userlogin.html')
def service (request):
    if "email" in request.session:
        return render(request,"service.html")
    else:
        return render(request,'userlogin.html')
def admin_dashboard (request):
    if "email" in request.session:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        )
        mycursor = mydb.cursor()
        #retrive post details       
        mycursor.execute("select * from userdetails")
        result=mycursor.fetchall()
        mycursor.execute("select * from sellerdetails")
        result1=mycursor.fetchall()
        mycursor.execute("select * from landdetails")
        result2=mycursor.fetchall()
        mycursor.execute("select * from sellerlanddetails")
        result3=mycursor.fetchall()
        count=0
        count1=0
        count2=0
        count3=0
        for x in result:
            count+=1
        for y in result1:
            count1+=1
        for z in result2:
            count2+=1
        for a in result3:
            count3+=1
        return render(request,"admin_dashboard.html",{'count':count,'count1':count1,'count2':count2,'count3':count3})
    else:
        return render(request,'adminlogin.html')
    

def land_types (request):
    if "email" in request.session:
        return render(request,"land_types.html")
    else:
        return render(request,'adminlogin.html')
def message_admin (request):
    if "email" in request.session:
        return render(request,"message_admin.html")
    else:
        return render(request,'adminlogin.html')
def total_users(request):
    if "email" in request.session:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        )
        mycursor = mydb.cursor()
        #retrive post details       
        mycursor.execute("select * from userdetails")
        result=mycursor.fetchall()
        userdetails=[]
        user=None
        count=0
        for x in result:
            user=user1()
            user.userid=x[0]
            user.username=x[1]
            user.password=x[2]
            user.email=x[3]
            user.mobile=x[4]
            user.address=x[5]
            userdetails.append(user)
            count+=1
        return render(request,"total_users.html",{'userdetails':userdetails})
    else:
        return render(request,'adminlogin.html')
def total_lands(request):
    if "Email" in request.session:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        )
        mycursor = mydb.cursor()
        #retrive post details       
        mycursor.execute("select * from landdetails")
        result=mycursor.fetchall()
        landdetails=[]
        for x in result:
            land=land1()
            land.land_id=x[0]
            land.survey_number=x[1]
            land.land_image=x[2]
            land.land_size=x[3]
            land.land_price=x[4]
            land.land_location=x[5]
            land.land_seller=x[6]
            land.seller_mobile=x[7]
            landdetails.append(land)
        return render(request,"total_lands.html",{'landdetails':landdetails})
    else:
        return render(request,'adminlogin.html')
def total_sellerlands(request):
    if "Email" in request.session:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        )
        mycursor = mydb.cursor()
        #retrive post details       
        mycursor.execute("select * from sellerlanddetails")
        result=mycursor.fetchall()
        sellerlanddetails=[]
        for x in result:
            sellerland=sellerland1()
            sellerland.LAND_ID=x[0]
            sellerland.Seller_ID=x[1]
            sellerland.SURVEY_NUMBER=x[2]
            sellerland.LAND_SIZE=x[3]
            sellerland.LAND_PRICE=x[4]
            sellerland.LAND_LOCATION=x[5]
            sellerland.LAND_SELLER=x[6]
            sellerland.SELLER_MOBILE=x[7]
            sellerland.LAND_IMAGE=x[8]
            sellerlanddetails.append(sellerland)
        return render(request,"total_sellerlands.html",{'sellerlanddetails':sellerlanddetails})
    else:
        return render(request,'sellerlogin.html')
def sellerdash(request):
        if "Email" in request.session:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="realestate"
            )
            mycursor = mydb.cursor()
            #retrive post details       
            mycursor.execute("select * from sellerlanddetails")
            result=mycursor.fetchall()
            sellerlanddetails=[]
            sellerland=None
            count=0
            for x in result:
                sellerland=sellerland1()
                sellerland.LAND_ID=x[0]
                sellerland.LAND_NAME=x[1]
                sellerland.LAND_SIZE=x[2]
                sellerland.LAND_PRICE=x[3]
                sellerland.LAND_LOCATION=x[4]
                sellerland.LAND_SELLER=x[5]
                sellerland.SELLER_MOBILE=x[6]
                sellerland.LAND_IMAGE=x[7]
                count=count+1
                sellerlanddetails.append(sellerland)
            return render(request,"sellerdash.html",{'count':count})
        else:
            return render(request,'sellerlogin.html')
def sellerlands(request):
    if "Email" in request.session:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        )
        mycursor = mydb.cursor()
        #retrive post details       
        mycursor.execute("select * from sellerlanddetails")
        result=mycursor.fetchall()
        sellerlanddetails=[]
        for x in result:
            sellerland=sellerland1()
            sellerland.LAND_ID=x[0]
            sellerland.Seller_ID=x[1]
            sellerland.SURVEY_NUMBER=x[2]
            sellerland.LAND_SIZE=x[3]
            sellerland.LAND_PRICE=x[4]
            sellerland.LAND_LOCATION=x[5]
            sellerland.LAND_SELLER=x[6]
            sellerland.SELLER_MOBILE=x[7]
            sellerland.LAND_IMAGE=x[8]
            sellerlanddetails.append(sellerland)
        return render(request,"sellerlands.html",{'sellerlanddetails':sellerlanddetails})
    else:
        return render(request,'sellerlogin.html')
def adminlogin(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        )
        mycursor = conn.cursor()
        #retrive post details       
        
        Email=request.POST['email']
        Password=request.POST['password']     
           
        mycursor.execute("select * from admin where email='"+Email+"' and password='"+Password+"'")
        result=mycursor.fetchone()
        if(result!=None):
            request.session['email'] = Email
            return redirect('admin_dashboard')    
        else:
            return render(request,'adminlogin.html',{'status':'invalid credentials'})
    return render(request,'adminlogin.html')
def sellerregistration(request):
    return render(request,"sellerregistration.html")
def adminprofile(request):
    return render(request,"adminprofile.html")
def userprofile(request):
    return render(request,"userprofile.html")
def sellerprofile(request):
    return render(request,"sellerprofile.html")
def total_sellers(request):
    if "Email" in request.session:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        )
        mycursor = mydb.cursor()
        #retrive post details       
        mycursor.execute("select * from sellerdetails")
        result=mycursor.fetchall()
        sellerdetails=[]
        for x in result:
            seller=seller1()
            seller.sellerid=x[0]
            seller.Name=x[1]
            seller.Email=x[2]
            seller.Gender=x[3]
            seller.Dob=x[4]
            seller.Mobile=x[5]
            seller.City=x[6]
            seller.Password=x[7]
            sellerdetails.append(seller)
        return render(request,"total_sellers.html",{'sellerdetails':sellerdetails})
    else:
        return render(request,'adminlogin.html')
def registration (request):
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        ) 
        mycursor =conn.cursor()
        #retrive post details       
        username=request.POST['username'] 
        password=request.POST['password'] 
        email=request.POST['email']    
        mobile=request.POST['mobile']
        address=request.POST['address']     
        mycursor.execute("insert into userdetails(username,password,email,mobile,address) values('"+username+"','"+password+"','"+email+"','"+mobile+"','"+address+"')")
        conn.commit()
        return render(request,'registration.html',{'status':'registered'})  
    else:
        
         
        return render(request,'registration.html')

def edituser(request,userid):
    if(request.method=='POST'):
        con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="realestate"
        )
        newcur=con.cursor()
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        address=request.POST["address"]
        newcur.execute("update userdetails set username='"+username+"', password='"+password+"',email='"+email+"',mobile='"+mobile+"',address='"+address+"' where userid='"+str(userid)+"'")
        con.commit()
        return redirect("total_users")
    else:            
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        )
        mycursor = mydb.cursor()
        #retrive post details       
        mycursor.execute("select * from userdetails where userid="+str(userid))
        result=mycursor.fetchone()
        user=user1()
        user.userid=result[0]
        user.username=result[1]
        user.password=result[2]
        user.email=result[3]
        user.mobile=result[4]
        user.address=result[5]
        return render(request,'edituser.html',{'user':user})
    
def editland(request,land_id):
    if(request.method=='POST'):
        con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="realestate"
        )
        newcur=con.cursor()
        survey_number=request.POST["survey_number"]
        land_image=request.POST["land_image"]
        land_size=request.POST["land_size"]
        land_price=request.POST["land_price"]
        land_location=request.POST["land_location"]
        land_seller=request.POST["land_seller"]
        seller_mobile=request.POST["seller_mobile"]
        newcur.execute("update landdetails set survey_number='"+survey_number+"', land_image='"+land_image+"',land_size='"+land_size+"',land_price='"+land_price+"',land_location='"+land_location+"',land_seller='"+land_seller+"',seller_mobile='"+seller_mobile+"' where land_id='"+str(land_id)+"'")
        con.commit()
        return redirect("total_lands")
    else:            
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        )
        mycursor = mydb.cursor()
        #retrive post details       
        mycursor.execute("select * from landdetails where land_id="+str(land_id))
        result=mycursor.fetchone()
        land=land1()
        land.land_id=result[0]
        land.survey_number=result[1]
        land.land_image=result[2]
        land.land_size=result[3]
        land.land_price=result[4]
        land.land_location=result[5]
        land.land_seller=result[6]
        land.seller_mobile=result[7]
        return render(request,'editland.html',{'land':land}) 

def editsellerland(request,land_id):
    if(request.method=='POST'):
        con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="realestate"
        )
        newcur=con.cursor()
        survey_number=request.POST["survey_number"]
        land_image=request.POST["land_image"]
        land_size=request.POST["land_size"]
        land_price=request.POST["land_price"]
        land_location=request.POST["land_location"]
        land_seller=request.POST["land_seller"]
        seller_mobile=request.POST["seller_mobile"]
        newcur.execute("update sellerlanddetails set survey_number='"+survey_number+"',land_size='"+land_size+"',land_price='"+land_price+"',land_location='"+land_location+"',land_seller='"+land_seller+"',seller_mobile='"+seller_mobile+"',land_image='"+land_image+"' where land_id='"+str(land_id)+"'")
        con.commit()
        return redirect("sellerlands")
    else:            
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        )
        mycursor = mydb.cursor()
        #retrive post details       
        mycursor.execute("select * from sellerlanddetails where land_id="+str(land_id))
        result=mycursor.fetchone()
        sellerland=sellerland1()
        sellerland.land_id=result[0]
        sellerland.survey_number=result[1]
        sellerland.land_size=result[2]
        sellerland.land_price=result[3]
        sellerland.land_location=result[4]
        sellerland.land_seller=result[5]
        sellerland.seller_mobile=result[6]
        sellerland.land_image=result[7]
        return render(request,'editsellerland.html',{'sellerland':sellerland}) 
def editseller(request,seller_id):
    if(request.method=='POST'):
        con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="realestate"
        )
        newcur=con.cursor()
        Name=request.POST["Name"]
        Email=request.POST["Email"]
        Gender=request.POST["Gender"]
        Dob=request.POST["Dob"]
        Mobile=request.POST["Mobile"]
        City=request.POST["City"]
        Password=request.POST["Password"]
        newcur.execute("update sellerdetails set Name='"+Name+"', Email='"+Email+"',Gender='"+Gender+"',Dob='"+Dob+"',Mobile='"+Mobile+"',City='"+City+"',Password='"+Password+"' where seller_id='"+str(seller_id)+"'")
        con.commit()
        return redirect("total_sellers")
    else:            
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        )
        mycursor = mydb.cursor()
        #retrive post details       
        mycursor.execute("select * from sellerdetails where seller_id="+str(seller_id))
        result=mycursor.fetchone()
        seller=seller1()
        seller.sellerid=result[0]
        seller.Name=result[1]
        seller.Email=result[2]
        seller.Gender=result[3]
        seller.Dob=result[4]
        seller.Mobile=result[5]
        seller.City=result[6]
        seller.Password=result[7]
        return render(request,'editseller.html',{'seller':seller})
    
def userlogin (request):
    if request.method == 'POST':
            conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="realestate"
            )
            mycursor = conn.cursor()
            #retrive post details       
        
            Email=request.POST['email']
            Password=request.POST['pwd']     
           
            mycursor.execute("select * from userdetails where email='"+Email+"' and password='"+Password+"'")
            result=mycursor.fetchone()
            if(result!=None):
                request.session['email'] = Email
                return redirect('index')
                #redirect('sellerregistration')
            else:
             return render(request,'userlogin.html',{'status':'invalid credentials'})    
    else:
        return render(request,'userlogin.html')
def sellerregistration (request):
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        ) 
        mycursor =conn.cursor()
        #retrive post details       
        Name=request.POST['Name']  
        Email=request.POST['Email']
        Gender=request.POST['Gender']     
        Dob=request.POST['Dob']
        Mobile=request.POST['Mobile']     
        City=request.POST['City']
        Password=request.POST['Password']
        mycursor.execute("insert into sellerdetails(Name,Email,Gender,Dob,Mobile,City,Password) values('"+Name+"','"+Email+"','"+Gender+"','"+Dob+"','"+Mobile+"','"+City+"','"+Password+"')")
        conn.commit()
        return redirect('sellerlogin')
    else:
        return render(request,'sellerregistration.html') 
    
def sellerlogin (request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        )
        mycursor = conn.cursor()
        #retrive post details       
    
        Email=request.POST['Email']
        Password=request.POST['Password']     
        
        mycursor.execute("select * from sellerdetails where Email='"+Email+"' and Password='"+Password+"'")
        result=mycursor.fetchone()
        if(result!=None):
            request.session['Email'] = Email
            return redirect('sellerdash')
            #redirect('sellerregistration')
        else:
            return render(request,'sellerlogin.html',{'status':'invalid credentials'})    
    else:
        return render(request,'sellerlogin.html')
        
    
def add_lands(request) :
    if "Email" in request.session:
        if request.method == 'POST' and request.FILES['myfile']: 
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            if request.method == 'POST' :     
                conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="realestate"
                ) 
                mycursor =conn.cursor()
                #retrive post details       
                survey_number =request.POST['survey_number']  
                Size=request.POST['land_size'] 
                Price=request.POST['land_price'] 
                Location=request.POST['land_location']
                Landseller=request.POST['land_seller']
                Sellermobile=request.POST['seller_mobile']
                mycursor.execute("insert into landdetails(survey_number,land_size,land_price,land_location,land_seller,seller_mobile,land_image) values('"+survey_number+"','"+Size+"','"+Price+"','"+Location+"','"+Landseller+"','"+Sellermobile+"','"+filename+"')")
                conn.commit()
                return redirect('add_lands')
        return render(request,'add_lands.html')
    else:
        return render(request,'adminlogin.html')
def selleraddland(request) :
        if 'Email' in request.session:
            if request.method == 'POST' and request.FILES['myfile']: 
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)    
                conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="realestate"
                ) 
                mycursor =conn.cursor()
                #retrive post details       
                Name =request.POST['land_name']  
                Size=request.POST['land_size'] 
                Price=request.POST['land_price'] 
                Location=request.POST['land_location']
                Landseller=request.POST['land_seller']
                Sellermobile=request.POST['seller_mobile']
                mycursor.execute("insert into sellerlanddetails(land_name,land_size,land_price,land_location,land_seller,seller_mobile,land_image) values('"+Name+"','"+Size+"','"+Price+"','"+Location+"','"+Landseller+"','"+Sellermobile+"','"+filename+"')")
                conn.commit()
                return redirect('sellerlands')
            return render(request,'selleraddland.html')
        else:
            return render(request,'sellerlogin.html')

def logout(request):
    del request.session['Email']
    request.session.modified = True
    return render(request,'sellerlogin.html')
def signout(request):
    del request.session['email']
    request.session.modified = True
    return render(request,'adminlogin.html')
def logoff(request):
    del request.session['email']
    request.session.modified = True
    return render(request,'userlogin.html')
def change_password(request):
   # return HttpResponse("<h3>Welcome REMS</h3>")
    if request.method == 'POST':

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="realestate"
        )
        mycursor = conn.cursor()
        # retrive post details
        otp = request.POST['otp-code']
        npwd = request.POST['new-password']
        mycursor.execute("select email from forget where otp='"+otp+"'")
        result=mycursor.fetchone()
        em=result[0]
        #mail='poojithadonakonda@gmail.com'
        if(result!=None):
            mycursor = conn.cursor()
            mycursor.execute("UPDATE userdetails SET password='"+npwd+"' WHERE email='"+em+"'")
            conn.commit()
            return render(request, 'userlogin.html', {'status':'success'})    
        else:
            return render(request,'change_password.html',{'status':'invalid otp'})  

def forget_password(request): 
    if request.method == 'POST':
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="realestate"
        )
        mycursor = conn.cursor()
        # retrive post details
        email = request.POST['email']
        #for otp in range(0,4):
        otp=str(random.randint(1000,9999))

        mycursor.execute("insert into forget(email,otp) values('"+email+"','"+otp+"')")
        conn.commit()
        #result = mycursor.fetchone()
        #pwd=str(result)
        #if (result != None):
            # SMTP server configuration
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'archanaarchu5757@gmail.com'
# for App Password enable 2-step verification then u can create app password
        smtp_password = 'nezgvusoghizblcr'

# Email content
        subject = 'Password recovery'
        body = 'This is a Password recovery email sent from kits.'+'One time Password '+ otp
        sender_email = 'archanaarchu5757@gmail.com'
        receiver_email = email

# Create a message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            return render(request, 'change_password.html', {'status': 'Password sent to given mail ID'})
        
    else:
        return render(request, 'forget_password.html')
def deleteuser(request,userid):        
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="realestate"
    ) 
    mycursor =conn.cursor()
    mycursor.execute("delete from userdetails where userid='"+userid+"'")
    return render(request,'total_users.html')
def deleteland(request,land_id):        
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="realestate"
    ) 
    mycursor =conn.cursor()
    mycursor.execute("delete from landdetails where land_id='"+land_id+"'")
    return redirect("total_lands")
def deleteseller(request,sellerid):        
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="realestate"
    ) 
    mycursor =conn.cursor()
    mycursor.execute("delete from sellerdetails where sellerid='"+sellerid+"'")
    conn.commit()
    return redirect("total_sellers")
def deletesellerland(request,land_id):        
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="realestate"
    ) 
    mycursor =conn.cursor()
    mycursor.execute("delete from sellerlanddetails where land_id='"+land_id+"'")
    return redirect("sellerlands")
def change_password(request):
   # return HttpResponse("<h3>Welcome REMS</h3>")
    if request.method == 'POST':

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="realestate"
        )
        mycursor = conn.cursor()
        # retrive post details
        otp = request.POST['otp-code']
        npwd = request.POST['new-password']
        mycursor.execute("select email from forget where otp='"+otp+"'")
        result=mycursor.fetchone()
        em=result[0]
        #mail='poojithadonakonda@gmail.com'
        if(result!=None):
            mycursor = conn.cursor()
            mycursor.execute("UPDATE sellerdetails SET password='"+npwd+"' WHERE email='"+em+"'")
            conn.commit()
            return render(request, 'sellerlogin.html', {'status':'success'})    
        else:
            return render(request,'change_password.html',{'status':'invalid otp'})  

def forget_password(request): 
    if request.method == 'POST':
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="realestate"
        )
        mycursor = conn.cursor()
        # retrive post details
        email = request.POST['email']
        #for otp in range(0,4):
        otp=str(random.randint(1000,9999))

        mycursor.execute("insert into forget(email,otp) values('"+email+"','"+otp+"')")
        conn.commit()
        #result = mycursor.fetchone()
        #pwd=str(result)
        #if (result != None):
            # SMTP server configuration
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'archanaarchu5757@gmail.com'
# for App Password enable 2-step verification then u can create app password
        smtp_password = 'nezgvusoghizblcr'

# Email content
        subject = 'Password recovery'
        body = 'This is a Password recovery email sent from REMS.'+'One time Password '+ otp
        sender_email = 'archanaarchu5757@gmail.com'
        receiver_email = email

# Create a message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            return render(request, 'change_password.html', {'status': 'Password sent to given mail ID'})
        
    else:
        return render(request, 'forget_password.html')
def change_password(request):
   # return HttpResponse("<h3>Welcome REMS</h3>")
    if request.method == 'POST':

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="realestate"
        )
        mycursor = conn.cursor()
        # retrive post details
        otp = request.POST['otp-code']
        npwd = request.POST['new-password']
        mycursor.execute("select email from forget where otp='"+otp+"'")
        result=mycursor.fetchone()
        em=result[0]
        #mail='poojithadonakonda@gmail.com'
        if(result!=None):
            mycursor = conn.cursor()
            mycursor.execute("UPDATE admin SET password='"+npwd+"' WHERE email='"+em+"'")
            conn.commit()
            return render(request, 'adminlogin.html', {'status':'success'})  
        else:
            return render(request,'change_password.html',{'status':'invalid otp'})  

def forget_password(request): 
    if request.method == 'POST':
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="realestate"
        )
        mycursor = conn.cursor()
        # retrive post details
        email = request.POST['email']
        #for otp in range(0,4):
        otp=str(random.randint(1000,9999))

        mycursor.execute("insert into forget(email,otp) values('"+email+"','"+otp+"')")
        conn.commit()
        #result = mycursor.fetchone()
        #pwd=str(result)
        #if (result != None):
            # SMTP server configuration
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'archanaarchu5757@gmail.com'
# for App Password enable 2-step verification then u can create app password
        smtp_password = 'nezgvusoghizblcr'

# Email content
        subject = 'Password recovery'
        body = 'This is a Password recovery email sent from REMS.'+'One time Password '+ otp
        sender_email = 'archanaarchu5757@gmail.com'
        receiver_email = email

# Create a message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            return render(request, 'change_password.html', {'status': 'Password sent to given mail ID'})
        
    else:
        return render(request, 'forget_password.html')

def complaint(request) :
    if "email" in request.session:
            if request.method == 'POST' :     
                conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="realestate"
                ) 
                mycursor =conn.cursor()
                #retrive post details       
                Full_Name =request.POST['Full_Name']  
                Email_Address=request.POST['Email_Address'] 
                Telephone_Number=request.POST['Telephone_Number'] 
                Complaint=request.POST['Complaint']
                mycursor.execute("insert into complaints(Full_Name,Email_Address,Telephone_Number,Complaint) values('"+Full_Name+"','"+Email_Address+"','"+Telephone_Number+"','"+Complaint+"')")
                conn.commit()
                return redirect('complaint')
            return render(request,'complaint.html')
    else:
        return render(request,'userlogin.html')
def complaints(request):
    if "Email" in request.session:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="realestate"
        )
        mycursor = mydb.cursor()
        #retrive post details       
        mycursor.execute("select * from complaints")
        result=mycursor.fetchall()
        complaints=[]
        for x in result:
            complaint=complaint1()
            complaint.id=x[0]
            complaint.Full_Name=x[1]
            complaint.Email_Address=x[2]
            complaint.Telephone_Number=x[3]
            complaint.Complaint=x[4]
            complaints.append(complaint)
        return render(request,"complaints.html",{'complaints':complaints})
    else:
        return render(request,'adminlogin.html')

               

#!C:/Users/Naveenkumar/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi,cgitb

cgitb.enable()
conn=pymysql.connect(host="Localhost", user="root", password="", database="student_registration")
cur=conn.cursor()

form=cgi.FieldStorage()
userid=form.getvalue("id")


q=""" select * from sturegister where id='%s' """ %(userid)
cur.execute(q)
res=cur.fetchall()

for i in res:
    print("""
       <!DOCTYPE html>
       <html lang="en">
       <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Sports addicts</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,900;1,400&display=swap');

                body{
                    margin: 0px;
                    padding: 0px;
                    box-sizing: border-box;
                    font-family: 'Poppins', sans-serif;
                }
                header nav{
                    position: sticky;
                    top:0px;
                    left:0px;
                    z-index: 10000;
                    padding: .5rem 5rem;
                background-color: #F50057 !important;
                }
                
                /* logo */
                
                header nav .navbar-brand{
                    font-size: 25px;
                    font-weight: 800;
                }
                
                 /* menus */
                 
                header nav .collapse .nav .nav-item .nav-link{
                    border-radius: 10px;
                }
                header nav .collapse .nav .nav-item .nav-link:hover{
                    color:#F50057 !important;
                    background-color: white !important;
                }
                header nav .container-fluid #bs{
                    background-color: #FF4081;
                    color:#fbfbfb;
                    border-radius: 50%%;
                    width:40px;height:40px;
                    border:none;
                    font-weight: 600;
                }
                
                .dropdown .dropdown-menu{
                    padding: 0px;
                    margin: 0px;
                }
                header nav .dropdown .dropdown-menu *{
                    background-color: #F50057 !important;
                    color:white !important;
                }
                header nav .dropdown .dropdown-menu .dropdown-item{
                    border-bottom: 2px solid white;
                    border-radius: 0px;
                    padding: 1.2rem 2rem;
                    font-weight: 500;
                }
                header nav .dropdown .dropdown-menu .d-items{
                    border: none;
                }
                
                        /* media queries */
                        /* for navbar */
                        
                @media (min-width:991px) and (max-width:1053px){
                    header nav{
                        font-size: small;
                    }
                }
                @media (min-width:300px) and (max-width:990px){
                    header nav{
                        padding: 0px;
                    } 
                } 
                
                     /* dashicon */
                
                @media  screen and (min-width:992px) {
                .button{
                    position: absolute;
                    right:10%%;
                    top:32%%;
                }
                }
                @media  screen and (max-width:380px){
                    header nav .navbar-brand{
                    font-size: 18px;
                    font-weight: 800;
                }
                header nav .container-fluid .navbar-toggler *{
                    width: 20px;
                    height:20px;
                }
                }
        
                        /* profile reg style */


                .definitions #editprofile input{
                    outline: none;
                    border-color:#fffcfd;
                    background-color: #F50057;
                    color: #fcfbfb;
                    border-radius: 10px;
                    height: 3rem;
                    font-weight: 500;
                    letter-spacing: 2px;
                }
                .definitions #editprofile label{
                    color: #F50057;
                    font-weight: 500;
                }
                        
                        /* dashboard */
                        /* definitions */
                        
                @media screen and (min-width:992px) {
                    #dashboard .container-fluid .row .definitions{
                    height:90vh;
                    overflow: auto;
                }
                }
                
                /* upcoming events */
                
                #upcomevents{
                    background-color: rgb(255, 255, 255) !important;
                } 
                #upcomevents h1{
                    color:#F50057 !important;
                    font-weight: 600;
                    letter-spacing: 3px;
                    text-transform: uppercase;
                }
                #upcomevents .card img{
                    border-top-left-radius: 20px;
                    border-top-right-radius: 20px;
                }
                #upcomevents .card{
                    background-color: #FF4081 !important;
                    color: rgb(255, 255, 255) !important;
                    border-radius: 20px !important;
                    border-color: #F50057;
                }
                #upcomevents .card .card-body h5{
                    letter-spacing: 3px;
                }
                #upcomevents .card .card-body .dateandtiming{
                    display: flex;
                    justify-content: space-evenly;
                    background-color: #F50057;
                    border-radius: 10px;
                    padding: 1rem;
                }
                #upcomevents .card .card-body .dateandtiming .date{
                    border-right: 2px solid white;
                    padding-right: 1rem;
                    margin-right: .5rem;
                }
                
                        /* completed events */
                
                #completedevents{
                    background-color: rgb(255, 255, 255) !important;
                }
                #completedevents h1{
                    color:#F50057 !important;
                    font-weight: 600;
                    letter-spacing: 3px;
                    text-transform: uppercase;
                }
                #completedevents .card img{
                    border-top-left-radius: 20px;
                    border-top-right-radius: 20px;
                }
                #completedevents .card{
                    background-color: #FF4081 !important;
                    color: white !important;
                    border-radius: 20px !important;
                    border-color: #F50057;
                }
                #completedevents .card .card-body h5{
                    letter-spacing: 3px;
                }
                #completedevents .card .card-body .dateandtiming{
                    display: flex;
                    justify-content: space-evenly;
                    background-color: #F50057;
                    border-radius: 10px;
                    padding: 1rem;
                }
                #completedevents .card .card-body .dateandtiming .date{
                    border-right: 2px solid white;
                    padding-right: 1rem;
                    margin-right: .5rem;
                }
                @media screen and (max-width:430px){
                    #completedevents .card{
                        width:100%% !important;
                        
                    }
                    
                    #completedevents {
                        padding:0px !important;
                    }
                    #upcomevents{
                        padding:0px !important;
                    }
                    #upcomeevents .card{
                        width:100%% !important;
                    }
                }
                
                    /* footer */
                
                footer .container-fluid{
                    background-color: #F50057 !important;
                }
                footer .container-fluid b a{
                    text-decoration: none;
                    color:antiquewhite !important;
                    color: white !important;
                    border-bottom: 3px solid transparent;
                    border-radius:2px;
                }
                footer .container-fluid b a:hover{
                    border-bottom: 3px solid white;
                    transition: .3s;
                }
                footer .container-fluid .menu{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                footer .container-fluid .social{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                footer .container-fluid .social img{
                    background-color: #f9f9f9 !important;
                    padding: 10px;
                    border-radius: 45%%;
                }
                
                @media screen and (min-width:0px) and (max-width:992px){
                    footer .container-fluid .row{
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                    }
                    footer .container-fluid .menu{
                        margin: 4rem 0rem;
                        flex-direction: column;
                    }
                    footer .container-fluid .menu b{
                        margin-bottom: 3rem;
                    }
                }


    </style>
</head>
<body>

    <!--header -->
    
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark">
            <div class="container-fluid">
            
              <!-- logo -->
              
              <a class="navbar-brand" href="#">SPORTS ADDICTS</a>
               
                <!---user dasboard--->
                
              <form action="/SportsEventOrganize/Homepage.py">
                  <button class="button" style="border-radius: 5px;background-color: #eeeeee;color:#F50057;border:none;font-size: 14px;" id="" >
                    Log Out
                  </button> 
              </form>
              <form action="" method="post" enctype="multipart/form-data">
                  <button type="submit" name="back" class="buttons" style="border-radius: 5px;background-color: #eeeeee;color:#F50057;border:none;font-size: 14px;" id="" >
                    Back
                  </button> 
              </form>
               
            
            
            </div>
            
        </nav>
    </header>
    
      <!-- dashboard section -->
 
    <section id="dashboard">
           <div class="container-fluid p-0 m-0">
            <div class="row m-0" style="height:90vh;width:100%%;border:2px solid;border-color: #f9f9f9;">
            
                <!-- user details -->
                
                <div class="col-lg-3 col-12 userdetails" style="background-color: #F50057 !important;">
                
                    <!-- profile -->
                    
                        <div class="row profile d-flex justify-content-center align-items-center text-center">
                            <span class="my-3 d-flex justify-content-center align-items-center" style="color:#f9f9f9;width:100px;height:100px;font-size: 50px;border-radius: 50%%;background-color: #FF4081;">S</span>
                            <h2 style="color:white;font-weight: 600;">Hii</h2>
                            <h3 style="color:#eeeeee">%s</h3>
                        </div>
                        
                        <!-- dashmenus -->
                        
                        <div class="row dashmenus my-4">
                            <ul class="nav navbar-nav py-4" style="padding-right: 0px;">
                                <li class="nav-item my-2">
                                    <a onclick="return editprofile()" id="ep" href="#editprofile" class="nav-link text-center" style="font-weight: 700;color:#eeeeee !important;
                                    background-color: black !important;">Edit Profile</a>
                                </li>
                                <li class="nav-item my-2">
                                    <a onclick="return upcomevents()" id="upcom" href="#upcomevents" class="nav-link text-center" style="font-weight: 700;background-color: #eeeeee;color: #F50057 ;">Your Upcoming Events</a>
                                </li>
                                <li class="nav-item my-2">
                                    <a onclick="return completedevents()" id="com" href="#completedevents" class="nav-link text-center" style="font-weight: 700;background-color: #eeeeee;color: #F50057 ;">Results of Events</a>
                                </li>
    
                            </ul>
                        </div>
                        
                </div>
                <!-- definitions of userdetails -->
                <div class="col-lg-9 col-12 definitions p-0">
                        <section class="right p-5" id="editprofile" style="display: block;">
                            <form action="" name="stuupform"  method="post" enctype="multipart/form-data">
                                <div class="mb-3">
                                  <label for="fullname" class="form-label">Full Name</label>
                                  <input type="text" class="form-control" id="fullname" name="fname" value=%s>
                                </div>
                                <div class="mb-3 uname">
                                  <label for="uname" class="form-label">User Name</label>
                                  <input type="text" class="form-control" id="uname" name="uname" value=%s>
                                </div>
                                <div class="mb-3">
                                  <label for="pass" class="form-label">Password</label>
                                  <input type="password" minlength="8" maxlength="16" class="form-control" id="pass" name="pass" value=%s>
                                </div>
                                <div class="mb-3">
                                  <label class="form-label" for="cpass">Confirm Password</label>
                                  <input type="password" minlength="8" maxlength="16" class="form-control" id="cpass" name="cpass" value=%s>
                                  
                                </div>
                                <div class="buttons mb-3 d-flex justify-content-center align-items-center">
                                  <button type="submit" class="btn btn-primary my-3" name="sub">Update</button>
                                </div>
                                
                              
                            </form>

                        </section>"""% (i[1],i[1],i[2],i[5],i[6]))
Fullname=form.getvalue("fname")
Username=form.getvalue("uname")
Password=form.getvalue("pass")
CPassword=form.getvalue("cpass")
Sub=form.getvalue("sub")
if Sub !=None:
    q="""UPDATE `sturegister` SET `fullname`='%s',`uname`='%s',`pass`='%s',`cpass`='%s' WHERE id='%s'""" %(Fullname,Username, Password, CPassword,userid)
    cur.execute(q)
    conn.commit()
    print("""
    <script>
        alert("Updated Successfully");
    </script>
    """)

pback=form.getvalue("back")
if pback!=None:
    print("""
    <script>
        location.href="Fullhomepage.py?id=%s";
    </script>
    """%userid)



print("""
                        
                        <section class="p-5" id="upcomevents" style="display:none;">
                            <div class="container my-lg-5 m-0">
                                <div class="row">""")

q=""" select id,eventname from sportsregister where id='%s' """%userid
cur.execute(q)
rec=cur.fetchall()
for i in rec:
    w="""select * from eventdetails where eventname='%s' """%(i[1])
    cur.execute(w)
    rec1=cur.fetchall()
    for i in rec1:
        print("""
                                  <!-- sports event card -->
                                  
                                  <div class="col-lg-4 col-12 d-flex justify-content-center align-items-center my-lg-4 my-5">
                                    <div class="card" style="width: 325px;height:525px;text-overflow:ellipsis;">
                                      <img src="/SportsEventOrganize/eventimages/%s" style="width: 325px;height:300px" class="card-img-top img-fluid" alt="...">
                                      <div class="card-body">
                                        <h5 class="card-title text-center" style="text-transform: capitalize;">%s</h5>
                                        <div class="dateandtiming my-3">
                                          <div class="date d-flex flex-column justify-content-center align-items-center">
                                            <h6 class="text-center" style="text-transform: capitalize;">%s</h6>
                                            <h6>%s</h6>
                                          </div>
                                          <div class="timing">
                                            <h6 style="text-transform: capitalize;">%s</h6>
                                            <h6>%s to %s</h6>
                                          </div>
                                        </div>
                                        <div class="text-center">
                                            <h6 style="text-transform:capitalize;">%s</h6>
                                        </div>
                                        
                                      </div>
                                    </div>
                                  </div>"""%(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[9]))

print("""
                                   
                                </div>
                              </div>
                        </section>
                        <section class="p-5" id="completedevents" style="display:none;">
                            <div class="container my-lg-5 m-0">
                                
                                <div class="row">""")
q="""select * from results"""
cur.execute(q)
rec=cur.fetchall()
for i in rec:
    print("""
                                  <!-- results card -->
                                  
                                  <div class="col-lg-4 col-12 d-flex justify-content-center align-items-center my-lg-4 my-5">
                                    <div class="card" style="width: 18rem;">
                                      <img src="/SportsEventOrganize/eventimagesforresults/%s" style="width:18rem;height:18rem" class="card-img-top img-fluid" alt="...">
                                      <div class="card-body">
                                        <h5 class="card-title text-center">%s</h5>
                                        <div class="d-flex justify-content-start align-items-center">
                                        <div class="firstprize d-flex justify-content-between align-items-center" style="min-width:110px;">
                                            <h6>First Prize</h6>
                                            <h6>:</h6>
                                        </div>
                                        <div>
                                            <h6 class="ps-2" style="text-transform:capitalize;">%s</h6>
                                        </div>
                                        </div>
                                        <div class="d-flex justify-content-start align-items-center">
                                        <div class="firstprize d-flex justify-content-between align-items-center" style="min-width:110px;">
                                            <h6>Second Prize</h6>
                                            <h6>:</h6>
                                        </div>
                                        <div>
                                            <h6 class="ps-2" style="text-transform:capitalize;">%s</h6>
                                        </div>
                                        </div>
                                        <div class="d-flex justify-content-start align-items-center">
                                        <div class="firstprize d-flex justify-content-between align-items-center" style="min-width:110px;">
                                            <h6>Third Prize</h6>
                                            <h6>:</h6>
                                        </div>
                                        <div>
                                            <h6 class="ps-2" style="text-transform:capitalize;">%s</h6>
                                        </div>
                                        </div>
                                      </div>
                                      </div>
                                  </div>"""%(i[2],i[1],i[3],i[4],i[5]))
print("""                                 
            </div>
           </div>   
              
    </section>


    <!-- footer -->

    <!-- <footer>
      <div class="container-fluid py-5">
        <div class="row">
          <div class="col-5">
                <h2 class="text-center text-white">SPORTS ADDICTS</h2>
          </div>
          <div class="col-4 menu">
              <b><a href="/SportsEventOrganize/Fullhomepage.py#home" class="mx-3 text-center">Home</a></b>
              <b><a href="/SportsEventOrganize/Fullhomepage.py#aboutus" class="mx-3 text-center">About</a></b>
              <b><a href="/SportsEventOrganize/Fullhomepage.py#event" class="mx-3 text-center">Events</a></b>
              
          </div>
          <div class="col-3 social">
              <img class="mx-2 text-center" src="/SportsEventOrganize/images/icon-facebook.svg" alt="">
              <img class="mx-2 text-center" src="/SportsEventOrganize/images/icon-instagram.svg" alt="">
              <img class="mx-2 text-center" src="/SportsEventOrganize/images/icon-twitter.svg" alt="">
          </div>
        </div>
      </div>
    </footer> -->
    <script >
        function editprofile(){
            document.getElementById("editprofile").style="display:block;"
            document.getElementById("upcomevents").style="display:none"
            document.getElementById("completedevents").style="display:none"
            document.getElementById("ep").style="color:#eeeeee;background-color:black;font-weight:700"
            document.getElementById("upcom").style="background-color:#eeeeee;color:#F50057;font-weight:700;"
            document.getElementById("com").style="background-color:#eeeeee;color:#F50057;font-weight:700;"
        }
        function upcomevents(){
            document.getElementById("upcomevents").style="display:block;background-color:black;color:#eeeeee;"
            document.getElementById("editprofile").style="display:none"
            document.getElementById("completedevents").style="display:none"
            document.getElementById("upcom").style="background-color:black;color:#eeeeee;font-weight:700;"
            document.getElementById("ep").style="color:#F50057;background-color:#eeeeee;font-weight:700;"
            document.getElementById("com").style="color:#F50057;background-color:#eeeeee;font-weight:700;"

        }
        function completedevents(){
            document.getElementById("completedevents").style="display:block;background-color:black;color:#eeeeee;"
            document.getElementById("upcomevents").style="display:none"
            document.getElementById("editprofile").style="display:none"
            document.getElementById("com").style="background-color:black;color:#eeeeee;font-weight:700;"
            document.getElementById("ep").style="color:#F50057;background-color:#eeeeee;font-weight:700"
            document.getElementById("upcom").style="color:#F50057;background-color:#eeeeee;font-weight:700"
        }
    </script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"></script>
</body>
</html>
    """ )
conn.close()

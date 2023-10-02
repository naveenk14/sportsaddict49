#!C:/Users/Naveenkumar/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi,cgitb

cgitb.enable()
conn=pymysql.connect(host="Localhost", user="root", password="", database="student_registration")
cur=conn.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration Form</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,900;1,400&display=swap');
        body{
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }

        /* navbar */
        
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
        
          /* log and signup  */
          
        header nav .dropdown a{
            color:#F50057 !important;
            background-color: white !important;
            border-radius: 10px;
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
                font-size: x-small;
            }
        }
        @media (min-width:300px) and (max-width:990px){
            header nav{
                padding: 0px;
            } 
        } 
        
            /* section */
        
        section{
            width:100%;
            min-height:100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        #sturegistration .container{
            margin: 10%;
            border: 2px solid #F50057 !important;
            border-radius: 10px;
        }
        #sturegistration .container .row .frmdetails .title h2{
            color: #F50057;
            text-transform: uppercase;
            font-weight: 700;
        }
        #sturegistration .container .row .frmdetails input{
            outline: none;
            border-color:#fffcfd;
            background-color: #F50057;
            color: #fcfbfb;
            border-radius: 10px;
            height: 3rem;
            font-weight: 500;
            text-transform: uppercase;
        }
        #sturegistration .container .row .frmdetails label{
            color: #F50057;
            font-weight: 500;
        }
        #sturegistration .container .row .frmdetails button{
            background-color: #f9f9f9;
            color: #F50057;
            border-color: #F50057;
            font-weight: 600;
            text-transform: uppercase;
            
        }
        #sturegistration .container .row .frmdetails .button{
            display: flex;
            justify-content: center;
            align-items: center;
        }
        #sturegistration .container .row .frmdetails .form-select{
            outline: none;
            border-color:#fffcfd;
            background-color: #F50057;
            color: #fcfbfb;
            border-radius: 10px;
            height: 3rem;
            font-weight: 500;
            text-transform: uppercase;
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
            border-radius: 45%;
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
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark">
            <div class="container-fluid">
            
              <!-- logo -->
              
              <a class="navbar-brand" href="#">SPORTS ADDICTS</a>
              
              <!-- toggler -->
              
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-expanded="false">
                <span class="navbar-toggler-icon"></span>
              </button>
              
              <!-- menus -->
              
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="nav navbar-nav mx-auto">
                  <li class="nav-item px-md-3 my-lg-0 my-2">
                    <a class="nav-link text-white fw-bold text-center" href="/SportsEventOrganize/Homepage.py#home">Home</a>
                  </li>
                  <li class="nav-item px-md-3 my-lg-0 my-2">
                    <a class="nav-link text-white fw-bold text-center" href="/SportsEventOrganize/Homepage.py#aboutus">About us</a>
                  </li>
                  <li class="nav-item px-md-3 my-lg-0 my-2">
                    <a class="nav-link text-white fw-bold text-center" href="/SportsEventOrganize/Homepage.py#event">Events</a>
                  </li>
                </ul>
                
                <!-- login and sign up -->
                
                <li class="nav nav-item dropdown d-flex justify-content-center align-items-center my-lg-0 my-4">
                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Log In
                  </a>
                  <ul class="dropdown-menu dropdown-menu-lg-end" aria-labelledby="navbarDropdown">
                    <li><a class="dropdown-item" href="/SportsEventOrganize/Sportsfaculty_login.py">Sports Faculty Login</a></li>
                    <li><a class="dropdown-item" href="/SportsEventOrganize/volunteer_login.py">Volunteer Login</a></li>
                    <li><a class="dropdown-item d-items" href="/SportsEventOrganize/StuLoginform.py">Student Login</a></li>
                  </ul>
                </li>
                <li class="nav nav-item dropdown d-flex justify-content-center align-items-center my-lg-0 my-4 ms-lg-4">
                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Sign Up
                  </a>
                  <ul class="dropdown-menu dropdown-menu-lg-end" aria-labelledby="navbarDropdown">
                    <li><a class="dropdown-item" href="/SportsEventOrganize/StuRegisterform.py">Student Registration</a></li>
                    
                  </ul>
                </li>
                
              </div>
            </div>
          </nav>
    </header>

    <!-- student regform -->

    <section id="sturegistration">
        <div class="container">
          
          <div class="row">
            <div class="col-lg-6 img d-flex justify-content-center align-items-center">
                  <img src="/SportsEventOrganize/images/n sportsday.webp" class="img-fluid" alt="">
            </div>
            <div class="col-lg-6 p-5 frmdetails">
                  <div class="title my-5">
                     <h2 class="text-center" style="letter-spacing: 2px;">Student Registration</h2>
                  </div>
                  <div class="form">
                    <form action="" name="stuform" onsubmit="return checkall()" method="post" enctype="multipart/form-data">
                          <div class="mb-3 fname">
                            <label for="fullname" class="form-label">Full Name</label>
                            <input type="text" class="form-control" id="fullname"name="fname">
                          </div>
                          <div class="mb-3 uname">
                            <label for="uname" class="form-label">User Name</label>
                            <input type="text" class="form-control" id="uname" name="uname">
                          </div>
                          <div class="mb-3">
                            <label for="dob" class="form-label">Date Of Birth</label>
                            <input type="date" class="form-control" id="dob" name="dob">
                          </div>
                          
                          <div class="mb-3 pnumber">
                                <label for="pnumber" class="form-label">Phone Number</label>
                                <input type="text" class="form-control" id="pnumber" name="pnumber">
                          </div>
                          <div class="mb-3">
                            <label for="pass" class="form-label">Password</label>
                            <input type="password" minlength="8" maxlength="16" class="form-control" id="pass" name="pass">
                          </div>
                          <div class="mb-3">
                            <label class="form-label" for="cpass">Confirm Password</label>
                            <input type="password" minlength="8" maxlength="16" class="form-control" id="cpass" name="cpass">
                            
                          </div>
                          <div class="error mb-3 text-center" style="text-transform: uppercase;color: rgb(239, 11, 144);font-weight: 500;" id="error">
                              <h5 style="letter-spacing: 2px;"></h5>
                          </div>
                          <div class="button my-5">
                            <button type="submit" class="btn btn-primary my-3" name="sub">Submit</button>
                          </div>
                    </form>
                  </div>
                  
            </div>
          </div>
        </div>
    </section>
    
    
    <!-- footer -->

    <footer>
      <div class="container-fluid py-5">
        <div class="row">
          <div class="col-5">
                <h2 class="text-center text-white">SPORTS ADDICTS</h2>
          </div>
          <div class="col-4 menu">
              <b><a href="/SportsEventOrganize/Homepage.py#home" class="mx-3 text-center">Home</a></b>
              <b><a href="/SportsEventOrganize/Homepage.py#aboutus" class="mx-3 text-center">About</a></b>
              <b><a href="/SportsEventOrganize/Homepage.py#event" class="mx-3 text-center">Events</a></b>
              
          </div>
          <div class="col-3 social">
              <img class="mx-2 text-center" src="/SportsEventOrganize/images/icon-facebook.svg" alt="">
              <img class="mx-2 text-center" src="/SportsEventOrganize/images/icon-instagram.svg" alt="">
              <img class="mx-2 text-center" src="/SportsEventOrganize/images/icon-twitter.svg" alt="">
          </div>
        </div>
      </div>
    </footer>
    <script>
        function checkall(){
    let Fname=document.forms["stuform"]["fname"].value;
    let Uname=document.forms["stuform"]["uname"].value;
    let Dob=document.forms["stuform"]["dob"].value;
    let Phnumber=document.forms["stuform"]["pnumber"].value;
    let Pass=document.forms["stuform"]["pass"].value;
    let Cpass=document.forms["stuform"]["cpass"].value;


    if(Fname==null || Fname==""){
        document.getElementById("error").innerHTML="enter a Full name !";
        return false;
    }
    else if(Uname==null || Uname==""){
        document.getElementById("error").innerHTML="enter a user name !"
        return false;
    }
    else if(Dob==null || Dob==""){
        document.getElementById("error").innerHTML="enter a dateofbirth !"
        return false;
    }
    else if(Phnumber==null || Phnumber==""){
        document.getElementById("error").innerHTML="enter a phone number !"
        return false;
    }
    else if(Pass==null || Pass==""){
        document.getElementById("error").innerHTML="enter a Password !";
        
        return false;
    }
    else if(Cpass==null || Cpass==""){
        document.getElementById("error").innerHTML="enter a confirm password !";
        return false;
    }

    if(Pass != Cpass){
        document.getElementById("error").innerHTML="Password not matched!";
        return false;
    }

    if(Fname != '' && Uname != '' && Dob != '' && Phnumber != '' && Pass != '' && Cpass != ''){
        return true;
    }
}
    </script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"></script>
</body>
</html>
""")

form=cgi.FieldStorage()
Fullname=form.getvalue("fname")
Username=form.getvalue("uname")
DOB=form.getvalue("dob")
Pnumber=form.getvalue("pnumber")
Password=form.getvalue("pass")
CPassword=form.getvalue("cpass")
Sub=form.getvalue("sub")

if Sub!=None:
    q=""" SELECT uname FROM `sturegister` WHERE uname="%s" """ % (Username)
    cur.execute(q)
    res=cur.fetchone()
    q=""" SELECT phonenumber FROM `sturegister` WHERE phonenumber="%s" """ % (Pnumber)
    cur.execute(q)
    res1=cur.fetchone()
    if res!=None:
        print("""
                    <script>
                        alert("username already exists");
                    </script>
                    """)
    elif res1!=None:
        print("""
                    <script>
                        alert("Mobilenumber already exists");
                    </script>
                    """)
    else:
        q = """insert into sturegister(fullname,uname,dob,phonenumber,pass,cpass) values('%s','%s','%s','%s','%s','%s')""" % (Fullname, Username,DOB,Pnumber, Password, CPassword)
        cur.execute(q)
        conn.commit()
        print("""
        <script>
            alert("Registered Successfully");
            location.href="StuLoginform.py"
        </script>
        """)
conn.close()

#!C:/Users/Naveenkumar/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="Localhost", user="root", password="", database="student_registration")
cur = conn.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        *{
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
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
        
            /*profile dashboard*/
        
        header nav .container-fluid #bs{
            background-color: #FF4081;
            color:#fbfbfb;
            border-radius: 50%;
            width:40px;height:40px;
            border:none;
            font-weight: 600;
        }
        @media  screen and (min-width:992px) {
            .button{
              position: absolute;
              right:10%;
              top:20%;
            }
        }
        @media  screen and (max-width:380px){
            header nav .navbar-brand{
                font-size: 18px;
                font-weight: 800;
        
            }
            header nav .container-fluid form #bs{
                width:30px;
                height:30px;
                font-weight: 600;
            }
            header nav .container-fluid .navbar-toggler *{
                width: 30px;
                height:30px;
            }
        }
        
                /* confirmticket*/
        
        section{
            width:100%;
            min-height:100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
         @media screen and (max-width:401px) {
                  #confirmation .container h6{
                      font-size: smaller;
                  }
                }
                
         #confirmation .container .buttons{
            display: flex;
            justify-content: center;
            align-items: center;
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
              
              <!---user dasboard--->
              
              <form action="" method="post" enctype="multipart/form-data">
                 <button type="submit" name="sub" class="button" id="bs">S</button>
              </form>
              
              <!-- menus -->
              
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
              
                <ul class="nav navbar-nav mx-auto">
                  <li class="nav-item px-md-3 my-lg-0 my-2">
                    <a class="nav-link text-white fw-bold text-center" href="/home.html#home">Home</a>
                  </li>
                  <li class="nav-item px-md-3 my-lg-0 my-2">
                    <a class="nav-link text-white fw-bold text-center" href="/home.html#aboutus">About us</a>
                  </li>
                  <li class="nav-item px-md-3 my-lg-0 my-2">
                    <a class="nav-link text-white fw-bold text-center" href="/home.html#event">Events</a>
                  </li>
                </ul>

              </div>
            </div>
        </nav>
    </header>
    
   <!-- confirmation -->
   
    <section id="confirmation">
      <div class="container">
        <div class="row p-lg-5 p-md-5 p-3">
          <div class="col-12 text-center">
                <h1 style="font-weight: 800;color:#F50057;">Congrats!</h1>
                <h1 style="font-weight: 700;">Your ticket is booked</h1>
                <h6 style="font-weight: 300;" >We hope you will enjoy participating :)</h6>
                <div class="img">
                  <img src="/SportsEventOrganize/images/ticket booked.webp" class="img-fluid" alt="">
                </div>
                <div class="buttons">
                  <form action="" method="post" enctype="multipart/form-data">
                    <button class="btn btn-primary" style="background-color: aliceblue;color:#F50057;border-color: #F50057;border-radius: 10px;font-weight: 500;" name="Rhomepage" >Back to Homepage</button>
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
              <b><a href="/home.html#home" class="mx-3 text-center">Home</a></b>
              <b><a href="/home.html#aboutus" class="mx-3 text-center">About</a></b>
              <b><a href="/home.html#event" class="mx-3 text-center">Events</a></b>
              <b><a href="/home.html#news" class="mx-3 text-center">News</a></b>
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
        function homepage(){
          location.href="Fullhomepage.py";
        }
    </script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"></script>
</body>
</html>
""")
form=cgi.FieldStorage()
Rtrn=form.getvalue("Rhomepage")
userid=form.getvalue("id")
Sub=form.getvalue("sub")
if Sub!=None:
    print("""
        <script>
                location.href = "StuDashboard.py?id=%s";
        </script>
    """%userid)
if Rtrn!=None:
    print("""
        <script>
            location.href="Fullhomepage.py?id=%s"
        </script>
    """%userid)

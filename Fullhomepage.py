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
    <title>Sports addicts</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body{
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
        header nav .container-fluid #bs{
            background-color: #FF4081;
            color:#fbfbfb;
            border-radius: 50%;
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
        
        section{
            width:100%;
            min-height:100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
                /* home   */
        
        #home{
            background: linear-gradient(75deg,rgba(0,0,0,.3),rgba(0,0,0,.4)),url(./images/93715.jpg);
            background-size: cover;
            background-position: center;
            height:90vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: end;
        }
        #home h1{
            letter-spacing: 4px;
            line-height: 50px;
            color: white !important;
            font-family: Verdana, Geneva, Tahoma, sans-serif;
            max-width:30vw;
            text-align: center;
        }
        #home p{
            letter-spacing: 3px;
            line-height: 25px;
            max-width:300px;
            text-align: center;
            height:100px;
            font-weight: 600;
            color:#f5f3f49b !important;
            font-family: 'Times New Roman', Times, serif;
        }
        #home button{
            background-color: #F50057;
            color:white !important;
            border-radius: 10px;
            border: none;
            outline: none;
            padding: .5rem 1rem;
            font-weight: 500;
        }
        .quotes{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
          
            /* upcoming events */
        
        #event{
            background-color: black !important;
        }
        #event h1{
            color:white !important;
            font-weight: 600;
            letter-spacing: 3px;
            text-transform: uppercase;
        }
        #event .card img{
            border-top-left-radius: 20px;
            border-top-right-radius: 20px;
        }
        #event .card{
            background-color: black !important;
            color: white !important;
            border-radius: 20px !important;
            border-color: #F50057;
        }
        #event .card .card-body h5{
            letter-spacing: 3px;
        }
        #event .card .card-body .dateandtiming{
            display: flex;
            justify-content: space-evenly;
            background-color: #F50057;
            border-radius: 10px;
            padding: 1rem;
        }
        #event .card .card-body .dateandtiming .date{
            border-right: 2px solid white;
            padding-right: 1rem;
            margin-right: .5rem;
        }
        
                /* finishevents */
        
        #finishevent{
            background-color: black !important;
        }
        #finishevent h1{
            color:white !important;
            font-weight: 600;
            letter-spacing: 3px;
            text-transform: uppercase;
        }
        #finishevent .card img{
            border-top-left-radius: 20px;
            border-top-right-radius: 20px;
        }
        #finishevent .card{
            background-color: black !important;
            color: white !important;
            border-radius: 20px !important;
            border-color: #F50057;
        }
        #finishevent .card .card-body h5{
            letter-spacing: 3px;
        }
        #finishevent .card .card-body .dateandtiming{
            display: flex;
            justify-content: space-evenly;
            background-color: #F50057;
            border-radius: 10px;
            padding: 1rem;
        }
        #finishevent .card .card-body .dateandtiming .date{
            border-right: 2px solid white;
            padding-right: 1rem;
            margin-right: .5rem;
        }
        
                /* about us */
        
        #aboutus{
            background-color: black !important;
        }
        #aboutus .container .row .title h2{
            color: #F50057 !important;
        }
        #aboutus .container .row .description p{
            line-height: 30px;
            font-size: 14px;
            font-weight: 500;
            padding: 1.5rem;
            letter-spacing: 2px;
            text-align: justify;
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
    <!--header -->
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark">
            <div class="container-fluid">
            
              <!-- logo -->
              
              <a class="navbar-brand" href="#">SPORTS ADDICTS</a>
 
                <!-- toggler -->
                
              <button class="navbar-toggler ms-auto me-2" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-expanded="false">
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
                    <a class="nav-link text-white fw-bold text-center" href="#home" >Home</a>
                  </li>
                  <li class="nav-item px-md-3 my-lg-0 my-2">
                    <a class="nav-link text-white fw-bold text-center" href="#aboutus">About us</a>
                  </li>
                  <li class="nav-item px-md-3 my-lg-0 my-2">
                    <a class="nav-link text-white fw-bold text-center" href="#event">Events</a>
                  </li>
                </ul>
                </div>
            
            </div>
        </nav>
    </header>

      <!-- homes section -->

    <section id="home">
              <div class="container-fluid">
                <div class="row">
                  <div class="col-lg-6 col-md-12 col-12 p-0">
                          
                  </div>
                  <div class="col-lg-6 col-md-12 col-12 p-0 quotes">
                    <h1 class="my-3">SHOW YOUR SKILLS !</h1>
                    <p class="my-3">
                      Somebody gives you an opportunity,say yes to it.So what if you fail? You won't know if you fail or succeed unless you try.
                    </p>
                    <form action="" method="post" enctype="multipart/form-data">
                      <button type="submit" name="rsubmit" class="my-5">
                        Register Now
                      </button>
                    </form>
                  </div>
                </div>
              </div>
    </section>

    <!-- Events section -->

    <section id="event">
        <div class="container m-5">
          <h1 class="text-center my-5">Upcoming Events</h1>
          <div class="row">""")

q="""select * from eventdetails where status='Approved' """
cur.execute(q)
rec1=cur.fetchall()

for i in rec1:
    print("""
            <!-- marathon card -->
            <div class="col-lg-4 col-12 d-flex justify-content-center align-items-center my-lg-4 my-5">
              <div class="card" style="width:325px;height:525px;">
                <img src="/SportsEventOrganize/eventimages/%s" style="width: 325px;height:350px;" class="card-img-top img-fluid" alt="...">
                <div class="card-body">
                  <h5 class="card-title text-center" style="text-transform:capitalize;">%s</h5>
                  <div class="dateandtiming my-3">
                    <div class="date d-flex flex-column justify-content-center align-items-center">
                      <h6 class="text-center" style="text-transform:capitalize;">%s</h6>
                      <h6 style="text-transform:capitalize;">%s</h6>
                    </div>
                    <div class="timing">
                      <h6 style="text-transform:capitalize;">%s</h6>
                      <h6 style="text-transform:capitalize;">%s to %s</h6>
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

<!-- finished events -->

<section id="finishevent">
  <div class="container m-5">
    <h1 class="text-center my-5">Results of Events</h1>
    <div class="row">""")
q="""select * from results"""
cur.execute(q)
rec=cur.fetchall()
for i in rec:
    print("""
    
      <!-- marathon card -->
                                  <div class="col-lg-4 col-12 d-flex justify-content-center align-items-center my-lg-4 my-5">
                                    <div class="card" style="width: 325px;height:525px;">
                                      <img src="/SportsEventOrganize/eventimagesforresults/%s" style="width:325px;height:350px" class="card-img-top img-fluid" alt="...">
                                      <div class="card-body">
                                        <h5 class="card-title text-center" style="text-transform:capitalize;">%s</h5>
                                        <div class="p-2" style="background-color:#F50057 !important;border-radius:10px;" >
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
                                      </div>
                                  </div>
      """%(i[2],i[1],i[3],i[4],i[5]))

print("""   </div>
  </div>
</section>

    <!-- about section -->
    
    <section id="aboutus">
        <div class="container">
          <div class="row my-lg-5 my-5">
            <div class="col-lg-6">
                <div class="title text-white text-center">
                      <h2>ABOUT US</h2>
                </div>
                <div class="description text-white">
                  <p>Sport events bring the community together also are a positive way to generate some local business. Hosting a sport event can help boost the local economy and morale. Depending on the size of the event it could even bring business to local hotels, restaurants, and free publicity to the town. There are many sport events that even contribute to a specific local charity, not only helping the sports talent but the locals as well. Sport events encourage community unification and joy for everyone of all ages.

                  Are you looking for sports talent for an event? Or need help planning an event? Look no further than Sports and Motion, we have a highly experienced team that can provide you the help you need as a sports consultancy company.</p>
                </div>
            </div>
            <div class="col-lg-6">
                <img src="./images/sports-event-concept-with-silhouette-athletics-running-cross-ribbon-white-background_1302-27609.webp" style="width:100%;height:100%;border-radius: 10px;" alt="">
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
              <b><a href="#home" class="mx-3 text-center">Home</a></b>
              <b><a href="#aboutus" class="mx-3 text-center">About</a></b>
              <b><a href="#event" class="mx-3 text-center">Events</a></b>
          </div>
          <div class="col-3 social">
              <img class="mx-2 text-center" src="./images/icon-facebook.svg" alt="">
              <img class="mx-2 text-center" src="./images/icon-instagram.svg" alt="">
              <img class="mx-2 text-center" src="./images/icon-twitter.svg" alt="">
          </div>
        </div>
      </div>
    </footer>
    <script>
    </script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"></script>
</body>
</html>
""")


form=cgi.FieldStorage()
userid=form.getvalue("id")
Sub=form.getvalue("sub")
Rsubmit=form.getvalue("rsubmit")
if Sub!=None:
    print("""
    <script>
            location.href = "StuDashboard.py?id=%s";
    </script>
    """%userid)

if Rsubmit!=None:
    print("""
        <script>
                location.href = "sportsreg.py?id=%s";
        </script>
        """ % userid)




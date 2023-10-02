#!C:/Users/Naveenkumar/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi,cgitb

cgitb.enable()
conn=pymysql.connect(host="Localhost", user="root", password="", database="student_registration")
cur=conn.cursor()

form=cgi.FieldStorage()
userid=form.getvalue("id")
q=""" select uname,fullname,dob,phonenumber from sturegister where id='%s' """ %(userid)
cur.execute(q)
details=cur.fetchone()

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
            border-radius: 50%%;
            width:40px;height:40px;
            border:none;
            font-weight: 600;
        }
        @media  screen and (min-width:992px) {
            .button{
              position: absolute;
              right:10%%;
              top:20%%;
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
        
                /* application */
        
        section{
            width:100%%;
            min-height:100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        #application .container{
            margin: 10%%;
            border: 2px solid #F50057 !important;
            border-radius: 10px;
        }
        #application .container .row .frmdetails .title h2{
            color: #F50057;
            text-transform: uppercase;
            font-weight: 700;
        }
         #application .container .row .frmdetails input{
             outline: none;
             border-color:#fffcfd;
             background-color: #F50057;
             color: #fcfbfb;
             border-radius: 10px;
             height: 3rem;
             font-weight: 500;
             text-transform: uppercase;
         }
        #application .container .row .frmdetails label{
            color: #F50057;
            font-weight: 500;
        }
        #application .container .row .frmdetails button{
            background-color: #f9f9f9;
            color: #F50057;
            border-color: #F50057;
            font-weight: 600;
            text-transform: uppercase;
        
        }
        #application .container .row .frmdetails .buttons{
            display: flex;
            justify-content: center;
            align-items: center;
        }
        #application .container .row .frmdetails .form-select{
            outline: none;
            border-color:#fffcfd;
            background-color: #F50057;
            color: #fcfbfb;
            border-radius: 10px;
            height: 3rem;
            font-weight: 500;
            text-transform: uppercase;
        }
        
        @media screen and (max-width:606px){
            #application .container .row .process h6{
                font-size: xx-small;
            }
            #application .container .row .process .bar hr{
                width:40px !important;
            }
            #application .container .row .process .payform{
                padding-left: 5px;
                padding-right: 5px;
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
                    <a class="nav-link text-white fw-bold text-center" href="/SportsEventOrganize/Fullhomepage.py?id=%s#home">Home</a>
                  </li>
                  <li class="nav-item px-md-3 my-lg-0 my-2">
                    <a class="nav-link text-white fw-bold text-center" href="/SportsEventOrganize/Fullhomepage.py?id=%s#aboutus">About us</a>
                  </li>
                  <li class="nav-item px-md-3 my-lg-0 my-2">
                    <a class="nav-link text-white fw-bold text-center" href="/SportsEventOrganize/Fullhomepage.py?id=%s#event">Events</a>
                  </li>
                </ul>
                
              </div>
            </div>
        </nav>
    </header>

    <!-- application -->

    <section id="application">
        <div class="container"> 
          <div class="row">
            <div class="col-lg-6 img d-flex justify-content-center align-items-center">
                  <img src="/SportsEventOrganize/images/sport-equipment-concept_1284-13034.webp" class="img-fluid" alt="">
            </div>
            <div class="col-lg-6 p-5 frmdetails">
                  <div class="title">
                     <h2 class="">Register</h2>
                  </div>
                  <div class="form">
                    <form action="" onsubmit="return checkall()" name="sportsform" method="post" enctype="multipart/form-data">
                      <div class="my-4">
                        <select id="eventname" class="form-select" aria-label="Default select example" name="eventname">
                          <option value='' disable selected hidden>Choose an event</option>"""%(userid,userid,userid))
q="""select eventname from eventdetails where status='Approved' """
cur.execute(q)
recu=cur.fetchall()

for i in recu:
    c=i[0]
    print("""
                          <option style="text-transform:uppercase;" value="%s" >%s</option>
                          """%(i[0],i[0]))

print("""
                        </select>
                      </div> 
                      <div class="mb-3 uname">
                        <label for="uname" class="form-label">User Name</label>
                        <input type="text" class="form-control" id="uname" name="uname" value=%s readonly>
                      </div>
                      <div class="mb-3 fname">
                        <label for="fullname" class="form-label">Full Name</label>
                        <input type="text" class="form-control" id="fullname" name="fname" value=%s readonly>
                      </div>
                      <div class="mb-3">
                        <label for="dob" class="form-label">Date Of Birth</label>
                        <input type="date" class="form-control" id="dob" name="dob" value=%s readonly>
                      </div>
                      <div class="mb-3">
                        <label class="form-label" for="pnumber">Mobile Number</label>
                        <input type="text" class="form-control" id="pnumber" name="mnumber" value=%s readonly>
                        
                      </div>
                      <div class="error mb-3 text-center" style="text-transform: uppercase;color: rgb(239, 11, 144);font-weight: 500;" id="error">
                          <h5 style="letter-spacing: 2px;"></h5>
                      </div>
                      <div class="buttons">
                        <button name="adddetails" type="submit" class="btn btn-primary my-3">Continue</button>
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
              <b><a href="/SportsEventOrganize/Fullhomepage.py?id=%s#home" class="mx-3 text-center">Home</a></b>
              <b><a href="/SportsEventOrganize/Fullhomepage.py?id=%s#aboutus" class="mx-3 text-center">About</a></b>
              <b><a href="/SportsEventOrganize/Fullhomepage.py?id=%s#event" class="mx-3 text-center">Events</a></b>
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
    let Evname=document.forms["sportsform"]["eventname"].value;
    let Fname=document.forms["sportsform"]["fname"].value;
    let Dob=document.forms["sportsform"]["dob"].value;
    let Mnumber=document.forms["sportsform"]["mnumber"].value;


    if(Evname==null || Evname==""){
        document.getElementById("error").innerHTML="enter a event name !";
        return false;
    }
    else if(Fname==null || Fname==""){
        document.getElementById("error").innerHTML="enter a fullname name !"
        return false;
    }
    else if(Dob==null || Dob==""){
        document.getElementById("error").innerHTML="enter a dateofbirth !";
        
        return false;
    }
    
    if(Evname != '' && Fname != '' && Dob != '' && Mnumber != '' ){
        return true;
    }
}
    </script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"></script>
</body>
</html>
"""%(details[0],details[1],details[2],details[3],userid,userid,userid))

Sub=form.getvalue("sub")
Ename=form.getvalue("eventname")
Adetails=form.getvalue("adddetails")
q="""select uname from sturegister where id='%s'""" %userid
cur.execute(q)
res=cur.fetchone()

if Sub!=None:
    print("""
    <script>
            location.href = "StuDashboard.py?id=%s";
    </script>
    """%userid)
if Adetails!=None:
    q = """select id from sportsregister where id='%s' and eventname='%s'""" % (userid, Ename)
    cur.execute(q)
    res1 = cur.fetchone()
    if res1!=None:
        print("""
                      <script>
                            alert("You already Registered!");
                      </script>
                      """)
    else:
        q = """insert into sportsregister(id,eventname,uname,fullname,dob,phonenumber) values ("%s","%s","%s","%s","%s","%s")""" % (
        userid ,Ename, details[0],details[1],details[2],details[3])
        cur.execute(q)
        conn.commit()
        print("""
                <script>
                    alert("Registered Successfully");
                    location.href="confirmticket.py?id=%s"
                </script>
                """%userid)

conn.close()


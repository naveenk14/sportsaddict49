#!C:/Users/Naveenkumar/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi,cgitb
import os

cgitb.enable()
conn = pymysql.connect(host="Localhost", user="root", password="", database="student_registration")
cur = conn.cursor()

form=cgi.FieldStorage(keep_blank_values=True)
pid=form.getvalue("id")

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
                
                        /* dashicon */
                        
                @media  screen and (min-width:992px) {
                    .button{
                        position: absolute;
                        right:10%;
                        top:32%;
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


                .definitions #addevents input{
                    outline: none;
                    border-color:#fffcfd;
                    background-color: #F50057;
                    color: #fcfbfb;
                    border-radius: 10px;
                    font-weight: 500;
                    letter-spacing: 2px;
                }
                .definitions #addevents label{
                    color: #F50057;
                    font-weight: 500;
                }
                .definitions #addvolunteers input{
                    outline: none;
                    border-color:#fffcfd;
                    background-color: #F50057;
                    color: #fcfbfb;
                    border-radius: 10px;
                    font-weight: 500;
                    letter-spacing: 2px;
                }
                .definitions #addvolunteers label{
                    color: #F50057;
                    font-weight: 500;
                }
                .definitions #editprofile input{
                    outline: none;
                    border-color:#fffcfd;
                    background-color: #F50057;
                    color: #fcfbfb;
                    border-radius: 10px;
                    font-weight: 500;
                    letter-spacing: 2px;
                }
                .definitions #editprofile label{
                    color: #F50057;
                    font-weight: 500;
                }
                    .definitions #addresults input{
                    outline: none;
                    border-color:#fffcfd;
                    background-color: #F50057;
                    color: #fcfbfb;
                    border-radius: 10px;
                    font-weight: 500;
                    height: 3rem;
                    letter-spacing: 2px;
                }
                .definitions #addresults label{
                    color: #F50057;
                    font-weight: 500;
                }
                .definitions #addresults .rowprize form .form-select{
                    outline: none;
                    border-color:#fffcfd;
                    background-color: #F50057;
                    color: #fcfbfb;
                    border-radius: 10px;
                    height: 3rem;
                    font-weight: 500;
                    text-transform: uppercase;
                }
                
                        /* definitions */
                    
                @media screen and (min-width:992px) {
                    #dashboard .container-fluid .row .definitions{
                    height:90vh;
                    overflow: auto;
                }
                }
                
                        /*for table responsive*/
                
                @media screen and (min-width:508px) and (max-width:713px){
                    #deltab *{
                        font-size:10px;
                    }
                }
                @media screen and (min-width:410px) and (max-width:508px){
                    #deltab *{
                        font-size:10px;
                        padding:4px !important;
                    }
                }
                @media screen and (min-width:320px) and (max-width:410px){
                    #deltab *{
                        font-size:7px;
                        padding:3px !important;
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
    <!--header-->
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

            </div>
        </nav>
    </header>

      <!-- dashboard section -->

    <section id="dashboard">
           <div class="container-fluid p-0 m-0">
            <div class="row m-0" style="height:90vh;width:100%;border:2px solid;border-color: #f9f9f9;">
            
                                    <!-- user details -->
                
                <div class="col-lg-3 col-12 userdetails" style="background-color: #F50057 !important;">
                
                                    <!-- profile -->
                                    
                        <div class="row profile d-flex justify-content-center align-items-center text-center">
                            <span class="my-3 d-flex justify-content-center align-items-center" style="color:#f9f9f9;width:100px;height:100px;font-size: 50px;border-radius: 50%;background-color: #FF4081;">S</span>
                            <h2 style="color:white;font-weight: 600;">Hii</h2>
                            <h3 style="color:#eeeeee">Sports Faculty</h3>
                        </div>
                                    <!-- dashmenus -->
                                        
                        <div class="row dashmenus my-4">
                            <ul class="nav navbar-nav py-4" style="padding-right: 0px;">    
                                <li class="nav-item my-2">
                                    <a id="aevents" href="#" class="nav-link text-center" style="font-weight: 700;background-color: black;color: #eeeeee ;">Add Events</a>
                                </li>
                                <li class="nav-item my-2">
                                    <a id="avolunteers" href="/SportsEventOrganize/spfm_addvolunteers.py" class="nav-link text-center" style="font-weight: 700;background-color: #eeeeee;color: #F50057 ;">Add Volunteers</a>
                                </li>
                                <li class="nav-item my-2">
                                    <a id="aresults" href="/SportsEventOrganize/spfm_addresults.py" class="nav-link text-center" style="font-weight: 700;background-color: #eeeeee;color: #F50057 ;">Add Results</a>
                                </li>
                                <li class="nav-item my-2">
                                    <a id="rstudents" href="/SportsEventOrganize/spfm_regstudents.py" class="nav-link text-center" style="font-weight: 700;background-color: #eeeeee;color: #F50057 ;">Registered Students</a>
                                </li>
                            </ul>
                        </div>

                </div>
                
                <div class="col-lg-9 col-12 definitions p-0">
                <section id="addevents">
                            <div class="container-fluid p-0">
                                <div class="row-12">
                                    <h2  style="background-color:#F50057;color:white;text-transform:uppercase;font-weight:700;font-size:25px;" class="text-center">Add New events</h2>
                                    <div class="addform p-5">
                                    <form  onsubmit="return checkall()" name="eventaddform" method="post" enctype="multipart/form-data">
                                        <div class="mb-3">
                                          <label for="eventprofileimg" class="form-label" style="font-weight:600;">Event Profile Pic</label>
                                          <input type="file" class="form-control" style="text-transform:capitalize;"  id="eventprofileimg" name="img" value="">
                                        </div>
                                        <div class="mb-3">
                                          <label for="eventname" class="form-label" style="font-weight:600;">Event Name</label>
                                          <input type="text" class="form-control"  id="eventname" name="eventname" value="" style="text-transform:capitalize;">
                                        </div>
                                        <div class="mb-3">
                                          <label for="month" class="form-label" style="font-weight:600;">Month</label>
                                          <input type="text" class="form-control" style="text-transform:capitalize;"  id="month" name="month" value="">
                                        </div>
                                         <div class="mb-3">
                                          <label for="date" class="form-label" style="font-weight:600;">Date</label>
                                          <input type="text" class="form-control" style="text-transform:capitalize;"  id="date" name="date" value="">
                                        </div>
                                        <div class="mb-3">
                                          <label for="day" class="form-label" style="font-weight:600;">Day</label>
                                          <input type="text" class="form-control" style="text-transform:capitalize;"  id="day" name="day" value="">
                                        </div>
                                        <div class="mb-3">
                                          <label for="stiming" class="form-label" style="font-weight:600;">Starting Time</label>
                                          <input type="text" class="form-control" style="text-transform:capitalize;" id="stiming" name="stiming" value="">
                                        </div>     
                                        <div class="mb-3">
                                          <label for="etiming" class="form-label" style="font-weight:600;">Ending Time</label>
                                          <input type="text" class="form-control" style="text-transform:capitalize;" id="etiming" name="etiming" value="">
                                        </div>
                                        <div class="mb-3">
                                          <label for="location" class="form-label" style="font-weight:600;">Location</label>
                                          <input type="text" class="form-control" style="text-transform:capitalize;" id="location" name="location" value="">
                                        </div>                  
                                        <div class="buttons mb-3 d-flex justify-content-center align-items-center">
                                          <button type="submit" class="btn btn-primary my-3" name="sub" style="text-transform:uppercase;font-weight:400;">Submit</button>
                                        </div>
                                        <div class="errors mb-3 text-center" style="text-transform: uppercase;color: rgb(239, 11, 144);font-weight: 500;" id="errors">
                                            <h5 style="letter-spacing: 2px;"></h5>
                                        </div>
                                    </form>
                                    </div>
                                </div>""")





print("""
                                
                                <div class="row-12">
                                    <h2 style="background-color:#F50057;color:white;text-transform:uppercase;font-weight:700;font-size:25px;border-left:2px solid white;" class="text-center m-0">View approved events</h2>
                                    <div class="viewdetails">
                                        <table class="table table-bordered" id="deltab">
                                        <thead>
                                          <tr>
                                              <th scope="col" style="color:#F50057 !important">Id</th>
                                              <th scope="col" style="color:#F50057 !important">Event Name</th>
                                              <th scope="col" style="color:#F50057 !important">Month</th>
                                              <th scope="col" style="color:#F50057 !important">Date</th>
                                              <th scope="col" style="color:#F50057 !important">Day</th>
                                              <th scope="col" style="color:#F50057 !important">Start Timing</th>
                                              <th scope="col" style="color:#F50057 !important">End Timing</th>
                                              <th scope="col" style="color:#F50057 !important">Location</th>
                                          </tr>
                                        </thead>
                                        <tbody style="border-color:white !important;background-color:#F50057 !important;color:white !important">""")

q="""select * from eventdetails where status='Approved' """
cur.execute(q)
conn.commit()
rec1=cur.fetchall()
for i in rec1:
    print("""
                                          
                                          <tr>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                          </tr>"""%(i[0],i[2],i[3],i[4],i[5],i[6],i[7],i[9]))

print("""
                                          </tbody>
                                          </table>
                                    </div>
                                </div>
                            </div>    
                        </section>
                </div>
      </div>
      </div>
    </section>  
     <script>
        function checkall(){
             
             let Seventimage=document.forms["eventaddform"]["img"].value;
             let Seventname=document.forms["eventaddform"]["eventname"].value;
             let Smonth=document.forms["eventaddform"]["month"].value;
             let Sdate=document.forms["eventaddform"]["date"].value;
             let Sday=document.forms["eventaddform"]["day"].value;
             let Stiming=document.forms["eventaddform"]["stiming"].value;
             let Etiming=document.forms["eventaddform"]["etiming"].value;
             let Location=document.forms["eventaddform"]["location"].value;

            if(Seventimage==null || Seventimage==""){
                document.getElementById("errors").innerHTML="enter a Event image !";
                return false;
            }
            if(Seventname==null || Seventname==""){
                document.getElementById("errors").innerHTML="enter a event name !";
                return false;
            }
            if(Smonth==null || Smonth==""){
                document.getElementById("errors").innerHTML="enter a month !";
                return false;
            }
            if(Sdate==null || Sdate==""){
                document.getElementById("errors").innerHTML="enter a date !";
                return false;
            }
            if(Sday==null || Sday==""){
                document.getElementById("errors").innerHTML="enter a day !";
                return false;
            }if(Stiming==null || Stiming==""){
                document.getElementById("errors").innerHTML="enter a Start timing !";
                return false;
            }if(Etiming==null || Etiming==""){
                document.getElementById("errors").innerHTML="enter a End timing !";
                return false;
            }
            if(Location==null || Location==""){
                document.getElementById("errors").innerHTML="enter a Location !";
                return false;
            }
            if(Seventimage != "" && Seventname != "" && Smonth != "" && Sdate != "" && Sday != "" && Stiming != "" && Etiming != "" && Location != ""){
                return true;
            }
        }
     </script> 
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"></script>
</body>
</html>""")



if len(form)!=0:
    peventimage=form['img']
    peventname=form.getvalue("eventname")
    pmonth=form.getvalue("month")
    pdate=form.getvalue("date")
    pday=form.getvalue("day")
    plocation=form.getvalue("location")
    pstiming=form.getvalue("stiming")
    petiming =form.getvalue("etiming")
    psub=form.getvalue("sub")
    q="""select id from eventdetails where eventname='%s' """%peventname
    cur.execute(q)
    conn.commit()
    rec=cur.fetchone()
    if rec==None:
        if peventimage.filename:
            fn=os.path.basename(peventimage.filename)
            open("eventimages/" +fn,"wb").write(peventimage.file.read())
            q=""" insert into eventdetails(eventimage,eventname,month,date,day,stiming,etiming,location) values('%s','%s','%s','%s','%s','%s','%s','%s')"""%(fn,peventname,pmonth,pdate,pday,pstiming,petiming,plocation)
            cur.execute(q)
            conn.commit()
            print("""
                <script>
                alert("Event Added Succesfully")
                </script>
                """)
        else:
            print("""
                <script>
                alert("Event Adding Failed")
                </script>
                """)

    else:
        print("""
            <script>
                alert("Event Name Already Exists ! ")
            </script>
            """)

conn.close()

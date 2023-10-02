#!C:/Users/Naveenkumar/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi,cgitb

cgitb.enable()
conn = pymysql.connect(host="Localhost", user="root", password="", database="student_registration")
cur = conn.cursor()



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
            
                    /* dashboard */
            
                    /* definitions */
            
            @media screen and (min-width:992px) {
                #dashboard .container-fluid .row .definitions{
                height:90vh;
                overflow: auto;
            }
            }
            
                    /*for table responsive*/
            
            @media screen and (min-width:320px) and (max-width:713px){
                #deltab *{
                    font-size:10px;
                }
            }
            @media screen and (min-width:320px) and (max-width:428px){
                #deltab *{
                    font-size:8px;
                    padding:4px !important;
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
                            <ul class="nav navbar-nav py-4" style="padding-right: 0px;">""")
print("""
                                
                                <li class="nav-item my-2">
                                    <a id="aevents" href="/SportsEventOrganize/spfm_addevent.py" class="nav-link text-center" style="font-weight: 700;background-color:#eeeeee ;color: #F50057 ;">Add Events</a>
                                </li>
                                <li class="nav-item my-2">
                                    <a id="avolunteers" href="#" class="nav-link text-center" style="font-weight: 700;background-color: black;color: #eeeeee ;">Add Volunteers</a>
                                </li>
                                <li class="nav-item my-2">
                                    <a id="aresults" href="/SportsEventOrganize/spfm_addresults.py" class="nav-link text-center" style="font-weight: 700;background-color: #eeeeee;color: #F50057 ;">Add Results</a>
                                </li>
                                <li class="nav-item my-2">
                                    <a id="rstudents" href="/SportsEventOrganize/spfm_regstudents.py" class="nav-link text-center" style="font-weight: 700;background-color: #eeeeee;color: #F50057 ;">Registered Students</a>
                                </li>""")
print("""
                              </ul>
                         </div>

                </div>
                <div class="col-lg-9 col-12 definitions p-0">
                <section id="addvolunteers">
                            <div class="container-fluid p-0">
                                    <div class="row-12">
                                    <h2  style="background-color:#F50057;color:white;text-transform:uppercase;font-weight:700;font-size:25px;" class="text-center">Add Volunteers</h2>
                                    <div class="addform p-5">
                                        <form action="" onsubmit="return checkall()" name="volunteeraddform"  method="post" enctype="multipart/form-data" class="d-flex flex-column justify-content-center align-items-center">
                                            <div class="mb-3">
                                              <label for="fullname" class="form-label" style="font-weight:600;">Full Name</label>
                                              <input type="text" style="text-transform:capitalize;" class="form-control" id="fullname" name="fname" value="">
                                            </div>
                                            <div class="mb-3">
                                              <label for="email" class="form-label" style="font-weight:600;">Email</label>
                                              <input type="email" style="text-transform:lowercase;" class="form-control" id="email" name="email" value="">
                                            </div>  
                                            <div class="mb-3">
                                              <label for="pnumbar" class="form-label" style="font-weight:600;">Phone Number</label>
                                              <input type="text" style="text-transform:capitalize;" class="form-control" id="pnumber" name="pnumber" value="" maxlength="10" minlength="10">
                                            </div>                    
                                            <div class="buttons mb-3 d-flex justify-content-center align-items-center">
                                              <button type="submit" class="btn btn-primary my-3" style="text-transform:uppercase;font-weight:400;" name="sub">Submit</button>
                                            </div>
                                            <div class="errors mb-3 text-center" style="text-transform: uppercase;color: rgb(239, 11, 144);font-weight: 500;" id="errors">
                                                <h5 style="letter-spacing: 2px;"></h5>
                                            </div>
                                
                                        </form>
                                    </div>""")

form=cgi.FieldStorage()
Fname=form.getvalue("fname")
Email=form.getvalue("email")
Pnumber=form.getvalue("pnumber")
Sub=form.getvalue("sub")

if Sub!=None:
    q=""" SELECT email FROM `volunteers` WHERE email='%s' or phonenumber='%s' """%(Email,Pnumber)
    cur.execute(q)
    res1=cur.fetchone()
    if res1!=None:
        print("""
         <script>
            alert("You requested already ");
         </script>
        """)
    elif res1==None:
        q=""" INSERT INTO `volunteers`(`fullname`, `email`, `phonenumber`) VALUES ('%s','%s','%s') """%(Fname,Email,Pnumber)
        cur.execute(q)
        conn.commit()
        print("""
        <script>
            alert("Request Sent");
        </script>
        """)

print("""
                                
                                <div class="row-12">
                                    <h2 style="background-color:#F50057;color:white;text-transform:uppercase;font-weight:700;font-size:25px;" class="text-center m-0">Existing Volunteers</h2>
                                    <div class="existvolundetails">
                                        <table class="table table-bordered" id="deltab">
                                        <thead>
                                          <tr>
                                              <th scope="col" style="color:#F50057 !important">Id</th>
                                              <th scope="col" style="color:#F50057 !important">Fullname</th>
                                              <th scope="col" style="color:#F50057 !important">Email</th>
                                              <th scope="col" style="color:#F50057 !important">Phonenumber</th>
                                              <th scope="col" style="color:#F50057 !important">Status</th>
                                          </tr>
                                        </thead>
                                        <tbody style="border-color:white !important;background-color:#F50057 !important;color:white !important;">""")
q="""select * from volunteers where status='Approved' """
cur.execute(q)
res=cur.fetchall()
for i in res:

    print("""
                                          <tr>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:lowercase;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                          </tr>
                                          """%(i[0],i[1],i[2],i[3],i[4]))
print("""
                                          </tbody>
                                          </table>
                                    </div>
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
             let Fullname=document.forms["volunteeraddform"]["fullname"].value;
             let Email=document.forms["volunteeraddform"]["email"].value;
             let Pnumber=document.forms["volunteeraddform"]["pnumber"].value;


            if(Fullname==null || Fullname==""){
                document.getElementById("errors").innerHTML="enter a Full name !";
                return false;
            }
            if(Email==null || Email==""){
                document.getElementById("errors").innerHTML="enter a email address !";
                return false;
            }
            if(Pnumber==null || Pnumber==""){
                document.getElementById("errors").innerHTML="enter a phone number !";
                return false;
            }
            if(Fullname != "" && Email != "" && Pnumber != ""){
                return true;
            }
        }
    </script>
    
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"></script>
</body>
</html>""")


#!C:/Users/Naveenkumar/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi,cgitb,smtplib

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
                
                        /*form style*/
                
                #dashboard input{
                    outline: none;
                    border-color:#fffcfd;
                    background-color: #F50057;
                    color: #fcfbfb;
                    border-radius: 10px;
                    height: 3rem;
                    font-weight: 500;
                    text-transform: uppercase;
                }
                #dashboard  label{
                    color: #F50057;
                    font-weight: 500;
                }
                #dashboard button{
                    background-color: #f9f9f9;
                    color: #F50057;
                    border-color: #F50057;
                    font-weight: 600;
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
                
                            /*for table responsive*/
                
                @media screen and (min-width:320px) and (max-width:640px){
                    #deltab *{
                        font-size:10px;
                    }
                }
                @media screen and (min-width:320px) and (max-width:426px){
                    #deltab *{
                        font-size:6px;
                    }
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
              
                    <!---user dashboard--->
                
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
                            <span class="my-3 d-flex justify-content-center align-items-center" style="color:#f9f9f9;width:100px;height:100px;font-size: 50px;border-radius: 50%;background-color: #FF4081;">A</span>
                            <h2 style="color:white;font-weight: 600;">Hii</h2>
                            <h3 style="color:#eeeeee">Admin</h3>
                        </div>
                        
                            <!-- dashmenus -->
                        
                        <div class="row dashmenus my-4">
                            <ul class="nav navbar-nav py-4" style="padding-right: 0px;">
                                <li class="nav-item my-2">
                                    <a id="spfm" href="/SportsEventOrganize/admindashboard.py" class="nav-link text-center" style="font-weight: 700;color:#F50057; !important;
                                    background-color: #eeeeee; !important;">Sports Faculty</a>
                                </li>
                                
                                <li class="nav-item my-2">
                                    <a id="Users" href="#" class="nav-link text-center" style="font-weight: 700;background-color:black;color: #eeeeee;">Users</a>
                                </li>
                                
                                <li class="nav-item my-2">
                                    <a id="Events" href="/SportsEventOrganize/admin_events.py" class="nav-link text-center" style="font-weight: 700;background-color: #eeeeee;color: #F50057 ;">Events</a>
                                </li>
                                
                                 <li class="nav-item my-2">
                                    <a id="Results" href="/SportsEventOrganize/admin_results.py" class="nav-link text-center" style="font-weight: 700;background-color: #eeeeee;color: #F50057 ;">Results Of Events</a>
                                </li>
                            </ul>
                        </div>

                </div>
                <div class="col-lg-9 col-12 definitions p-0 mt-lg-0 mt-1">
                <section id="userslist">
                            <div class="container-fluid p-0">
                                <div class="row-12">
                                    <h2 style="background-color:#F50057;color:white;text-transform:uppercase;font-weight:700;font-size:25px;" class="text-center m-0">New Volunteers</h2>
                                    <div class="newvolundetails">
                                        <table class="table table-bordered" id="deltab">
                                        
                                        <thead>
                                          <tr>
                                              <th scope="col" style="color:#F50057 !important">id</th>
                                              <th scope="col" style="color:#F50057 !important">Fullname</th>
                                              <th scope="col" style="color:#F50057 !important">Email</th>
                                              <th scope="col" style="color:#F50057 !important">Status</th>
                                          </tr>
                                        </thead>
                                        <tbody style="border-color:white !important;background-color:#F50057 !important;color:white !important;">""")

q="""select * from volunteers where status='' """
cur.execute(q)
res=cur.fetchall()

for i in res:
    print("""
                                            <tr>
                                              <form action=""  name="idform"  method="post" enctype="multipart/form-data" >
                                              <td>
                                                <input type="text" value="%s" name="id" readonly style="width:25px;border:none;padding:0px !important;text-transform:capitalize;">
                                              </td>
                                              <td class="d-flex justify-content-center align-items-center" style="text-transform:capitalize;padding:18px !important";">%s</td>
                                              <td style="padding:18px !important";">%s</td>
                                              <td style="padding:18px !important";text-transform:capitalize;">%s</td>
                                              <td class="d-flex justify-content-evenly align-items-center">
                                                <input type="submit" class="btn btn-success my-3" style="font-size:15px;background-color:white;color:#F50057;margin:0px !important;width:100px;height:40px;" name="app" value="Approved">
                                                <input type="submit" class="btn btn-danger my-3" style="font-size:15px;background-color:white;color:#F50057;margin:0px !important;width:100px;height:40px;" name="rej" value="Reject">  
                                              </td>
                                              </form>
                                            </tr>
                                          """%(i[0],i[1],i[2],i[3]))
form=cgi.FieldStorage()
App=form.getvalue("app")
Rej=form.getvalue("rej")
pid=form.getvalue("id")

if App!=None:
    q="""update volunteers set status='Approved' WHERE id='%s' """%pid
    cur.execute(q)
    q="""select fullname,email from volunteers where id='%s' """%pid
    cur.execute(q)
    rec=cur.fetchone()
    faddress='12345nk333@gmail.com'
    passwd='rfmsjlpmhzkehbpk'
    toaddress=rec[1]
    Username='sportshead'
    subject='You Appointed as a volunteer'
    body='Welcome..{} \n\n Username:{} \n\n Password:{}'.format(rec[0],Username,rec[0])
    msg="""Subject:{} \n\n {}""".format(subject,body)
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(faddress,passwd)
    server.sendmail(faddress,toaddress,msg)
    server.quit()
    print("""
        <script>
            alert("Mail Sending Succesfully");
        </script>
        """)

    conn.commit()

elif Rej!=None:
    q="""delete from volunteers WHERE id='%s' """%(pid)
    cur.execute(q)
    conn.commit()


print("""
                                          </tbody>
                                          </table>
                                    </div>
                                </div>
                                <div class="row-12">
                                    <h2 style="background-color:#F50057;color:white;text-transform:uppercase;font-weight:700;font-size:25px;" class="text-center m-0">Existing Volunteers</h2>
                                    <div class="existvolundetails">
                                        <table class="table table-bordered" id="deltab">
                                        <thead>
                                          <tr>
                                              <th scope="col" style="color:#F50057 !important">id</th>
                                              <th scope="col" style="color:#F50057 !important">Fullname</th>
                                              <th scope="col" style="color:#F50057 !important">Email</th>
                                              <th scope="col" style="color:#F50057 !important">Phonenumber</th>
                                              <th scope="col" style="color:#F50057 !important">Status</th>
                                          </tr>
                                        </thead>
                                        <tbody style="border-color:white !important;background-color:#F50057 !important;color:white !important;">""")


w="""select * from volunteers where status='Approved' """
cur.execute(w)
res1=cur.fetchall()

for i in res1:
    print("""
                                          <tr>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td>%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                          </tr>"""%(i[0],i[1],i[2],i[3],i[4]))

print("""
                                          </tbody>
                                          </table>
                                    </div>
                                </div>
                                <div class="row-12">
                                    <h2 style="background-color:#F50057;color:white;text-transform:uppercase;font-weight:700;font-size:25px;border-left:2px solid white;" class="text-center m-0">Student Details</h2>
                                    <div class="studetails">
                                        <table class="table table-bordered" id="deltab">
                                        <thead>
                                          <tr>
                                              <th scope="col" style="color:#F50057 !important">id</th>
                                              <th scope="col" style="color:#F50057 !important">Event name</th>
                                              <th scope="col" style="color:#F50057 !important">Username</th>
                                              <th scope="col" style="color:#F50057 !important">Fullname</th>
                                              <th scope="col" style="color:#F50057 !important">DateofBirth</th>
                                              <th scope="col" style="color:#F50057 !important">Mobilenumber</th>
                                          </tr>
                                        </thead>
                                        <tbody style="border-color:white !important;background-color:#F50057 !important;color:white !important;">""")
q="""select * from sturegister"""
cur.execute(q)
res=cur.fetchall()
for i in res:
    print("""

                                          <tr>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                              <td style="text-transform:capitalize;">%s</td>
                                          </tr>
                                          """%(i[0],i[1],i[2],i[3],i[4],i[5]))
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
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"></script>
</body>
</html>""")

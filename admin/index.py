#!"C:/Users/Eshita/anaconda3/python.exe"
import cgi
import mysql.connector as conn
try:
    db = conn.connect(host='localhost',user='root',passwd='',db='kph')
    cursor = db.cursor()
    print('''Content-type:text/html\n\n
<!DOCTYPE html>
<html lang="en">
<head>
  <script src="https://code.jquery.com/jquery-1.9.1.js"></script>
    <!-- Basic Page Needs
  ================================================== -->
    <meta charset="utf-8">
    <title>Asansol Pizzaria | Home</title>
    <link rel="shortcut icon" href="images/favicon.png" type="image/x-icon">
    <meta name="keyword" content="Asansol Pizzaria">
    <meta name="Description" content="Pizza Online Delivery">

    <!-- Mobile Specific Metas
  ================================================== -->
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

    <!-- CSS
  ================================================== -->
    <script src="js/admin-js.js"></script>
    <link href="css/admin-css.css" rel="stylesheet"/>
    <!--[if lt IE 9]>
		<script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script>
	<![endif]-->
</head>
<body style="background-image: url(images/bg.png);
                 background-size: 30%;
                 background-color: rgba(184, 219, 38, 0.24); 
                 background-blend-mode: multiply">

    <div class="container">
        <div class="flat-form">
            <ul class="tabs">
                <li>
                    <a href="#login" class="active">Login</a>
                </li>
                <!--<li>
                    <a href="#register">Register</a>
                </li>
                <li>
                    <a href="#reset">Reset Password</a>
                </li>-->
            </ul>
            <div id="login" class="form-action show">
                <h1 style="text-align: center">Asansol Pizzaria</h1>
                <p style="text-align: center">
                    Administrators can only login.
                    <b>Unauthorized Access Prohibited</b>
                </p>''')
    formData = cgi.FieldStorage()
    error = formData.getvalue('error')

    #print(error)
    if error == '1':
        print("""<h2>Invalid Login Credential<h2>""")
    print('''
                <form method="get" action="login.py">
                    <ul>
                        <li>
                            <input type="text" placeholder="Username" name="username"/>
                        </li>
                        <li>
                            <input type="password" placeholder="Password" name="password"/>
                        </li>
                        <li><input type="hidden" name="error" value="0"/>
                            <input type="submit" value="Login" class="button"/>
                        </li>
                    </ul>
                </form>
            </div>
            <!--/#login.form-action-->
            <!--<div id="register" class="form-action hide">
                <h1>Register</h1>
                <p>
                    New members have to register first to access.
                </p>
                <form>
                    <ul>
                        <li>
                            <input type="text" placeholder="Username" />
                        </li>
                        <li>
                            <input type="password" placeholder="Password" />
                        </li>
                        <li>
                            <input type="submit" value="Sign Up" class="button" />
                        </li>
                    </ul>
                </form>
            </div>-->
            <!--/#register.form-action
            <div id="reset" class="form-action hide">
                <h1>Get Password</h1>
                <p>
                    To get your password enter your Name and your birthday
                    and we'll send you your password.
                    <b></b>
                </p>
                <form>
                    <ul>
                        <li>
                            <input type="text" placeholder="Name" />
                        </li>
                        <li>
                            <input type="text" placeholder="Birthday" />
                        </li>
                        <li>
                            <input type="submit" value="Send" class="button" />
                        </li>
                    </ul>
                </form>
            </div>
            
        </div>-->
    </div>
    <script class="cssdeck" src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.8.0/jquery.min.js"></script>
</body>
</html>''')
except:
    cgi.print_exception()

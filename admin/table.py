#!"C:/Users/Eshita/anaconda3/python.exe"
import cgi
import mysql.connector as conn
db = conn.connect(host='localhost',user='root',passwd='',db='kph')
cursor = db.cursor()
print("""Content-type:text/html\n\n
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Asansol Pizzaria| Admin</title>
    <link rel="shortcut icon" href="images/favicon.png" type="image/x-icon">
    <!-- BOOTSTRAP STYLES-->
    <link href="assets/css/bootstrap.css" rel="stylesheet" />
    <!-- FONTAWESOME STYLES-->
    <link href="assets/css/font-awesome.css" rel="stylesheet" />
    <!-- MORRIS CHART STYLES-->
    <link href="assets/js/morris/morris-0.4.3.min.css" rel="stylesheet" />
    <!-- CUSTOM STYLES-->
    <link href="assets/css/custom.css" rel="stylesheet" />
    <!-- GOOGLE FONTS-->
    <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css' />
</head>

<body>
    <div id="wrapper">
        <nav class="navbar navbar-default navbar-cls-top " role="navigation" style="margin-bottom: 0">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".sidebar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="dashboard.html">Administrator</a>
            </div>
            <div style="color: white;
padding: 15px 50px 5px 50px;
float: right;
font-size: 16px;"> Don't Leave : Logged In &nbsp; <a href="index.py" class="btn btn-danger square-btn-adjust">Logout</a> </div>
        </nav>
        <!-- /. NAV TOP  -->
        <nav class="navbar-default navbar-side" role="navigation">
            <div class="sidebar-collapse">
                <ul class="nav" id="main-menu">
                    <li class="text-center">
                        <img src="assets/img/administrator1.png" class="user-image img-responsive" />
                    </li>


                    <li>
                        <a class="active-menu" href="dashboard.html"><i class="fa fa-dashboard fa-3x"></i> Dashboard</a>
                    </li>
                    <li>
                        <a href="getmsg.py"><i class="fa fa-qrcode fa-3x"></i> Contact Messages</a>
                    </li>
                    <li>
                        <a href="table.py"><i class="fa fa-table fa-3x"></i> Tables In Database</a>
                    </li>
                    <!--<li>
                        <a href="#"><i class="fa fa-edit fa-3x"></i> Forms </a>
                    </li>-->
                    <li  >
                        <a class="active-menu"  href="orders.py"><i class="fa fa-square-o fa-3x"></i> Orders</a>
                    </li>
                </ul>

            </div>

        </nav>
        <!-- /. NAV SIDE  -->
        <div id="page-wrapper" >
            <div id="page-inner">
                <div class="row">
                    <div class="col-md-12">
                     <h2>Contact Messages </h2>   
                        <!--<h5>Welcome to Kolkata Pizza Hub , Love to see you back. </h5>-->
                       
                    </div>
                </div>
                 <!-- /. ROW  -->
                 <hr />""")
sql = "select * from booking"
cursor.execute(sql)
order = cursor.fetchall()
print('''<div class="row">
                <div class="col-md-6">
                  <!--   Kitchen Sink -->
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Booking
                        </div>
                        <div class="panel-body">
                            <div class="table-responsive">
                                <table class="table table-striped table-bordered table-hover">
                                    <thead><tr>
                                            <th>#</th>
                                            <th>Time</th>
                                            <th>Date</th>
                                            <th>Person</th>
                                        </tr></thead><tbody>''')
for each in order:
    print('''
                                        <tr class="odd gradeX">
                                            <td class="center">{0}</td>
                                            <td class="center">{1}</td>
                                            <td class="center">{2}</td>
                                            <td class="center">{3}</td>                                          
                                        </tr>
                '''.format(each[0],each[1],each[2],each[3]))
    #print(each)
print('''            
            
            
    
                                        
                  </tbody>
                                </table>
                            </div>
                        </div>
                    </div></div>''')

                    
sql = "select * from contact"
cursor.execute(sql)
order = cursor.fetchall()    
print('''<div class="col-md-6">
<div class="panel panel-default">
                        <div class="panel-heading">
                            Contact
                        </div>
                        <div class="panel-body">
                            <div class="table-responsive">
                                <table class="table table-striped table-bordered table-hover">
                                    <thead><tr>
                                            <th>Name</th>
                                            <th>Email</th>
                                            <th>Message</th>
                                           
                                        </tr></thead><tbody>''')
for each in order:
    print('''
                                        <tr class="odd gradeX">
                                            <td class="center">{0}</td>
                                            <td class="center">{1}</td>
                                            <td class="center">{2}</td>
                                                                                
                                        </tr>
                '''.format(each[0],each[1],each[2]))
    #print(each)
print('''            
            
            
    
                                        
                  </tbody>
                                </table>
                            </div>
                        </div>
                    </div>                    
                    
                    
                     <!-- End  Kitchen Sink -->
                </div>
            </div>                  
                <hr/>
             <!-- /. PAGE INNER  -->''')





sql = "select * from coupon"
cursor.execute(sql)
order = cursor.fetchall()
print('''<div class="row">
                <div class="col-md-6">
                  <!--   Kitchen Sink -->
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Coupon
                        </div>
                        <div class="panel-body">
                            <div class="table-responsive">
                                <table class="table table-striped table-bordered table-hover">
                                    <thead><tr>
                                            <th>Name</th>
                                            <th>Code</th>
                                            
                                        </tr></thead><tbody>''')
for each in order:
    print('''
                                        <tr class="odd gradeX">
                                            <td class="center">{0}</td>
                                            <td class="center">{1}</td>
                                            
                                        </tr>
                '''.format(each[0],each[1]))
    #print(each)
print('''            
            
            
    
                                        
                  </tbody>
                                </table>
                            </div>
                        </div>
                    </div></div>''')

                    
sql = "select * from orders"
cursor.execute(sql)
order = cursor.fetchall()    
print('''<div class="col-md-6">
<div class="panel panel-default">
                        <div class="panel-heading">
                            Orders
                        </div>
                        <div class="panel-body">
                            <div class="table-responsive">
                                <table class="table table-striped table-bordered table-hover">
                                    <thead><tr>
                                            <th>Order Id</th>
                                            <th>Details</th>
                                            <th>Name</th>
                                            <th>Phone Number</th>
                                            <th>Email id</th>
                                            <th>Address</th>
                                           
                                        </tr></thead><tbody>''')
for each in order:
    print('''
                                        <tr class="odd gradeX">
                                            <td class="center">{0}</td>
                                            <td class="center">{1}</td>
                                            <td class="center">{2}</td>
                                            <td class="center">{3}</td>
                                            <td class="center">{4}</td>
                                            <td class="center">{5}</td>
                                                                                
                                        </tr>
                '''.format(each[0],each[1],each[2],each[3],each[4],each[5]))
    #print(each)
print('''            
            
            
    
                                        
                  </tbody>
                                </table>
                            </div>
                        </div>
                    </div>                    
                    
                    
                     <!-- End  Kitchen Sink -->
                </div>
            </div>                  
                <hr/>
             <!-- /. PAGE INNER  -->''')








sql = "select * from pizza"
cursor.execute(sql)
order = cursor.fetchall()
print('''<div class="row">
                <div class="col-md-6">
                  <!--   Kitchen Sink -->
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Pizza\'s
                        </div>
                        <div class="panel-body">
                            <div class="table-responsive">
                                <table class="table table-striped table-bordered table-hover">
                                    <thead><tr>
                                            <th>Pizza Name</th>
                                            <th>Image</th>
                                            <th>Id</th>
                                            <th>Size</th>
                                            <th>Price</th>
                                            
                                        </tr></thead><tbody>''')
for each in order:
    print('''
                                        <tr class="odd gradeX">
                                            <td class="center">{0}</td>
                                            <td class="center"><img src="/tools/Kolkata Pizza Hub/www/images/pizza_menu/{1}" alt="" height="60px" width="60px"></td>
                                            <td class="center">{2}</td>
                                            <td class="center">{3}</td>
                                            <td class="center">{4}</td>
                                            
                                        </tr>
                '''.format(each[0],each[1],each[2],each[3],each[4]))
    #print(each)
print('''            
            
            
    
                                        
                  </tbody>
                                </table>
                            </div>
                        </div>
                    </div></div>''')

                    
sql = "select * from topping"
cursor.execute(sql)
order = cursor.fetchall()    
print('''<div class="col-md-6">
<div class="panel panel-default">
                        <div class="panel-heading">
                            Topping\'s
                        </div>
                        <div class="panel-body">
                            <div class="table-responsive">
                                <table class="table table-striped table-bordered table-hover">
                                    <thead><tr>
                                            <th>Image</th>
                                            <th>Id</th>
                                            <th>Name</th>
                                           
                                        </tr></thead><tbody>''')
for each in order:
    print('''
                                        <tr class="odd gradeX">
                                            <td class="center"><img src="/tools/Kolkata Pizza Hub/www/images/pizza_top/{0}" alt=""></td>
                                            <td class="center">{1}</td>
                                            <td class="center">{2}</td>
                                        
                                                                                
                                        </tr>
                '''.format(each[0],each[1],each[2]))
    #print(each)
print('''            
            
            
    
                                        
                  </tbody>
                                </table>
                            </div>
                        </div>
                    </div>                    
                    
                    
                     <!-- End  Kitchen Sink -->
                </div>
            </div>                  
                <hr/>
             <!-- /. PAGE INNER  -->''')











print('''            </div></div>
         <!-- /. PAGE WRAPPER  -->
        </div>
     <!-- /. WRAPPER  -->
    <!-- SCRIPTS -AT THE BOTOM TO REDUCE THE LOAD TIME-->
    <!-- JQUERY SCRIPTS -->
    <script src="assets/js/jquery-1.10.2.js"></script>
      <!-- BOOTSTRAP SCRIPTS -->
    <script src="assets/js/bootstrap.min.js"></script>
    <!-- METISMENU SCRIPTS -->
    <script src="assets/js/jquery.metisMenu.js"></script>
      <!-- CUSTOM SCRIPTS -->
    <script src="assets/js/custom.js"></script>''')

print("""</body>
    </html>""")



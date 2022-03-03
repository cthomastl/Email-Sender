class rest:
 def getName(userName):
# User Startup Screen
   print("Hi, Welcome to the automated email sender")
name=input("What is your name?: ")
userName=input(name + ", " + "Create a username: ")
passWord = int(input(name + ", " + "Create a password: "))



print(" Menu: \n\t")
print(" Email Application \n\t ")

selection =input(" press y to go back to the menu or x to start the Emailer Application \n\t ")
if selection == (" y "):
 quit()
elif selection == (" x "):
  (" Loading ")
   


# Sign in Authentication
print(" Sign in \n\t ")
passWord = int(input("Welome back user " + userName +", " + " Please enter your password: "))
if passWord == passWord:
    ("Success! \n\t ... \n\t  ")



  
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("Welcome to the email sender! ")

receiver_email = "morrisemelia@gmail.com"
password = input("Type your password and press enter: \n\t ")
sender_email = input("Type your email name and press enter: \n\t ")
message = MIMEMultipart("alternative")
message["Subject"] = "Hi, this is " + name + " ! "+  " Please make a reservation here"
message["From"] = sender_email
message["To"] = receiver_email



text = """
Hi,
How are you? 
"""
html =  """ 

  <!DOCTYPE html>
<html>
  <head>
    <title>Simple login form</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet">
    <style>
      html, body {
      display: flex;
      justify-content: center;
      font-family: Roboto, Arial, sans-serif;
      font-size: 15px;
      }
      form {
      border: 5px solid #f1f1f1;
      }
      input[type=text], input[type=password] {
      width: 100%;
      padding: 16px 8px;
      margin: 8px 0;
      display: inline-block;
      border: 1px solid #ccc;
      box-sizing: border-box;
      }
      button {
      background-color: #2e9ccf;
      color: white;
      padding: 14px 0;
      margin: 10px 0;
      border: none;
      cursor: grabbing;
      width: 100%;
      }
      h1 {
      text-align:center;
      fone-size:18;
      }
      button:hover {
      opacity: 0.8;
      }
      .formcontainer {
      text-align: left;
      margin: 24px 50px 12px;
      }
      .container {
      padding: 16px 0;
      text-align:left;
      }
      span.psw {
      float: right;
      padding-top: 0;
      padding-right: 15px;
      }
      /* Change styles for span on extra small screens */
      @media screen and (max-width: 300px) {
      span.psw {
      display: block;
      float: none;
      }
    </style>
  </head>
  <body>
    <form action="/action_page.php">
      <h1>Hi, here is your Reservation Form</h1>
      <div class="formcontainer">
      <hr/>
      <div class="container">
        <label for="uname"><strong>Name</strong></label>
        <input type="text" placeholder="Enter Username" name="uname" required>
        <label for="psw"><strong>Phone number</strong></label>
        <input type="password" placeholder="Enter Password" name="psw" required>
      </div>
      <button type="submit">Login</button>
      <div class="container" style="background-color: #eee">
        <label style="padding-left: 15px">
        <input type="checkbox"  checked="checked" name="remember"> Reserve my spot
        </label>
        <span class="psw"><a href="#"> Forgot password?</a></span>
      </div>
    </form>
  </body>
</html>

"""


part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")


message.attach(part1)
message.attach(part2)


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
  
print("Success! thank you for using the Email application")

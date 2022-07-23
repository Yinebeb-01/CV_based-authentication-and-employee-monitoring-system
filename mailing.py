import imghdr
import os
import smtplib
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import random
from datetime import datetime
import time
from tkinter import Label, LabelFrame, Entry, Button, StringVar, Toplevel
from tkinter.tix import Tk
import imaplib
import base64

from DataBase import Database
from Display import Display
from keypad import KeyPad


class Mailing:

    def generateOtp(self, email):
        {completet the code along ypur otp age}

    def gustModeOtp(self):
        {completet the code by yourself}

        # self.sentVerificationeMaile(email, otp)
        otpDeth = otpBirth + otpAge
        return otp, otpDeth

    def sentVerificationeMaile(self, email, otp):
        message = MIMEMultipart("alternative")
        message["Subject"] = "VERIFICATION CODE "
        message["From"] = "alomansimlo@gmail.com"
        message["To"] = email
        html = f"""\
        <html>
          <body>
            <h4>One Time Verification Code</h4><hr>
             <p>
              your one time verification code is <b> {otp}  </b>
              .This code will be expired after 30 seconds.Enter the code to the system using the keypad before it expired.<br>
              <b style ="color: rgb(200,120,110)">Don't give this code to anyone !</b>  
              <br>
              <br>
               <b>Contact the system admin if you need help</b>
               <p>   Click on <a href="tel:0969139694">make a call  </a> 
               <p>   Click on <a href="mailto: yosfemyayu@gmail.com">send an email</a>
              <br>
              <br>
              <br>
              <h5> From <i>From CV Based Authentication And Employee Monitoring System.</i></h5><hr>
            </p>
          </body>
        </html>
        From CV Based Authentication And Employee Monitoring System 
        """
        part = MIMEText(html, "html")
        message.attach(part)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login('username@gmail.com', 'password')
            server.sendmail('username@gmail.com', email, message.as_string())
            server.quit()
        print("====")

    def sentAdminAllert(self, email, imageDirectory, otp, gustPhone):
        message = MIMEMultipart("alternative")
        message["Subject"] = "Access Alert(Guest mode)  "
        message["From"] = 'username@gmail.com'
        message["To"] = email

        html = f"""\
            <html>
                <body>
                    <h4 style="color:brown">Someone Is Requesting Your Permission </h4>
                    <hr>
                    <p style="font-family:'Times New Roman', Times, serif">
                        Someone whose picture attached bellow is waiting your permission to enter to the room.
                        if you take all the responsibility,you can give him/her guest mode right to
                        access the system as a guest.A one Times gust code for this gust is <strong style=" color:rgb(209, 19, 19)">
                            {otp}
                        </strong>
    
                        
                        
                        
                        
                        <br>
                        <br>
                        <a><img src="cid:image1" alt="image of the guest" ></a>  
                            <a><img src=" cid:image2" alt="image of the guest" ></a>  
                            <a><img src=" cid:image3" alt="image of the guest" ></a>  
                             <br>
                             <br>
                            If you don't  give access right to the guest with in 30 second, An <b>" Access is Denied"</b> message is
                            sent to him/her
                            automatically.
                            <br>
                            <br>
                            <i style="margin-left:20px;font-size:large;font-weight:bold; color:rgb(165, 116, 42);">Tell the code to the gust <br></i>
                            <br>

                
                            <a style="background-color: #13aa52;border: 1px solid #13aa52;border-radius: 4px; box-shadow: rgba(0, 0, 0, .1) 0 2px 4px 0;font-size: 16px;font-weight: 400;
                              outline: none;outline: 0;color:white;
                              padding: 10px 60px;
                              margin-left:60px;
                              text-align: center;
                            " 
                             href="tel:{gustPhone}"> Make a call                            
                            </a><br>
                            
            
                            <br>
                            <br>
                            <br>
                            <br>
                            <h5> From <i style="color:rgb(244,157,232)">From CV Based Authentication And Employee Monitoring
                                    System.</i>
                            </h5>
                            <hr>
                    </p>
                </body>    
            </html>
        """




        part = MIMEText(html, "html")
        message.attach(part)
        image_id = 1
        for image in os.listdir(imageDirectory):
            fb = open(imageDirectory + "//" + image, 'rb')
            imageAttachment = MIMEImage(fb.read())
            imageAttachment.add_header('Content-ID', f'<image{image_id}>')
            fb.close()
            message.attach(imageAttachment)
            image_id = image_id + 1

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login('alomansimlo@gmail.com', 'eursyrglckkepyxm')
            server.sendmail('alomansimlo@gmail.com', email, message.as_string())
            server.quit()
        print("====")

    def sentMail(self, email, subject, header, messages):

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = 'alomansimlo@gmail.com'
        message["To"] = email
        html = f"""\
        <html>
          <body>
            <h4>{header} </h4><hr>
             <p>
             {messages}
             <br>
             <br>
             <br>
             <br>
               <b>System Admins Address</b>
               <p>   Click on <a href="tel:0969139694">make a call  </a> 
               <p>   Click on <a href="mailto: yosfemyayu@gmail.com">send an email</a>
              <br>
              <br>
              <h5> From <i style = "color:rgb(244,157,232)">From CV Based Authentication And Employee Monitoring System.</i></h5><hr>
            </p>
          </body>
        </html>
        """
        part = MIMEText(html, "html")
        message.attach(part)

        # text = MIMEText('<img src="cid:image1">', 'html')
        # msg.attach(text)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login('alomansimlo@gmail.com', 'eursyrglckkepyxm')
            server.sendmail('alomansimlo@gmail.com', email, message.as_string())
            server.quit()
        print("maile sent===================")

    # this method replace by lcd and keypad interface
    def TwofactorAuthontication(self):
        display = Display()
        display.lcdPrint("Authenticatation", 1)
        display.lcdPrint("Via 2FA ", 2)
        time.sleep(3)

        keypad = KeyPad()
        userID = keypad.getKeyPadInput("UserID")

        db = Database()
        object = db.getEmpPassEmailId(userID)
        # password = object[0][0]
        # email = object[0][1]
        # id = object[0][2]

        trialLimit = 3
        trial = 0
        while trial < trialLimit:
            keypad = KeyPad()
            password = keypad.getKeyPadInput("Password")
            if password == object[0]:
                display.lcdPrint("Emailing OTP..", 1)
                display.lcdPrint("Cheak your Email", 2)
                time.sleep(3)

                # geberate otp and emaile it to the user
                sys_otp, otpDeth = self.generateOtp(object[1])

                while time.time() < otpDeth:
                    keypad = KeyPad()
                    user_otp = keypad.getKeyPadInput("OTP")
                    if user_otp == sys_otp:
                        display.lcdPrint("--Wellcome--", 1)
                        return object[2]

                    else:
                        display.lcdPrint("--incorrect--", 1)
                        display.lcdPrint("Cheak your Email", 2)
                        time.sleep(3)

                display.lcdPrint("Current OTP Expired!--", 1)

            # ==================for testing case break it

            else:
                display.lcdPrint("--Incorrect !--", 1)
                display.lcdPrint("Please try again", 2)
                time.sleep(3)
                keypad = KeyPad()
                uerID = keypad.getKeyPadInput("UserID")
                object = db.getEmpPassEmailId(userID)

            trial += 1
            if trial >= trialLimit:
                display.lcdPrint("-- Wrong User--", 1)
                display.lcdPrint("Pls Contact admins", 2)
                time.sleep(3)
        # ==================terminate authentication process

        # print('email =', email)
        # print('pasword = ',password)
        # sprint(db.getEmployees())

        return -1

    def gustMode(self, email, dire):
        # e min request 
        otpAge = 3*60
        charset = '0123456789ABCD'
        otp = ""

        # generate four digit OTP(random number)
        for i in range(4):
            otp += str(charset[random.randint(0, len(charset) - 1)])

        display = Display()
        display.lcdPrint("with your phone", 1)
        display.lcdPrint("we will contact u", 2)
        time.sleep(3)
        display.lcdPrint("Enter your phone", 2)

        keypad = KeyPad()
        gustPhone = keypad.getKeyPadInput("phone")

        self.sentAdminAllert(email=email, imageDirectory=dire,
                             otp=otp, gustPhone=gustPhone)
        otpBirth = time.time()
        otpDeth = otpBirth + otpAge

        # inform the gust the request is sent
        display.lcdPrint("===Well done===", 1)
        display.lcdPrint("Request is sent..", 2)
        time.sleep(3)

        trialLimit = 4
        trial = 0

        while time.time() < otpDeth:
            keypad = KeyPad()
            gust_otp = keypad.getKeyPadInput("OTP")
            if gust_otp == otp:
                display.lcdPrint("--Wellcome--", 1)
                # id -2 used for gustMode
                return -2

            else:
                display.lcdPrint("--incorrect--", 1)
                display.lcdPrint("Pls Contact admins", 2)
                time.sleep(3)
            trial += 1
            if trial >= trialLimit:
                display.lcdPrint("--Wrong Trial--", 1)
                display.lcdPrint("Pls Contact admins", 2)
                time.sleep(3)
                return -1

        # probably the admin is not respond with in 30 second
        display.lcdPrint("Request Canceled", 1)
        # id -1 used for invalid user
        return -1

    def login(self, userId, password):
        db = Database()
        email = db.getEmployeeEmail(userId, password)
        if len(email) > 0:
            otp, age = self.generateOtp(email[0][0])
            for widgets in self.root.winfo_children():
                widgets.destroy()

            self.frame2 = LabelFrame(self.root, text="Activation code(OTP) is sen", padx=30, pady=30,
                                     font=('times', 15, 'italic'),
                                     fg='#9a1e1e')
            self.frame2.pack(pady=40)

            # labelTitle = Label(self.frame2, text="Activation code(OTP) is sent to your email Optional ", fg='blue', font=('times', 10, 'bold'),
            #                    pady=10,
            #                    width=850)
            # labelTitle.grid(row = 0,column =0,columnspan = 1)

            label1 = Label(self.frame2, text="OTP", font=('times', 13, 'bold')).grid(row=1, column=0, sticky='e')

            self.otpE = Entry(self.frame2, font=('times', 13, 'italic'), width=20, fg='blue')
            self.otpE.grid(row=1, column=1)

            buttenLogin = Button(self.frame2, text="Authenticat", font=('times', 13, 'bold italic'), fg='blue',
                                 width='20', bg="#88cffa",
                                 pady=5, command=lambda: self.verify(self.otpE.get(), otp, age)).grid(pady=10, row=9,
                                                                                                      column=0,
                                                                                                      columnspan=2,
                                                                                                      sticky='ew')



        else:
            print("invalid user UserId or password")

    def callback(self, input):
        if input == "":
            print(input)
            return True
        else:
            last = str(input)[-1]
            if last.isdigit():
                print(input)
                return True
            elif last in str("ABCD"):
                print(input)
                return True
            else:
                print(input)
                return False

    def verify(self, otpe, otp, age):
        d = Display()
        now = time.time()

        if now <= age:
            if otpe == otp:
                print("==succees |Door opened! (?)")
                # lcd print
                d.lcdPrint("Door OPened!", 1)

            else:
                print('invalied otp')
                d.lcdPrint("invalied otp!", 1)

        else:
            print("==otp is expired")
            d.lcdPrint("OTP expired!", 1)
        pass

# def showWindow(self):
# d = Mailing().sentAdminAllert('yosfemyayu@gmail.com','Gusts')
# print("sedted")
# d.root.mainloop()

##################################################################################
# Using version 3.8.7
##################################################################################
import sys, os, ctypes, winshell
import nncam
os.add_dll_directory(os.getcwd()) # Python 3.8 needs this

from win32com.shell import shell, shellcon

from struct import *

import numpy as np
from datetime import datetime
import time
from PIL import Image as ImagePIL
import piexif
from cv2 import rotate, ROTATE_90_CLOCKWISE, ROTATE_180, ROTATE_90_COUNTERCLOCKWISE, flip, imwrite, IMWRITE_TIFF_COMPRESSION, \
                IMWRITE_JPEG_QUALITY, INTER_LINEAR
from cv2 import resize as resizeCV2
from GUI_Main import *
from mouseStuff import *
from Hardware import HardwareControl
from pathlib import Path
import seqfile

import configparser
from appdirs import *
import PyPDF2
from PyPDF2.generic import AnnotationBuilder

from PySide2 import QtCore, QtWidgets
# import pyqtgraph as pg
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
# from matplotlib.figure import Figure
# from matplotlib import pyplot as plt

from threadWork import Worker, WorkerSignals, ThreadFunctions
from FactorySettings import *


delayCommand = 0.001  # Delay between commands
pin_OFF = b'\x00'  # Pin Low
pin_ON = b'\x01'  # Pin High

pinMains = b'\x04'  # Mains
pinTUV = b'\x05'  # Trans UV
pinEWL = b'\x06'  # Epi White Light
pinTWL = b'\x07'  # Trans White Light
pinTBL = b'\x17'  # Trans Blue Light
pinEUVA = b'\x19'  # Epi UV A
pinEUVB = b'\x1B'  # Epi UV B
pinSpare = b'\x24'  # Spare pin
allPins = [b'\x04', b'\x05', b'\x06', b'\x07', b'\x17', b'\x19', b'\x1B', b'\x24']

focusFar = b'\x60'  #
focusNear = b'\x61'  #
irisOpen = b'\x62'  #
irisClose = b'\x63'  #
zoomIn = b'\x64'  #
zoomOut = b'\x65'  #
filterLeft = b'\x66'  #
filterRight = b'\x67'  #

level3 = b'\x03'
level2 = b'\x02'
level1 = b'\x01'


appName = "GelProCCD"
appAuthor = "BiozenLabs"

# ================================ Indranil Kavyant ======================================
from hashlib import md5
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sqlite3 as db
import platform
import pandas as pd
from datetime import datetime
import pickle
import shutil


from endesive import pdf, hsm

import PyKCS11 as PK11
import pdfkit

Login_System_Needed = True; # True if Login Panel is needed

# ================================ Login Code Begins ======================================
if(Login_System_Needed):

    path_wkhtmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
    check_wkhtmltopdf = os.path.isfile(path_wkhtmltopdf)
    print(check_wkhtmltopdf)
    print(path_wkhtmltopdf)

    if check_wkhtmltopdf:
        # config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    #==================================== Defining dll path for DSC ==================================

    if sys.platform == 'win32':
        dllpath =[ r'c:\windows\System32\eps2003csp11.dll', r'c:\windows\System32\mTokenMiniDrv.x64.dll',r'c:\windows\System32\SignatureP11.dll']
    else:
        dllpath = '/usr/lib/WatchData/ProxKey/lib/libwdpkcs_SignatureP11.so'

    # ==================== Database Connection and table creation if no exist =======================
    database = db.connect("C:\ProgramData\ProCCD\dblogin.db") #TODO: Don't hardcode this
    cusror = database.cursor()
    cusror.execute("CREATE TABLE IF NOT EXISTS auth_user(ID INTEGER PRIMARY KEY AUTOINCREMENT, USERNAME VARCHAR(256) UNIQUE, PASSWORD VARCHAR(256) , USERGROUP VARCHAR(50), ACTIVATED BOOL, CREATED_AT DATETIME NOT NULL DEFAULT (datetime('now','localtime')))")
    cusror.execute("CREATE TABLE IF NOT EXISTS requests( ID INTEGER PRIMARY KEY AUTOINCREMENT , USERNAME VARCHAR(256) , REQUESTTYPE VARCHAR(256) )")
    cusror.execute("CREATE TABLE IF NOT EXISTS login_count(ID INTEGER PRIMARY KEY AUTOINCREMENT, USERNAME VARCHAR(256), COUNT INTEGER(5))")
    cusror.execute("CREATE TABLE IF NOT EXISTS action_record (ID INTEGER PRIMARY KEY AUTOINCREMENT ,  USERNAME VARCHAR (256) , ACTIONTIME DATETIME NOT NULL DEFAULT (datetime('now','localtime')) , TYPEOFACTION VARCHAR(256), NEW_VALUE VARCHAR(256) DEFAULT NULL ,DOCUMENT_NAME VARCHAR(256) DEFAULT NULL, COMPUTERNAME VARCHAR(256), EXTRA1 VARCHAR(256) DEFAULT NULL , EXTRA2 DEFAULT NULL ) ")
    cusror.execute("CREATE TABLE IF NOT EXISTS login_record  (ID INTEGER PRIMARY KEY AUTOINCREMENT , USERNAME VARCHAR(256),STATUS VARCHAR(20), COMPUTERNAME VARCHAR(150) , EXTRA1 TEXT DEFAULT NULL, EXTRA2 TEXT DEFAULT NULL, ATTEMPTED_AT DATETIME NOT NULL DEFAULT (datetime('now','localtime')) )")


    #============================= functions for digitally sign document=================================

    def writewithname(username, pdf, outputpdf):
        with open(pdf, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            # Create a PDF writer object
            pdf_writer = PyPDF2.PdfWriter()

            # Copy all pages of the input PDF to the PDF writer object
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])
                date = str(datetime.now())
                annotation = AnnotationBuilder.free_text(
                    f"Signed by : {username} \nDate : {date[0:11]}",
                    rect=(50, 550, 200, 650),
                    font="Arial",
                    bold=True,
                    italic=True,
                    font_size="10pt",
                    font_color="#000000"
                )
                pdf_writer.add_annotation(page_num, annotation)

            # Save the modified PDF to a new file
            with open(outputpdf, 'wb') as output_file:
                pdf_writer.write(output_file)
    class Signer(hsm.HSM):
        pin = ''

        def certificate(self):

            print(self.pkcs11.getSlotList(tokenPresent=True))
            print(self.pkcs11.getTokenInfo(1))

            if self.pin == "":
                self.pin = input("Enter Your pin (Without any spaces ): ")

            self.login("ePass2003", self.pin)  # WF PROXKey is token name.
            keyid = [0x5e, 0x9a, 0x33, 0x44, 0x8b, 0xc3, 0xa1, 0x35, 0x33, 0xc7, 0xc2, 0x02, 0xf6, 0x9b, 0xde, 0x55, 0xfe,
                     0x83, 0x7b, 0xde]
            # keyid = [0x3f, 0xa6, 0x63, 0xdb, 0x75, 0x97, 0x5d, 0xa6, 0xb0, 0x32, 0xef, 0x2d, 0xdc, 0xc4, 0x8d, 0xe8]
            keyid = bytes(keyid)
            try:
                pk11objects = self.session.findObjects([(PK11.CKA_CLASS, PK11.CKO_CERTIFICATE)])
                all_attributes = [
                    # PK11.CKA_SUBJECT,
                    PK11.CKA_VALUE,
                    # PK11.CKA_ISSUER,
                    # PK11.CKA_CERTIFICATE_CATEGORY,
                    # PK11.CKA_END_DATE,
                    PK11.CKA_ID,
                ]

                for pk11object in pk11objects:
                    try:
                        attributes = self.session.getAttributeValue(pk11object, all_attributes)
                    except PK11.PyKCS11Error as e:
                        continue

                    attrDict = dict(list(zip(all_attributes, attributes)))
                    cert = bytes(attrDict[PK11.CKA_VALUE])
                    # if keyid == bytes(attrDict[PK11.CKA_ID]):
                    return bytes(attrDict[PK11.CKA_ID]), cert
            finally:
                self.logout()
            return None, None

        def sign(self, keyid, data, mech):
            self.login("ePass2003", self.pin)
            try:
                privKey = self.session.findObjects([(PK11.CKA_CLASS, PK11.CKO_PRIVATE_KEY)])[0]
                mech = getattr(PK11, 'CKM_%s_RSA_PKCS' % mech.upper())
                sig = self.session.sign(privKey, data, PK11.Mechanism(mech, None))
                return bytes(sig)
            finally:
                self.logout()
    dscdll=''

    def sign_pdf(inputpdf_path, signedpdf_path,pin,dll,name="Kalyan Kundu"):
        date = datetime.datetime.utcnow() - datetime.timedelta(hours=12)
        date = date.strftime('%Y%m%d%H%M%S+00\'00\'')
        dct = {
            "sigflags": 3,
            "sigpage": 0,
            "sigbutton": True,
            "contact": "kalyan@kavyant.com",
            "location": 'India',
            "signingdate": date,  # .encode(),
            "reason": 'Sample sign',
            f"signature": f"{name}\n" + str(date),
            "signaturebox": (25, 25, 200, 200),
        }
        clshsm = Signer(dll)
        clshsm.pin=pin
        fname = inputpdf_path.strip()
        datau = open(fname, 'rb').read()
        datas = pdf.cms.sign(datau, dct,
                             None, None,
                             [],
                             'sha256',
                             clshsm,
                             )
        signed_pdfname = signedpdf_path.strip()
        if (signed_pdfname != ""):
            if signed_pdfname[-4::].lower() == ".pdf":
                pass

            else:
                signed_pdfname += ".pdf"

            with open(signed_pdfname, 'wb') as fp:
                fp.write(datau)
                fp.write(datas)


    class FetchDSC(hsm.HSM):
        def certificate(self):
            tokenlist = self.pkcs11.getSlotList(tokenPresent=True)
            dsc_list = []
            if len(tokenlist) > 0:

                for i in range(1, len(tokenlist) + 1):
                    token = self.pkcs11.getTokenInfo(1)
                    dsc_list.append(token.label.strip())

            return dsc_list




    # ==================== Database Connection and table creation if no exist =======================
    def convertdate(date_string): # This function is for changing date format coming from admin panel
        print(date_string)
        try:
            date_time = datetime.strptime(date_string, '%m/%d/%Y %I:%M %p')
        except:
            try:
                date_time = datetime.strptime(date_string, '%d-%m-%Y %I:%M %p')
            except:
                try:
                    date_time = datetime.strptime(date_string, '%d-%m-%Y %H:%M ')
                except Exception as e:
                    print(e)
        # Convert the datetime object to a string using the strftime method
        new_date_string = date_time.strftime('%Y-%m-%d %H:%M:%S')

        return new_date_string

    class AdminPanel(QtWidgets.QDialog): # This class defined with methods that are being used to execute operations which an admin can do
        def __init__(self):
            super().__init__()
            self.admin_panel = uic.loadUi('admin_panel.ui', self)
            self.audit_trail_rows = cusror.execute("SELECT * from action_record")
            self.audit_trail_data = self.audit_trail_rows.fetchall()
            self.password = self.findChild(QtWidgets.QLineEdit, "lineAdminPanel_OneTimePassword")
            self.username = self.findChild(QtWidgets.QLineEdit, "lineAdminPanel_NewUser")
            self.user_group = self.findChild(QtWidgets.QComboBox, "comboAdminPanel_UserGroup")
            self.users = self.findChild(QtWidgets.QComboBox, "userlist")
            self.admin_panel.buttonAdminPanel_AddUser.clicked.connect(self.insertuser)
            self.admin_panel.buttonAdminPanel_RemoveUser.clicked.connect(self.remove_user)
            self.admin_panel.buttonAdminPanel_ResetUserPassword.clicked.connect(self.changepassword)
            self.admin_panel.buttonAdminPanel_ExportLoginList.clicked.connect(self.export_login_record)
            self.admin_panel.buttonAdminPanel_ExportUserList.clicked.connect(self.export_user_record)
            self.admin_panel.buttonPasswordReset_Cancel.clicked.connect(self.close)
            self.admin_panel.buttonAdminPanel_ActivateUser.clicked.connect(self.active_or_deactivateuser)
            self.admin_panel.buttonAdminPanel_PrintUserList.clicked.connect(self.print_userrecord)
            self.admin_panel.buttonAdminPanel_PrintLoginList_3.clicked.connect(self.print_login_record)
            self.loginreport_start_date = self.findChild(QtWidgets.QDateTimeEdit,"dateTimeAdminPanel_LoginsFrom")
            self.login_report_end_date = self.findChild(QtWidgets.QDateTimeEdit,"dateTimeAdminPanel_LoginsTill")
            self.cursor = cusror
            self.msg = self.findChild(QtWidgets.QLabel, "messege")
            self.msg.setStyleSheet("color: rgb(200, 50, 50);font: bold;font-size:15px;")
            self.user =''
            self.showLoginRecords()
            self.showUsers()
            self.update_userlist()

        def update_userlist(self):
            self.cursor.execute("SELECT * FROM auth_user WHERE USERGROUP != 'secretadmin' ORDER BY USERNAME")
            users = cusror.fetchall()
            usernames = [i[1] for i in users]
            self.users.clear()
            self.users.addItems(usernames)

        def e_sign(self,html, outputfilename):
            pdfkit.from_string(html, 'tmp.pdf', configuration=config)
            getdsc=[]
            for dll in dllpath:
                try:

                    dsc = FetchDSC(dll)
                    if len(dsc) >0:
                        getdsc= dsc
                        dscdll = dll
                except:
                    pass
            if getdsc !=[]:

                if len(getdsc.certificate()) > 0:
                    pin, done1 = QtWidgets.QInputDialog.getText(
                        self, 'E-Sign Document', 'Enter pin:')
                    sign_pdf("tmp.pdf", outputfilename, pin,dscdll)
                    self.msg.setText("Login records successfully exported ( E - S   igned) !")
            else:
                if outputfilename[-3:-1].lower() !='pdf':
                    outputfilename +=".pdf"

                writewithname(self.user, 'tmp.pdf',outputfilename)

                self.msg.setText("Login records successfully exported (Un - Signed) !")
        def showUsers(self): # Show user table in admin panel
            self.tableWidget = self.findChild(QtWidgets.QTableWidget, "tableAdminPanel_UserList")
            self.cursor.execute("SELECT * FROM auth_user WHERE USERGROUP != 'secretadmin' ORDER BY USERNAME")
            users = cusror.fetchall()
            self.tableWidget.setRowCount(len(users))
            self.tableWidget.setColumnCount(6)

            for id, item in enumerate(users):
                self.tableWidget.setItem(id, 0, QtWidgets.QTableWidgetItem(item[1]))
                self.tableWidget.setItem(id, 1, QtWidgets.QTableWidgetItem(item[3]))
                self.tableWidget.setItem(id, 2, QtWidgets.QTableWidgetItem(item[5][0:10]))
                self.tableWidget.setItem(id, 3, QtWidgets.QTableWidgetItem("Yes" if item[4] == 1 else "No"))
                self.tableWidget.setItem(id, 4, QtWidgets.QTableWidgetItem(""))
                self.tableWidget.setItem(id, 5, QtWidgets.QTableWidgetItem(""))

        def showLoginRecords(self): # Show login record table in admin panel
            self.tableWidget = self.findChild(QtWidgets.QTableWidget, "tableAdminPanel_LoginList")
            self.cursor.execute("SELECT * FROM login_record")
            login_records = cusror.fetchall()
            self.tableWidget.setRowCount(len(login_records))
            self.tableWidget.setColumnCount(7)

            for id, item in enumerate(login_records):
                self.tableWidget.setItem(id, 0, QtWidgets.QTableWidgetItem(item[1]))
                self.tableWidget.setItem(id, 1, QtWidgets.QTableWidgetItem(item[6][11:19]))
                self.tableWidget.setItem(id, 2, QtWidgets.QTableWidgetItem(item[6][0:10]))
                self.tableWidget.setItem(id, 3, QtWidgets.QTableWidgetItem(item[2]))
                self.tableWidget.setItem(id, 4, QtWidgets.QTableWidgetItem(item[3]))
                self.tableWidget.setItem(id, 5, QtWidgets.QTableWidgetItem(""))
                self.tableWidget.setItem(id, 6, QtWidgets.QTableWidgetItem(""))

        def saveFileDialog(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                      "All Files (*);;Signed PDF (*.pdf)", options=options)
            if fileName:
                return fileName
            else:
                return ""

        def savedbdialog(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                      "All Files (*);;Sqlite3 db file (*.db)", options=options)
            if fileName:
                return fileName
            else:
                return ""


        def export_login_record(self):
            start_date =convertdate(self.loginreport_start_date.text())
            end_date  = convertdate(self.login_report_end_date.text())

            self.cursor.execute("SELECT * FROM login_record WHERE ATTEMPTED_AT BETWEEN ? AND ?", (start_date, end_date))
            login_records = cusror.fetchall()
            if len(login_records) >0:

                login_record_with_header = [("ID","USERNAME","STATUS","COMPUTERNAME", "EXTRA1","EXTRA2","ATTEMPT_AT")]+login_records
                data = pd.DataFrame(login_record_with_header)
                filename = self.saveFileDialog()
                if filename !="":
                    html=data.to_html()
                    self.e_sign(html,filename)
            else:
                self.msg.setText("No data Found !")

        def print_login_record(self):
            start_date = convertdate(self.loginreport_start_date.text())
            end_date = convertdate(self.login_report_end_date.text())
            self.cursor.execute("SELECT * FROM login_record WHERE ATTEMPTED_AT BETWEEN ? AND ?", (start_date, end_date))
            login_records = cusror.fetchall()
            if len(login_records) > 0:
                login_record_with_header = [("ID", "USERNAME", "STATUS", "COMPUTERNAME", "EXTRA1", "EXTRA2",
                                             "ATTEMPT_AT")] + login_records
                data = pd.DataFrame(login_record_with_header)
                data.to_csv("login_record.csv")
                os.startfile("login_record.csv", "print")
            else:
                self.msg.setText("No data Found !")

        def export_user_record(self):
            self.cursor.execute("SELECT * FROM auth_user")
            user_record = cusror.fetchall()
            user_record_with_header = [("ID","USERNAME","PASSWORD","USERGROUP", "ACTIVATED","CREATED_AT")]+user_record
            data = pd.DataFrame(user_record_with_header)
            filename = self.saveFileDialog()
            if filename !="" :
                html=data.to_html()
                self.e_sign(html,filename)

        def print_userrecord(self):
            self.cursor.execute("SELECT * FROM auth_user")
            login_records = cusror.fetchall()
            login_record_with_header = [("ID","USERNAME","STATUS","COMPUTERNAME", "EXTRA1","EXTRA2","ATTEMPT_AT")]+login_records
            data = pd.DataFrame(login_record_with_header)
            data.to_csv("users_record.csv")
            os.startfile("users_record.csv","print")

        def insertuser(self): # Creating new user by admin
            password = self.password.text()
            username = self.username.text().lower().strip()
            usergroup = self.user_group.currentText().lower()
            print(password, usergroup, username)
            try:
                password = md5(bytes(password, "utf-8")).hexdigest()
                self.cursor.execute("INSERT INTO auth_user(USERNAME, PASSWORD, USERGROUP, ACTIVATED)VALUES(?,?,?,?)",
                               (username, password, usergroup, True))
                database.commit()
                self.msg.setText("New User Added!")
                self.update_userlist()
                self.showUsers()
                return "inserted"
            except:
                self.msg.setText("There is a problem. Try later.")
                return "error "


        def changepassword(self): # Reset password of a user by admin
            username = username = self.users.currentText()
            password = "12345678"
            password = md5(bytes(password, "utf-8")).hexdigest()
            try:
                cusror.execute("UPDATE auth_user SET PASSWORD= ? WHERE USERNAME= ? ", (password, username))
                cusror.execute(f"UPDATE login_count SET COUNT = '5' WHERE USERNAME = '{username}'")
                database.commit()
                self.msg.setText(f"Password has been reset for user : {username}")
            except Exception as e:
                print(e)

        def active_or_deactivateuser(self): # Active or Deactive a user
            username = self.users.currentText()
            row = cusror.execute("SELECT * FROM auth_user WHERE USERNAME= ? ", (username,))
            data = row.fetchall()
            if data[0][3] != "admin":
                if data[0][4] == 1:
                    try:
                        cusror.execute("UPDATE auth_user SET ACTIVATED= 0 WHERE USERNAME= ? ", (username,))
                        self.msg.setText(f"Deactivated user : {username}")
                        self.showUsers()
                    except:
                        pass
                else:
                    try:
                        cusror.execute("UPDATE auth_user SET ACTIVATED= 1 WHERE USERNAME= ? ", (username,))
                        self.msg.setText(f"Activated user : {username}")
                        self.showUsers()
                    except:
                        pass
                database.commit()
            else:
                self.msg.setText("Admin can not be deactivated.")

        def remove_user(self): # Delete a user
            username = self.users.currentText()

            row = cusror.execute("SELECT * FROM auth_user WHERE USERNAME= ? ", (username,))
            data = row.fetchall()
            if data[0][3] != "admin":
                try:
                    cusror.execute("DELETE FROM auth_user WHERE username= ?", (username,))
                    database.commit()
                    self.update_userlist()
                    self.showUsers()
                    self.msg.setText(f"User : {username} has been removed!")
                except Exception as e:
                    print(e)
            else:
                self.msg.setText("Admin can not be removed!")

    class ForgetPassword(QtWidgets.QDialog): # This class handles all the operation in forget password window
        def __init__(self):
            super().__init__()
            self.forgot_password = uic.loadUi('forgot_password.ui', self)
            self.login_id = self.findChild(QtWidgets.QLineEdit, "linePasswordReset_LoginID")
            self.password = self.findChild(QtWidgets.QLineEdit, "linePasswordReset_OldPassword")
            self.new_password = self.findChild(QtWidgets.QLineEdit, "linePasswordReset_NewPassword")
            self.re_new_password = self.findChild(QtWidgets.QLineEdit, "linePasswordReset_NewPasswordConfirm")
            self.messege = self.findChild(QtWidgets.QLabel, "messege")
            self.messege.setStyleSheet("color: rgb(200, 50, 50);font: bold;")

            self.forgot_password.buttonPasswordReset_ChangePassword.clicked.connect(self.changePassword)
            self.forgot_password.buttonPasswordReset_AskAdmin.clicked.connect(self.password_messege)
            self.forgot_password.buttonPasswordReset_Cancel.clicked.connect(self.login)

        def changePassword(self): # Change password by a user
            if self.login_id.text() == "" or self.password.text() == "" or self.new_password.text() == "" or self.re_new_password.text() == "":
                self.messege.setText("Please fill all the fields!")
            else:
                cusror.execute(
                    f"SELECT * FROM auth_user WHERE USERNAME = '{self.login_id.text()}' AND PASSWORD = '{md5(bytes(self.password.text(), 'utf-8')).hexdigest()}'")
                user = cusror.fetchall()
                if user:
                    if len(self.new_password.text()) >= 7:
                        if self.new_password.text() == self.re_new_password.text():
                            cusror.execute("INSERT INTO login_record (USERNAME, STATUS, COMPUTERNAME) VALUES(?,?,?)",
                                           (self.login_id.text(), 'Changed Password', platform.node()))
                            cusror.execute(
                                f"UPDATE auth_user SET PASSWORD = '{md5(bytes(self.re_new_password.text(), 'utf-8')).hexdigest()}' WHERE USERNAME = '{self.login_id.text()}' AND PASSWORD = '{md5(bytes(self.password.text(), 'utf-8')).hexdigest()}'")
                            database.commit()
                            self.messege.setText("Password has been changed!")
                        else:
                            self.messege.setText("Confirm password is not matched!")
                    else:
                        self.messege.setText("Password should have minimum 7 characters!")
                else:
                    self.messege.setText("User not found!")

        def password_messege(self): # Send a message to admin to reset password
            if self.login_id.text() == "":
                self.messege.setText("Please enter your login ID")
            else:
                cusror.execute(
                    f"INSERT INTO requests (USERNAME, REQUESTTYPE) VALUES ('{self.login_id.text()}', 'RESET PASSWORD')")
                database.commit()
                self.close()
                self.w = PasswordMessege()
                self.w.show()

        def login(self):
            self.close()
            self.w = Login()
            self.w.show()

    class PasswordMessege(QtWidgets.QDialog): # This class is to show password message window
        def __init__(self):
            super().__init__()
            self.password_messege = uic.loadUi('password_messege.ui', self)
            self.password_messege.buttonLoginPanelMessage_Exit.clicked.connect(self.close)

    class Login(QtWidgets.QDialog): # This class handles all the logins and keep records

        def __init__(self):
            super(Login, self).__init__()
            self.log = uic.loadUi('login.ui', self)
            self.username = self.findChild(QtWidgets.QLineEdit, "lineLoginPanel_LoginID")
            self.password = self.findChild(QtWidgets.QLineEdit, "lineLoginPanel_Password")
            self.fail = self.findChild(QtWidgets.QLabel, "wrong_password")
            self.fail.setStyleSheet("color: rgb(200, 50, 50);font: bold;")
            self.log.buttonLoginPanel_OK.clicked.connect(self.login)
            self.log.buttonLoginPanel_ForgotPassword.clicked.connect(self.changePassword)
            self.log.buttonLoginPanel_Cancel.clicked.connect(self.close)
            self.show()


        def login(self):  # Handles logins and login counts
            cusror.execute(f"SELECT * FROM login_count WHERE USERNAME = '{self.username.text()}'")
            user = cusror.fetchall()
            if not user:
                cusror.execute(f"INSERT INTO login_count (USERNAME, COUNT) VALUES ('{self.username.text()}', '5')")
                database.commit()

            if self.username.text() == "" or self.password.text() == "":
                self.fail.setText("Enter Login Id and Password!")
            else:
                cusror.execute(f"SELECT COUNT FROM login_count WHERE USERNAME = '{self.username.text()}'")
                count = cusror.fetchall()

                if count[0][0] > 0 or self.username.text() == "secretadmin":
                    password = md5(bytes(self.password.text(), "utf-8")).hexdigest()
                    cusror.execute(
                        f"SELECT * FROM auth_user WHERE USERNAME = '{self.username.text().lower().strip()}' AND PASSWORD = '{password}' AND ACTIVATED = '1'")
                    user = cusror.fetchall()
                    if user:
                        cusror.execute("INSERT INTO login_record (USERNAME, STATUS, COMPUTERNAME) VALUES(?,?,?)",
                                       (self.username.text(), 'Login Success', platform.node()))
                        cusror.execute(f"UPDATE login_count SET COUNT = '5' WHERE USERNAME = '{self.username.text()}'")
                        database.commit()
                        if user[0][3] == 'admin' or user[0][3] == 'secretadmin':
                            self.adminPanel(user[0][1])
                        else:
                            self.mainApp()
                    else:
                        cusror.execute(
                            f"UPDATE login_count SET COUNT = '{count[0][0] - 1}' WHERE USERNAME = '{self.username.text()}'")
                        cusror.execute("INSERT INTO login_record (USERNAME, STATUS, COMPUTERNAME) VALUES(?,?,?)",
                                       (self.username.text(), 'Incorrect Credential', platform.node()))
                        database.commit()
                        self.fail.setText(f"Incorrect Credential! Attempts left : {count[0][0] - 1}")
                else:
                    self.fail.setText("Attempts left : 0 Please ask admin to reset count!")

        def mainApp(self):
            self.close()
            runForm = MainAppWindow()
            runForm.showMaximized()
            runForm.show()

        def adminPanel(self,username):
            self.close()
            self.w = AdminPanel()
            self.w.user= username
            self.w.showMaximized()
            self.w.show()

        def changePassword(self):
            self.close()
            self.w = ForgetPassword()
            self.w.show()

# ================================ Login Code Ends  ======================================


# ================================ Main Program ======================================
class MainAppWindow(QMainWindow, Ui_MainWindow, HardwareControl, ThreadFunctions):

    # Initialisation()  # All generic initialisations are done here

    eventImage = Signal()
    eventStillImage = Signal()

    def __init__(self, *args, **kwargs):
        super(MainAppWindow, self).__init__(*args, **kwargs)

        #TODO: Sequence the startup. Which module starts first and so on, with error messages, splash.close and all.

        self.desktopLoc = shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, 0, 0)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        time.sleep(1)
        splash.close()

        self.ardu = HardwareControl()
        self.ArduinoPortInMainDOTpy = None

        for arduPort in self.ardu.ports:
            if "Arduino" in arduPort.description:  # Identify which port is Arduino and select it
                self.ArduinoPortInMainDOTpy = arduPort[0] # Using such a long name to distinguish from finding Arduinos in Hardware.py
                # print("Arduino: ", self.ArduinoPortInMainDOTpy)

        if self.ArduinoPortInMainDOTpy == None: # If there is no hardware connected then 'arduPort' will be 0
            print("No hardware")
            self.disableHardwareButtons()
            QMessageBox.warning(self, 'ERROR HW1!   Hardware Controller Not Found',
                                                          '\n'
                                                          '          It seems the hardware controller is not connected!                              \n\n'
                                                          '          1. Check if the USB cable of the controller is                              \n'
                                                          '             connected to a USB port of your PC.                                      \n\n'
                                                          '          2. Or if connected, unplug and replug the controller USB cable.            .\n\n'
                                                          '          3. Then close the application and restart it.                        \n\n', QMessageBox.Ok)
            #TODO: NOT IMPORTANT. Check if both camera and hardware are not present and close the application.

        self.rotationValue = 0
        self.hcam = None
        self.buf = None      # video buffer
        self.w = 0           # video width
        self.h = 0           # video height
        self.indexInitialResolution = 1 # Depends on camera
        self.histoData = [0]
        self.total = 0

        self.timerStarted = False
        self.timerCount = 10
        self.longTimerStarted = False

        # Preset Factory Settings here. These will get saved into config.ini in the first run of the program.
        # Then on, the values there can be changed using the Settings menu.
        self.defaultRotation = 0
        self.extendedResolution = 1.25
        self.reducedResolution = 0.5
        self.displayFlip = 0
        self.saveFlip = 0
        self.showTransBL = True
        self.showTransWL = True
        self.showEpiUVA = True
        self.showEpiUVB = True
        self.showTemperTab = True

        self.flagToSaveLongExpoImage = False
        self.clickDisposableImage = False               #


        self.initCamera()

        # self.canvas = pg.GraphicsLayoutWidget()
        # self.ui.layoutHistogram.addWidget(self.canvas)
        # self.plt1 = self.canvas.addPlot()

        # Depending on the camera connected prepare a blank image for showing the histogram
        # From the initcamera, we get resolution of camera for this image
        # img = np.zeros([self.resolutionTable[self.indexInitialResolution][0], self.resolutionTable[self.indexInitialResolution ][1], 3], dtype=np.uint8)
        # img.fill(255)  # or img[:] = 255
        # y, x = np.histogram(img, range=(0, 255), bins=255)
        # self.plt1.plot(x, y, stepMode=True, fillLevel=None, fillOutline=True, brush=(0, 0, 255, 150))

        self.saveFolder = None

        self.threadpool = QThreadPool()

        self.scene = GrafixScene()  # Create a scene. Note this has overloaded mouse events
        self.scene.setSceneRect(0, 0, self.w, self.h)  # Set its size to the image size (found above)
        self.someScene = self.ui.graphicsView.setScene(self.scene)  # Set it up in graphicsView widget of UI
        # self.vuPort = self.ui.graphicsView.setViewport(QGLWidget())

        self.ui.progressExposureTime.setMaximum(100)
        self.ui.progressExposureTime.setValue(0)

        ###=============================================================================================================
        ### DO THE CHANGES IN EXPOSURE HERE
        self.ui.buttonAutoExposure.clicked.connect(self.changeAutoExposure)

        ## If exposure to be changed as soon as slider released, use the code below
        self.ui.sliderExposureSec.sliderReleased.connect(self.changeExposure)
        self.ui.sliderExposureMilliSec.sliderReleased.connect(self.changeExposure)
        # self.ui.sliderExposureMicroSec.sliderReleased.connect(self.changeExposure)
        # self.ui.spinExposureMicroSec.valueChanged.connect(self.changeExposure)
        self.ui.spinExposureMilliSec.valueChanged.connect(self.changeExposure)
        self.ui.spinExposureSec.valueChanged.connect(self.changeExposure)
        ###=============================================================================================================

        ###=============================================================================================================
        ## CHEMI and LIVE IMAGE RADIO BUTTONS
        self.ui.radioVideoMode.setChecked(True)
        self.selectVideoOrChemiMode()
        self.ui.radioChemiMode.toggled.connect(self.selectVideoOrChemiMode)
        self.ui.radioVideoMode.toggled.connect(self.selectVideoOrChemiMode)
        ###=============================================================================================================

        self.ui.buttonSave.clicked.connect(self.clickImage)
        self.ui.buttonSaveChemi.clicked.connect(self.clickChemiImage)

        self.ui.spinRotation.valueChanged.connect(self.changeRotation)

        self.ui.buttonMains.clicked.connect(self.relayMains)
        self.ui.buttonEpiWhite.clicked.connect(self.relayEWL)
        self.ui.buttonTransUV.clicked.connect(self.relayTUV)
        self.ui.buttonTransWhite.clicked.connect(self.relayTWL)
        self.ui.buttonTransBlue.clicked.connect(self.relayTBL)
        self.ui.buttonEpiUVA.clicked.connect(self.relayUVA)
        self.ui.buttonEpiUVB.clicked.connect(self.relayUVB)

        self.ui.buttonFocusL3.clicked.connect(self.hbridgeFocusFar3)
        self.ui.buttonFocusL2.clicked.connect(self.hbridgeFocusFar2)
        self.ui.buttonFocusL1.clicked.connect(self.hbridgeFocusFar1)
        self.ui.buttonFocusR3.clicked.connect(self.hbridgeFocusNear3)
        self.ui.buttonFocusR2.clicked.connect(self.hbridgeFocusNear2)
        self.ui.buttonFocusR1.clicked.connect(self.hbridgeFocusNear1)

        self.ui.buttonIrisL3.clicked.connect(self.hbridgeIrisOpen3)
        self.ui.buttonIrisL2.clicked.connect(self.hbridgeIrisOpen2)
        self.ui.buttonIrisL1.clicked.connect(self.hbridgeIrisOpen1)
        self.ui.buttonIrisR3.clicked.connect(self.hbridgeIrisClose3)
        self.ui.buttonIrisR2.clicked.connect(self.hbridgeIrisClose2)
        self.ui.buttonIrisR1.clicked.connect(self.hbridgeIrisClose1)

        self.ui.buttonZoomL3.clicked.connect(self.hbridgeZoomIn3)
        self.ui.buttonZoomL2.clicked.connect(self.hbridgeZoomIn2)
        self.ui.buttonZoomL1.clicked.connect(self.hbridgeZoomIn1)
        self.ui.buttonZoomR3.clicked.connect(self.hbridgeZoomOut3)
        self.ui.buttonZoomR2.clicked.connect(self.hbridgeZoomOut2)
        self.ui.buttonZoomR1.clicked.connect(self.hbridgeZoomOut1)

        self.ui.buttonSpareL3.clicked.connect(self.hbridgeSpareL3)
        self.ui.buttonSpareL2.clicked.connect(self.hbridgeSpareL2)
        self.ui.buttonSpareL1.clicked.connect(self.hbridgeSpareL1)
        self.ui.buttonSpareR3.clicked.connect(self.hbridgeSpareR3)
        self.ui.buttonSpareR2.clicked.connect(self.hbridgeSpareR2)
        self.ui.buttonSpareR1.clicked.connect(self.hbridgeSpareR1)

        self.ui.buttonFilterL3.clicked.connect(self.hbridgeFilterL3)
        self.ui.buttonFilterL2.clicked.connect(self.hbridgeFilterL2)
        self.ui.buttonFilterL1.clicked.connect(self.hbridgeFilterL1)
        self.ui.buttonFilterR3.clicked.connect(self.hbridgeFilterR3)
        self.ui.buttonFilterR2.clicked.connect(self.hbridgeFilterR2)
        self.ui.buttonFilterR1.clicked.connect(self.hbridgeFilterR1)

        self.ui.comboFrequency.currentIndexChanged.connect(self.changeFrequency)

        self.ui.buttonFitWindow.clicked.connect(self.fitinWindow)

        self.ui.sliderDisplayZoom.sliderReleased.connect(self.zoomChange)

        self.ui.pushSavedFolder.clicked.connect(self.chooseSavedFolder)

        self.ui.pushAddPrefix.clicked.connect(self.addPrefix)

        self.ui.comboResolution.currentIndexChanged.connect(self.changeResolution)

        self.ui.buttonSaveProtocol.clicked.connect(self.saveProtocol)
        self.ui.buttonLoadProtocol.clicked.connect(self.loadProtocol)

        self.config = configparser.ConfigParser()
        self.applicationConfig = configparser.ConfigParser()

        self.factoryConfig = configparser.ConfigParser()
        self.readFactorySettings() # Read configuration settings at start-up

        self.ui.actionProgram_Settings.triggered.connect(self.setupFactorySettings)
        self.ui.buttonLoadPreviousSettings.clicked.connect(self.loadApplicationSettings)

        # UV Timer Signals
        self.ui.buttonStartStainFree.clicked.connect(self.startUVTimer)
        self.ui.buttonAbortStainFree.clicked.connect(self.abortUVTimer)
        # self.ui.sliderStainFree.sliderReleased.connect(self.setTimerValue)
        self.ui.spinStainFree.valueChanged.connect(self.setTimerValue)
        self.ui.sliderStainFree.valueChanged.connect(self.setTimerValue)

        self.ui.buttonFanOnOff.clicked.connect(self.fanOnOff)
        self.ui.buttonCoolingOnOff.clicked.connect(self.coolingOnOff)
        self.ui.sliderCooling.valueChanged.connect(self.coolingTemperatureChanged)
        self.ui.spinCooling.valueChanged.connect(self.coolingTemperatureChangedSpin)

    def fanOnOff(self):
        if self.hcam is not None:
            if self.ui.buttonFanOnOff.isChecked():
                self.hcam.put_Option(nncam.NNCAM_OPTION_FAN, 3)
                self.ui.buttonFanOnOff.setText("Cooling Fan ON")
            else:
                self.hcam.put_Option(nncam.NNCAM_OPTION_FAN, 0)
                self.ui.buttonFanOnOff.setText("Cooling Fan OFF")

    def calculateTemperatureTEC(self):
        if self.hcam is not None:
            if self.cameraIsCooled:
                self.TEC_Temperature = 0
                # print("TestTempppp:", self.hcam.get_Temperature(self.TEC_Temperature))
                actualTemperature = self.hcam.get_Temperature(self.TEC_Temperature)
                # print("Actual Temperature:", actualTemperature)
                if actualTemperature > 1000:
                    actualTemperature = actualTemperature - 65535
                self.ui.labelTemperature.setText(str(actualTemperature/10))
            else:
                self.ui.toolTemperature.setVisible(False)

    def coolingOnOff(self):
        if self.hcam is not None:
            # self.TEC_Temperature = bytes(0)
            # print("TestTemp:", self.hcam.get_Temperature(self.TEC_Temperature))

            if self.ui.buttonCoolingOnOff.isChecked():
                self.coolingTemperatureChanged()
                self.hcam.put_Option(nncam.NNCAM_OPTION_TEC, 1)
                self.hcam.put_Option(nncam.NNCAM_OPTION_FAN, 3)
                self.ui.buttonCoolingOnOff.setText("Cooling ON")
                self.ui.buttonFanOnOff.setChecked(True)
                self.ui.buttonFanOnOff.setText("Cooling Fan ON")
            else:
                self.ui.buttonCoolingOnOff.setText("Cooling OFF")
                # self.hcam.put_Option(nncam.NNCAM_OPTION_FAN, 0)
                self.hcam.put_Option(nncam.NNCAM_OPTION_TEC, 0)

    def coolingTemperatureChanged(self):
        if self.hcam:
            self.TECTargetTemperature = int(self.ui.sliderCooling.value() * 10)
            if self.TECTargetTemperature < -300:
                self.TECTargetTemperature = -300
            if self.TECTargetTemperature > 300:
                self.TECTargetTemperature = 300
            self.hcam.put_Option(nncam.NNCAM_OPTION_TECTARGET, self.TECTargetTemperature)
            # print("Temp:", self.TECTargetTemperature)

    def coolingTemperatureChangedSpin(self):
        if self.hcam:
            self.TECTargetTemperature = int(self.ui.spinCooling.value() * 10)
            if self.TECTargetTemperature < -300:
                self.TECTargetTemperature = -300
            if self.TECTargetTemperature > 300:
                self.TECTargetTemperature = 300
            self.hcam.put_Option(nncam.NNCAM_OPTION_TECTARGET, self.TECTargetTemperature)
            # print("TECTargetTemperature:", self.TECTargetTemperature)

    def disableHardwareButtons(self):

        self.ui.buttonFocusL3.setEnabled(False)
        self.ui.buttonFocusL2.setEnabled(False)
        self.ui.buttonFocusL1.setEnabled(False)
        self.ui.buttonFocusR1.setEnabled(False)
        self.ui.buttonFocusR2.setEnabled(False)
        self.ui.buttonFocusR3.setEnabled(False)
        # self.ui.sliderFocus.setEnabled(False)
        # self.ui.spinFocus.setEnabled(False)

        self.ui.buttonZoomL3.setEnabled(False)
        self.ui.buttonZoomL2.setEnabled(False)
        self.ui.buttonZoomL1.setEnabled(False)
        self.ui.buttonZoomR1.setEnabled(False)
        self.ui.buttonZoomR2.setEnabled(False)
        self.ui.buttonZoomR3.setEnabled(False)
        # self.ui.sliderZoom.setEnabled(False)
        # self.ui.spinZoom.setEnabled(False)

        self.ui.buttonIrisL3.setEnabled(False)
        self.ui.buttonIrisL2.setEnabled(False)
        self.ui.buttonIrisL1.setEnabled(False)
        self.ui.buttonIrisR1.setEnabled(False)
        self.ui.buttonIrisR2.setEnabled(False)
        self.ui.buttonIrisR3.setEnabled(False)
        # self.ui.sliderIris.setEnabled(False)
        # self.ui.spinIris.setEnabled(False)

        self.ui.buttonFilterL3.setEnabled(False)
        self.ui.buttonFilterL2.setEnabled(False)
        self.ui.buttonFilterL1.setEnabled(False)
        self.ui.buttonFilterR1.setEnabled(False)
        self.ui.buttonFilterR2.setEnabled(False)
        self.ui.buttonFilterR3.setEnabled(False)
        # self.ui.sliderFilter.setEnabled(False)
        # self.ui.spinFilter.setEnabled(False)

        self.ui.buttonSpareL3.setEnabled(False)
        self.ui.buttonSpareL2.setEnabled(False)
        self.ui.buttonSpareL1.setEnabled(False)
        self.ui.buttonSpareR1.setEnabled(False)
        self.ui.buttonSpareR2.setEnabled(False)
        self.ui.buttonSpareR3.setEnabled(False)
        # self.ui.sliderSpare.setEnabled(False)
        # self.ui.spinSpare.setEnabled(False)

        self.ui.buttonMains.setEnabled(False)
        self.ui.buttonEpiWhite.setEnabled(False)
        self.ui.buttonTransUV.setEnabled(False)
        self.ui.buttonTransWhite.setEnabled(False)
        self.ui.buttonTransBlue.setEnabled(False)
        self.ui.buttonEpiUVA.setEnabled(False)
        self.ui.buttonEpiUVB.setEnabled(False)
        self.ui.sliderStainFree.setEnabled(False)
        self.ui.spinStainFree.setEnabled(False)
        self.ui.buttonStartStainFree.setEnabled(False)
        self.ui.buttonAbortStainFree.setEnabled(False)

        self.ui.buttonSaveProtocol.setEnabled(False)
        self.ui.buttonLoadProtocol.setEnabled(False)

    def disableCameraButtons(self):

        self.ui.buttonSave.setEnabled(False)
        self.ui.buttonFitWindow.setEnabled(False)
        self.ui.buttonLoadPreviousSettings.setEnabled(False)

        self.ui.buttonAutoExposure.setEnabled(False)
        # self.ui.sliderExposureMicroSec.setEnabled(False)
        self.ui.sliderExposureMilliSec.setEnabled(False)
        self.ui.sliderExposureSec.setEnabled(False)
        self.ui.spinLongExposureMilliSec.setEnabled(False)
        self.ui.spinLongExposureSec.setEnabled(False)
        self.ui.spinLongExposureMin.setEnabled(False)

        self.ui.comboResolution.setEnabled(False)
        self.ui.comboFormat.setEnabled(False)
        self.ui.comboFnamePrefix.setEnabled(False)
        self.ui.lineAddPrefix.setEnabled(False)
        self.ui.pushAddPrefix.setEnabled(False)
        self.ui.comboFnameSuffix.setEnabled(False)

        self.ui.spinRotation.setEnabled(False)
        self.ui.comboFrequency.setEnabled(False)
        self.ui.sliderDisplayZoom.setEnabled(False)
        self.ui.sliderCooling.setEnabled(False)
        self.ui.spinCooling.setEnabled(False)

        self.ui.buttonSaveProtocol.setEnabled(False)
        self.ui.buttonLoadProtocol.setEnabled(False)


    def initCamera(self):
        # API: Enumerate out cameras connected to PC
        a = nncam.Nncam.EnumV2()

        splash.close()

        if len(a) <= 0 or a == None: # If there are no cameras then 'a' will be 0
            QMessageBox.warning(self, 'ERROR CAM1!   Camera Not Found',
                                      '\n'
                                      '          It seems a working camera is not connected!                             \n\n'
                                      '          1. Check if the USB cable of the camera is                              \n'
                                      '             connected to a USB port of your PC.                                  \n\n'
                                      '          2. Or if connected, unplug and replug the camera USB cable.            .\n\n'
                                      '          3. Then close the application and restart it.                    \n\n', QMessageBox.Ok)
            self.ui.statusbar.showMessage("No Camera Found")
            self.disableCameraButtons()

        else: # A camera is found connected
            self.camname = a[0].displayname
            self.camModel = str(self.camname)
            # self.setWindowTitle(self.camname)
            # print("Preview:", a[0].model.preview)
            # print("Still:", a[0].model.still)
            # print("Autofocus:", a[0].model.maxfanspeed)


            # API: Video image data arrives.
            # Use Nncam_PullImage(V2) to 'pull' the image data
            self.eventImage.connect(self.eventImageSignal)

            # API: Still image data arrives.
            # Use Nncam_PullStillImage(V2) to 'pull' the image data
            self.eventStillImage.connect(self.eventStillImageSignal)

            try:

                self.hcam = nncam.Nncam.Open(a[0].id)                       # Open the first available camera


                # In RAW mode, flip and rotate don't work.
                # self.hcam.put_Option(nncam.Nncam_OPTION_UPSIDE_DOWN, 0)
                self.hcam.put_HFlip(0)
                self.hcam.put_VFlip(0)

                #-----------------------------------------------------------
                # Image Chroma | Option Bitdepth | Option RAW | Option RGB |
                #--------------|-----------------|------------|------------|
                #   Colour 8   |        0        |      0     |      0     |
                #   Mono 8     |        0        |      1     |      3     |
                #   Mono 16    |        1        |      1     |      4     |
                #-----------------------------------------------------------
                #-------------------|--------------|------------|-------------|-------------|
                # Image Chroma      | Colour 8-bit | Mono 8-bit | Mono 16-bit | Mono 8 RGB
                #                   |              |            | *Use This*  |
                #-------------------|--------------|------------|-------------|-------------|
                #  Option Bitdepth  |       0      |      0     |      1      |     0
                #  Option RAW 8     |       0      |      1     |      1      |     0
                #  Option RGB       |       0      |      3     |      4      |     3
                #-------------------|--------------|------------|-------------|-------------|

                self.hcam.put_Option(nncam.NNCAM_OPTION_BITDEPTH, 1)        # 0 use 8-bits, 1 use max bits
                self.hcam.put_Option(nncam.NNCAM_OPTION_RAW, 1)             # 0 RGB mode, 1 RAW mode
                self.hcam.put_Option(nncam.NNCAM_OPTION_RGB, 4)             # 0 = RGB24 (basically 8-bits
                                                                            # 1 = enable RGB48 format when bitdepth > 8
                                                                            # 2 = RGB32
                                                                            # 3 = 8 bits gray (only for mono)
                                                                            # 4 = 16 bits gray (only for mono and bitdepth > 8)
                self.hcam.put_HZ(1)  # 50Hz, so that flicker is avoided


            except nncam.HRESULTException:
                QMessageBox.warning(self, 'ERROR CAM2!   Camera Not Found',
                                    '\n'
                                    '          It seems a working camera is not connected!                             \n\n'
                                    '          1. Check if the USB cable of the camera is                              \n'
                                    '             connected to a USB port of your PC.                                  \n\n'
                                    '          2. Or if connected, unplug and replug the camera USB cable.            .\n\n'
                                    '          3. Then please close the application and restart it.                    \n\n',
                                    QMessageBox.Ok)
                self.ui.statusbar.showMessage("No Camera Found")
                self.disableCameraButtons()

            else:
                self.isMonochrome = self.hcam.get_Chrome()                  # Check if camera is monochrome
                # print("Mono1?", self.isMonochrome)
                #
                # self.isMono = nncam.Nncam.get_Chrome(self.hcam)                  # Check if camera is monochrome
                # print("Mono2?", self.isMono)

                print("Frame rate:", self.hcam.get_FrameRate())
                print("ROI:", self.hcam.get_Roi())

                # self.hcam.put_Option(nncam.NNCAM_OPTION_TECTARGET, -200)
                # print(self.hcam.get_Option(nncam.NNCAM_OPTION_TECTARGET))

                # Parameters:
                #           HNncam h: camera instance handle
                #           short nTemperature: in 0.1℃ (32 means 3.2℃, -35 means -3.5℃)
                # nTemp = ctypes.c_ushort()
                # Temperature =  nncam.Nncam.get_Temperature(self.hcam, ctypes.byref(nTemp))
                # print("Temperature:", Temperature)
                # result = lib.Toupcam_get_Temperature(self.cam, ctypes.byref(nTemp))

                self.cameraIsCooled = 0 # Initialise to camera is not cooled
                if a[0].model.maxfanspeed != 0:
                    self.cameraIsCooled = 1 # Camera has a TEC cooler
                    self.hcam.put_Option(nncam.NNCAM_OPTION_FAN, 0)
                    # self.hcam.put_Option(nncam.NNCAM_OPTION_TEC, 0)

                self.maxBits = nncam.Nncam.MaxBitDepth(self.hcam)           # Find out the maximum bit depth possible
                # Usually 12-bit image data means a pixel is 4095 when it is at the brightest
                # But in a 16-bit image display system the brightest pixel will be 65535.
                # So the brightest pixel in 12-bit image data will seem very dark in a 16-bit display system since its intensity is just 4096/65536
                # So we need to scale up the image data from a 12-bit (or 10-bit) system to 16-bit by simply multiplying...
                # ...by 65536/4095 (65536/1024 for 10bit)
                # We need to scale up the bits of pixels to show the pic correctly in 16-bit format.
                self.scaleFactor = int((2**16)/(2**self.maxBits))

                # self.rawFormat = nncam.Nncam.get_RawFormat(self.hcam)
                # print("Rawformat:", self.rawFormat)

                self.getExpoTimeRange()
                self.getResolution() # This fills up the Resolution combobox
                # self.hcam.put_eSize(self.indexInitialResolution) # This shows the live image with user defined resolution
                # self.w, self.h = self.hcam.get_Size()

                self.changeResolution()

                self.w = self.resolutionTable[self.indexResolution][0]
                self.h = self.resolutionTable[self.indexResolution][1]

                self.changeRotation()

                self.zoomFactor = self.ui.sliderDisplayZoom.value() / 100


                # self.bufsize = ((self.w * 24 + 31) // 32 * 4) * self.h
                # self.buf = bytes(self.bufsize) # Creates a Byte object of bufsize (Byte object is sequence of Bytes)
                # self.pic = bytes(self.bufsize) # Creates a Byte object of bufsize (to save image)
                self.ui.buttonAutoExposure.setChecked(self.hcam.get_AutoExpoEnable())

                try:
                    # if sys.platform == 'win32':
                    #     self.hcam.put_Option(nncam.Nncam_OPTION_BYTEORDER, 0) # QImage.Format_RGB888
                    self.hcam.StartPullModeWithCallback(self.cameraCallback, self)
                except nncam.HRESULTException:
                    QMessageBox.warning(self, 'ERROR CAM3!   Camera Not Found',
                                        '\n'
                                        '          It seems a working camera is not connected!                             \n\n'
                                        '          1. Check if the USB cable of the camera is                              \n'
                                        '             connected to a USB port of your PC.                                  \n\n'
                                        '          2. Or if connected, unplug and replug the camera USB cable.            .\n\n'
                                        '          3. Then please close the application and restart it.                    \n\n',
                                        QMessageBox.Ok)
                    self.ui.statusbar.showMessage("No Camera Found")
                    self.disableCameraButtons()
                # the vast majority of callbacks come from nncam.dll/so/dylib internal threads, so we use qt signal to post this event to the UI thread
                splash.close()

    @staticmethod
    def cameraCallback(nEvent, ctx):
        if nEvent == nncam.NNCAM_EVENT_IMAGE:
            # print("Start of Live Image Callback:", time.perf_counter())
            ctx.eventImage.emit()
        if nEvent == nncam.NNCAM_EVENT_STILLIMAGE:
            # print("Start of Still Image Callback:", time.perf_counter())
            ctx.eventStillImage.emit()

#-----------------------------------------------------------------------------------------------------------------------
# run in the UI thread
    @Slot()
    def eventImageSignal(self): # This sends a video signal (LIVE IMAGE)

        entries = []
        self.videoFromRawBuffer12bit = None

        # self.TEC_Temperature = bytes(0)
        # print("TestTemp:", self.hcam.get_Temperature(self.TEC_Temperature))
        # self.hcam.put_Option(nncam.NNCAM_OPTION_TEC, 1)
        # self.hcam.put_Option(nncam.NNCAM_OPTION_FAN, 3)

        # liveImageStartTime = time.process_time()
        # liveImageStartTime = time.perf_counter()
        # print("Start of Live Image Slot:", liveImageStartTime)
        if self.hcam is not None:
            try:
                # FOR 8 or 16 bit GRAYSCALE IMAGES
                # Data from camera is in the form of a 1D array.
                # So self.buf is a 1D array with all pixel data.
                self.hcam.PullImageV2(self.buf, 16, None)

                if self.ui.radioChemiMode.isChecked() & self.flagToSaveLongExpoImage is True:
                    wd = self.resolutionTable[0][0]
                    ht = self.resolutionTable[0][1]
                    self.saveBufferToImage(self.buf, wd, ht)

                videoFromRawBuffer = np.frombuffer(self.buf, dtype="uint16") # Create of numpy array of 16-bit data
                self.videoFromRawBuffer12bit = videoFromRawBuffer

                # To convert a 12-bit image to 16-bit, we need to scale the RAW bits from 12 to 16 (i.e. * 2**4)
                videoFromRawBuffer = videoFromRawBuffer * self.scaleFactor
                # print("Size before:", videoFromRawBuffer.shape) # This is still a 1D array. Uncomment to check.

                # Array (buffer) is now given the shape of the camera resolution (2D array)
                if self.rotationLandscape: # Earlier a sub-routine has already checked this
                    videoFromRawBuffer = videoFromRawBuffer.reshape(self.imgHeight, self.imgWidth) # This in landscape mode
                    # print("Size after Landscape:", videoFromRawBuffer.shape) # Uncomment to see 2D array size.
                else:
                    videoFromRawBuffer = videoFromRawBuffer.reshape(self.imgWidth, self.imgHeight) # This in portrait mode
                    # print("Size after Portrait:", videoFromRawBuffer.shape) # Uncomment to see 2D array size.

                if self.rotationValue == 0:
                    pass
                    # No Rotation
                    # videoFromRawBuffer = flip(videoFromRawBuffer, self.displayFlip)
                if self.rotationValue == 90:
                    # print("Size 90 before:", videoFromRawBuffer.shape)
                    videoFromRawBuffer = rotate(videoFromRawBuffer, ROTATE_90_CLOCKWISE)
                    # videoFromRawBuffer = flip(videoFromRawBuffer, self.displayFlip)
                    # print("Size 90 after:", videoFromRawBuffer.shape)
                if self.rotationValue == 180:
                    videoFromRawBuffer = rotate(videoFromRawBuffer, ROTATE_180)
                    # videoFromRawBuffer = flip(videoFromRawBuffer, self.displayFlip)
                if self.rotationValue == 270:
                    videoFromRawBuffer = rotate(videoFromRawBuffer, ROTATE_90_COUNTERCLOCKWISE)
                    # videoFromRawBuffer = flip(videoFromRawBuffer, self.displayFlip)

                displayFlipLUT = [0, 0, 1, -1]  # Gives flip value based on saved factory settings. See spinDisplayFlip in FactorySettings GUI
                                                # 1 = hori, 2 = vert, 3 = H+V. This parses to OpenCV 0, 1 and -1 correspondingly
                if self.displayFlip != 0:       # self.displayFlip = 0, means no flip (so skip flipping).
                    videoFromRawBuffer = flip(videoFromRawBuffer, displayFlipLUT[self.displayFlip])

                self.total += 1  # TODO: Maybe save total frames captured and show in diagnostic screen

            except nncam.HRESULTException:
                # QMessageBox.warning(self, '', 'Image acquisition failed!', QMessageBox.Ok)
                print("Image acquisition failed") # TODO: Happens when image rotated. So for rotation, stop image display just before rotation
            else:

                # In case of long exposures, we are using Trigger Mode. As per API, in trigger mode, the output is in
                # eventImageSignal not eventStillImageSignal (as in Snap Mode).
                # So save the image in case it is the output of a software triggered image


                # Liveimage for 16 bits and monochrome
                self.liveImage = QImage(videoFromRawBuffer, self.imgWidth, self.imgHeight, (self.imgWidth * 2), QImage.Format_Grayscale16)
                # Liveimage for RGB
                # self.liveImage = QImage(self.buf, self.imgWidth, self.imgHeight, (self.imgWidth * 2), QImage.Format_RGB888)

                # self.zoomChange()
                self.zoomFactor = self.ui.sliderDisplayZoom.value() / 100
                self.imageScaleH = self.imgHeight * self.zoomFactor
                self.imageScaleW = self.imgWidth * self.zoomFactor
                self.pixmap = QPixmap.fromImage(self.liveImage)  # Create pixmap from QImage item
                self.pixmap = self.pixmap.scaled(int(self.imageScaleW), int(self.imageScaleH), Qt.KeepAspectRatio)
                self.zoomRect = self.pixmap.rect()
                self.scene.clear()
                if self.justRotatedSoCenterDisplay:
                    self.ui.graphicsView.centerOn(self.zoomRect.center())
                    self.justRotatedSoCenterDisplay = False
                self.scene.setSceneRect(self.zoomRect)
                self.sceneItem = self.scene.addPixmap(QPixmap(self.pixmap))
                self.addGrid()
                self.expoTime = self.hcam.get_ExpoTime()
                # self.ui.labelExpoS.setText(str(self.expoTime / 1000000))
                self.displayExposure()


                if self.ui.cameraAdjustments.currentIndex() == 7:
                    # Construct Image for histogram
                    reduceRatio = 0.5
                    # ccc = resize(videoFromRawBuffer, (0,0), fx=reduceRatio, fy=reduceRatio)
                    # self.liveImage = ImagePIL.frombuffer(data=ccc, mode='RGB', size=(self.imgWidth*reduceRatio, self.imgHeight*reduceRatio)) #TODO: Change automatic resolution
                    # self.plt1.clear()
                    # self.updateHistogram() #TODO: Causing slow response in GUI. Maybe update every second not in realtime. Or reduce image bit-depth. Or size
                    # self.histogram_wrapper()  # Giving some error

                #BRIGHTNESS
                # self.brightness = nncam.Nncam.get_Brightness(self.hcam)
                # self.brightness = nncam.Nncam.get(self.hcam)
                # self.hcam.put_Brightness(50)
                # print("Parameter:", self.brightness)

                # liveImageElapsedTime = time.process_time() - liveImageStartTime
                # liveImageElapsedTime = time.perf_counter() - liveImageStartTime
                # print("Elapsed Live Image Time:", liveImageElapsedTime)

        self.calculateTemperatureTEC()

    def clickChemiImage(self):  # Click a long exposure
        if self.saveFolder is None or not os.path.exists(self.saveFolder):
            self.chooseSavedFolder()  # Asks
            # Lines below simply saves the image in a newly created GelCam folder on desktop
            # self.saveFolder = os.path.join(winshell.desktop(), 'GelCAM')
            # os.makedirs(self.saveFolder, exist_ok=True)
            # self.ui.textSavedFolder.setText(self.saveFolder)
        self.hcam.put_AutoExpoEnable(False)
        # Calculate the total exposure value first
        self.longExpoValue =  self.ui.spinLongExposureMin.value()  * 60 * 1000 * 1000 \
                              + self.ui.spinLongExposureSec.value()     * 1000 * 1000 \
                              + self.ui.spinLongExposureMilliSec.value()       * 1000  # \
        # print("Long Expo:", self.longExpoValue)
        self.longTimerCount = self.longExpoValue / 1000000
        if self.longTimerCount < 1:
            self.longTimerCount = 1
        self.hcam.put_ExpoTime(self.longExpoValue)
        self.hcam.put_Option(nncam.NNCAM_OPTION_TRIGGER, 1)
        nncam.Nncam.Trigger(self.hcam, 1)
        self.flagToSaveLongExpoImage = True
        self.startExpoTimer()

    def clickImage(self):  # Initiates the internal processing of camera to click an image

        self.hcam.put_Option(nncam.NNCAM_OPTION_TRIGGER, 0)
        self.hcam.put_Option(nncam.NNCAM_OPTION_TRIGGER, 0)

        if self.saveFolder is None or not os.path.exists(self.saveFolder):
            self.chooseSavedFolder()  # Asks
            # Lines below simply saves the image in a newly created GelCam folder on desktop
            # self.saveFolder = os.path.join(winshell.desktop(), 'GelCAM')
            # os.makedirs(self.saveFolder, exist_ok=True)

        ## Ensure exposure values are updated
        # self.changeExposure()

        ## Suppose a long expo LIVE image (say 70 sec) is updating, and after 20 sec, user clicks Save image, then
        ## the image that gets saved is roughly 50 sec (70 sec - 20 sec). To overcome this, when a long expo is clicked
        ## first click a very small expo image (say 1 millisec) and then click the long expo image immediately after.
        ## This way the update of the LIVE image begins along with the SAVE image process.

        # oldExposure = self.hcam.get_ExpoTime()          # Save the present exposure for use later in this subroutine
        # self.clickDisposableImage = False               #

        # # Iff Set Exposure is > 1 second, click a sacrificial image first which can then be disposed off
        # if oldExposure > 1000000:                       # Exposure > 1 sec
        #     self.clickDisposableImage = True            # Setup flag to indicate this image need not be saved
        #     self.hcam.put_ExpoTime(1000)                # Feeding a 1000uS exposure time
        #     nncam.Nncam.Snap(self.hcam, 0)              # Click image
        #     print("Sacrifical image clicked")           #
        #     time.sleep(0.1)
        #     self.clickDisposableImage = False           # Set the flag back to ensure that the new click gets saved

        ## It seems some cameras like I3CMOS05000KMB gives error with nncam.Nncam.Snap(self.hcam, 0)
        ## if self.camname == I3CMOS05000KMB:
        ##     nncam.Nncam.Snap(self.hcam, 1)
        ## else:

        # self.hcam.put_ExpoTime(oldExposure)             # Restore the old exposure for proper clicking
        nncam.Nncam.Snap(self.hcam, 0)

        # self.stillImageClickedTime = time.perf_counter()
        ## so using nncam.Nncam.Snap(self.hcam, 1)
        ## nncam.Nncam.Snap(self.hcam, self.indexResolution)

# -----------------------------------------------------------------------------------------------------------------------

# @Slot() # THIS IS FOR COLOUR IMAGES AND IS WORKING
# def eventStillImageSignal(self):
#
#     wd =  self.resolutionTable[self.indexResolution][0]
#     ht =  self.resolutionTable[self.indexResolution][1]
#     self.pic = bytes((wd * 24 + 31) // 32 * 4) * ht
#     self.hcam.PullStillImageV2(self.pic, 24, None)
#
#     if self.rotationValue == 90 or self.rotationValue == 270:
#         imag = ImagePIL.frombuffer(data=self.pic, mode='RGB', size=(ht, wd))
#     else:
#         imag = ImagePIL.frombuffer(data=self.pic, mode='RGB', size=(wd, ht))
#
#     zeroth_ifd = {
#         piexif.ImageIFD.Make: u"Sony CCD",
#         piexif.ImageIFD.Software: u"SpecialSoftware"
#     }
#
#     exif_ifd = {
#         # piexif.ExifIFD.DateTimeOriginal: u"2099:09:29 10:10:10",
#         piexif.ExifIFD.LensMake: u"Computar",
#         piexif.ExifIFD.Sharpness: 65535,
#         piexif.ExifIFD.LensModel: u"8-48mm, 6x",
#      }
#     exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd}
#     exif_bytes = piexif.dump(exif_dict)
#
#     fnameFormat = self.ui.comboFormat.currentText()
#     fnamePrefix = self.ui.comboFnamePrefix.currentText()
#     fnameSuffix = self.ui.comboFnameSuffix.currentText()
#
#     if fnamePrefix == "User Defined...":
#         saveName = QFileDialog.getSaveFileName(None, "Save Image", '', "Images (*.jpg *.tif *.png *.bmp)")
#         saveName = (os.path.splitext(saveName[0])) # Remove jpg extension
#         nextFile = saveName[0] + "." + fnameFormat # Now add correct extension
#     else:
#         if self.saveFolder is None or not os.path.exists(self.saveFolder):
#             self.saveFolder = os.path.join(winshell.desktop(), 'GelCAM')
#             os.makedirs(self.saveFolder, exist_ok=True)
#             self.ui.textSavedFolder.setText(self.saveFolder)
#
#         if fnameSuffix == "Date and Time":
#             fnameSuffix = datetime.now().strftime("%Y%m%d_%H%M%S")
#             nextFile = os.path.join(self.saveFolder, (fnamePrefix + fnameSuffix + "." + fnameFormat))
#
#         if fnameSuffix == "Auto Numbering":
#             # createPath = ("{}/{}{}.{}".format(self.saveFolder, fnamePrefix, i+1, fnameFormat))
#             # nextFile = seqfile.findNextFile(self.saveFolder, prefix=fnamePrefix)
#             # nextFile = nextFile + "." + fnameFormat
#             # # splitNextFile = os.path.splitext(nextFile)
#             # # print(splitNextFile[0])
#             # # os.remove(splitNextFile[0])
#             nextFile = seqfile.findNextFile(folder=self.saveFolder, prefix=fnamePrefix, suffix=("." + fnameFormat))
#
#     if fnameFormat == "JPEG":
#         imag.save(nextFile, format='JPEG', dpi=(300.0, 300.0), exif=exif_bytes)
#     if fnameFormat == "TIFF":
#         imag.save(nextFile, format='TIFF', dpi=(300.0, 300.0), exif=exif_bytes)
#     if fnameFormat == "BMP":
#         imag.save(nextFile, format='BMP', dpi=(300.0, 300.0), exif=exif_bytes)
#     if fnameFormat == "PNG":
#         imag.save(nextFile, format='PNG', dpi=(300.0, 300.0), exif=exif_bytes)
#
#-----------------------------------------------------------------------------------------------------------------------

# For MONO Images
    @Slot() # For grayscale images
    def eventStillImageSignal(self):
        # stillImageStartTime = time.process_time()
        # stillImageStartTime = time.perf_counter()
        # print("CLICK IMAGE SLOT BEGIN:", stillImageStartTime)

        # NOTE: Since we are processing in RAW mode, camera sends picture data
        # without any rotation and at the highest resolution.
        # So no point in checking what is the resolution selected or what rotation.
        # Go with the largest resolution possible for the model because that is what is being sent.
        # Rotate the image after processing the RAW data.

        ## Following code creates image size based on what resolution is selected in Resolution Menu
        ## But we don't need this.
        # wd = self.resolutionTable[self.indexResolution][0]
        # ht = self.resolutionTable[self.indexResolution][1]

        # Following creates image size based on maximum resolution
        wd = self.resolutionTable[0][0]
        ht = self.resolutionTable[0][1]
        self.pic = bytes(wd * 2 * ht)
        self.hcam.PullStillImageV2(self.pic, 16, None)
        self.saveBufferToImage(self.pic, wd, ht)

    def saveBufferToImage(self, bufferToSave, wd, ht):

        self.flagToSaveLongExpoImage = False

        arrayFromRawBuffer = (np.frombuffer(bufferToSave, dtype="uint16"))  #
        # To convert a 12-bit image to 16-bit, we need to scale the RAW bits from 12 to 16 (i.e. * 2**4)
        arrayFromRawBuffer = arrayFromRawBuffer * self.scaleFactor #
        # print("Size:", arrayFromRawBuffer.shape) # Gives (1555200,)
        # So far arrayFromBuffer is a linear array

        imag16 = ImagePIL.frombuffer(data=arrayFromRawBuffer, mode='I;16', size=(wd, ht))
        imag16CV2 = np.array(imag16)
        arrayFromRawBuffer8 = np.uint8(np.array(arrayFromRawBuffer) / 256)
        imag8 = ImagePIL.frombuffer(data=arrayFromRawBuffer8, mode='L', size=(wd, ht))

        # To resize 8 bit images (jpg, bmp), check what's the current Resolution index.
        # If its 0, the original image.
        # If its 1, then extended resolution.
        # If its 2, then reduced resolution.
        # Pillow Resize doesn't work with 16 bit images
        # To resize 16 bit images, we convert the 16-bit Pillow image to an Open CV (16-bit) image
        # This Open CV is rotated since Open CV allows rotation of 16-bit images
        # The rotated Open CV image is then converted back to Pillow image to allow easy saving

        # If we are saving in Tiff or PNG (if yes, we will need special 16-bit Open CV rotation explained above)
        fnameFormat = self.ui.comboFormat.currentText()
        # Find out what is the resolution to be saved
        indx = 0
        indx = self.ui.comboResolution.currentIndex()
        if indx == 1:
            imag8 = imag8.resize( ( int(wd*self.extendedResolution), int(ht*self.extendedResolution) ), resample=1 )
            if fnameFormat == "TIFF" or fnameFormat == "PNG":
                width = int(wd * self.extendedResolution)
                height = int(ht * self.extendedResolution)
                imageResizedCV2 =  np.full((height, width), fill_value=500, dtype=np.uint16)
                resizeCV2(src=imag16CV2, dsize=(width, height), dst=imageResizedCV2)
                imag16 = ImagePIL.fromarray(imageResizedCV2)
            print("Extended Resolution:", self.extendedResolution)
        elif indx == 2:
            imag8 = imag8.resize( ( int(wd*self.reducedResolution), int(ht*self.reducedResolution) ), resample=1 )
            if fnameFormat == "TIFF" or fnameFormat == "PNG":
                width = int(wd * self.reducedResolution)
                height = int(ht * self.reducedResolution)
                imageResizedCV2 =  np.full((height, width), fill_value=500, dtype=np.uint16)
                resizeCV2(src=imag16CV2, dsize=(width, height), dst=imageResizedCV2)
                imag16 = ImagePIL.fromarray(imageResizedCV2)
            print("Reduced Resolution:", self.reducedResolution)


        imag8 = imag8.rotate((360 - int(self.rotationValue)), expand=True)
        imag16 = imag16.rotate((360 - int(self.rotationValue)), expand=True)

        #TODO
        # Gives flip value based on saved factory settings. See spinSaveFlip in FactorySettings GUI
        # self.saveFlip = 0, means no flip (so skip flipping). 1 = hori, 2 = vert, 3 = H+V. This parses to OpenCV 0, 1 and -1 correspondingly
        if self.saveFlip == 1:  # Horizontal Flip. Somehow we need to FLIP_TOP_BOTTOM for this.
            imag8 = imag8.transpose(ImagePIL.FLIP_TOP_BOTTOM)
            imag16 = imag16.transpose(ImagePIL.FLIP_TOP_BOTTOM)
        if self.saveFlip == 2:  # Vertical Flip
            imag8 = imag8.transpose(ImagePIL.FLIP_LEFT_RIGHT)
            imag16 = imag16.transpose(ImagePIL.FLIP_LEFT_RIGHT)
        if self.saveFlip == 3:  # Both flips need to be done
            imag8 = imag8.transpose(ImagePIL.FLIP_TOP_BOTTOM)
            imag8 = imag8.transpose(ImagePIL.FLIP_LEFT_RIGHT)
            imag16 = imag16.transpose(ImagePIL.FLIP_TOP_BOTTOM)
            imag8 = imag8.transpose(ImagePIL.FLIP_LEFT_RIGHT)

        # # This is for Open CV saving:
        # arrayFromRawBuffer = np.reshape(arrayFromRawBuffer, (-1, wd)) # Reshapes a 1d array (RAW data) to 2d 1440x1080 array
        # # imwrite('E:\\Python\\Touptek\\images\\bit_Test16cv2_12.TIFF', arrayFromRawBuffer, [int(IMWRITE_TIFF_COMPRESSION), 1]) # This saves 16-bit TIFF
        # imag8 = arrayFromRawBuffer8 = (arrayFromRawBuffer * 0.00390625) # Scale down to 8-bit
        # imwrite('E:\\Python\\Touptek\\images\\bit_Test16cv2_8.jpg', arrayFromRawBuffer8)

        zeroth_ifd = {
            piexif.ImageIFD.Make: u"Sony CCD",
            piexif.ImageIFD.Software: u"Sony OEM Scientific Camera System"
        }

        exif_ifd = {
            # piexif.ExifIFD.DateTimeOriginal: u"2099:09:29 10:10:10",
            piexif.ExifIFD.LensMake: u"Computar",
            piexif.ExifIFD.Sharpness: 65535,
            piexif.ExifIFD.LensModel: u"Zoom Lens",
        }
        exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd}
        exif_bytes = piexif.dump(exif_dict)

        fnameFormat = self.ui.comboFormat.currentText()
        fnamePrefix = self.ui.comboFnamePrefix.currentText()
        fnameSuffix = self.ui.comboFnameSuffix.currentText()

        if self.saveFolder is None or not os.path.exists(self.saveFolder):
            self.chooseSavedFolder()  # Asks where to save

        # If user inputs a saved folder then do the saving
        if os.path.exists(self.saveFolder):

            if fnamePrefix == "User Defined...":
                saveName = QFileDialog.getSaveFileName(None, "Save Image", '', "Images (*.jpg *.tif *.png *.bmp)")
                saveName = (os.path.splitext(saveName[0]))  # Remove jpg extension
                nextFile = saveName[0] + "." + fnameFormat  # Now add correct extension

            if fnameSuffix == "Date and Time":
                fnameSuffix = datetime.now().strftime("%Y%m%d_%H%M%S")
                nextFile = os.path.join(self.saveFolder, (fnamePrefix + fnameSuffix + "." + fnameFormat))

            if fnameSuffix == "Auto Numbering":
                nextFile = seqfile.findNextFile(folder=self.saveFolder, prefix=fnamePrefix, suffix=("." + fnameFormat))

            if fnameFormat == "JPEG":
                # imwrite(nextFile, arrayFromRawBuffer8, [IMWRITE_JPEG_QUALITY, 100])
                # temp = ImagePIL.open(nextFile)
                imag8.save(nextFile, format='JPEG', dpi=(300.0, 300.0), exif=exif_bytes, subsampling=0, quality=100)
            if fnameFormat == "BMP":
                imag8.save(nextFile, format='BMP', dpi=(300.0, 300.0), exif=exif_bytes)
            if fnameFormat == "PNG":
                imag16.save(nextFile, format='PNG', dpi=(300.0, 300.0))
            if fnameFormat == "TIFF":
                imag16.save(nextFile, format='TIFF', dpi=(300.0, 300.0))

    def next_path(path):
        path = os.path.expanduser(path)

        if not os.path.exists(path):
            return path

        root, ext = os.path.splitext(os.path.expanduser(path))
        dir = os.path.dirname(root)
        fname = os.path.basename(root)
        candidate = fname + ext
        index = 0
        ls = set(os.listdir(dir))
        while candidate in ls:
            candidate = "{}_{}.{}".format(fname, index, ext)
            index += 1
        return os.path.join(dir, candidate)

    def closeEvent(self, event):
        if self.hcam is not None:
            # print("Date:", nncam.Nncam.ProductionDate(self.hcam))
            self.saveApplicationSettings()
            self.hcam.Close()
            self.hcam = None
            # print("Closing Application")
        if self.ArduinoPortInMainDOTpy != None:
            self.ardu.switchOFF()

    def changeAutoExposure(self, state):
        if self.hcam is not None:
            #State is True if Auto and False if Manual
            if self.ui.buttonAutoExposure.isChecked():
                self.ui.buttonAutoExposure.setText("Auto Exposure ON | Manual Exposure Off")
                self.hcam.put_AutoExpoEnable(True)
                self.ui.progressExposureTime.setMaximum(100)
                self.ui.progressExposureTime.setValue(0)
            else:
                self.ui.buttonAutoExposure.setText("Manual Exposure ON | Auto Exposure Off")

    def selectVideoOrChemiMode(self):

        # Live Mode (exposures < 5 sec)
        if self.ui.radioVideoMode.isChecked():
            self.hcam.put_Option(nncam.NNCAM_OPTION_TRIGGER, 0)
            self.videoModeSelected = True
            self.ui.frameVideoMode.setEnabled(True)
            self.ui.frameChemiMode.setEnabled(False)
            self.ui.buttonSaveChemi.setEnabled(False)
            self.ui.buttonSave.setEnabled(True)
            self.ui.spinExposureSec.setMaximum(4)
            self.hcam.put_ExpoTime(350000)
            self.hcam.put_AutoExpoEnable(True)

        # Chemi Mode (long exposures)
        if self.ui.radioChemiMode.isChecked():
            self.hcam.put_Option(nncam.NNCAM_OPTION_TRIGGER, 1)
            self.videoModeSelected = False
            self.ui.buttonSaveChemi.setEnabled(True)
            self.ui.buttonSave.setEnabled(False)
            self.ui.frameVideoMode.setEnabled(False)
            self.ui.frameChemiMode.setEnabled(True)
            self.ui.spinLongExposureSec.setMinimum(5)
            self.hcam.put_AutoExpoEnable(False)

    def changeExposure(self):

        if self.hcam is not None:
            if self.ui.buttonAutoExposure.isChecked():
                self.ui.buttonAutoExposure.setText("Auto Exposure ON | Manual Exposure Off")
                self.ui.progressExposureTime.setMaximum(100)
                self.ui.progressExposureTime.setValue(0)

            else:
                self.hcam.put_AutoExpoEnable(False)
                self.ui.buttonAutoExposure.setText("Manual Exposure ON | Auto Exposure Off")
                self.timeExpo =     self.ui.sliderExposureSec.value()        *  1000000 \
                                    + self.ui.sliderExposureMilliSec.value() *     1000
                if self.timeExpo < 100: # if < 100uS
                    self.timeExpo = 100 # Rangecheck

                self.hcam.put_ExpoTime(self.timeExpo)   # Update the camera with this new exposure

                self.longTimerCount = self.timeExpo/1000000
                if self.longTimerCount < 1:
                    self.longTimerCount = 1
                # Run exposure countdown timer iff Set Exposure is > 1 second, i.e. expoTimerCount > 1000 x 1000 uS

    def changeLongExposure(self):
        if self.hcam is not None:
            self.disableVideoMode()
            self.timeExpo = self.ui.spinLongExposureMin.value() * 60000000 \
                            + self.ui.spinLongExposureSec.value() * 1000000 \
                            + self.ui.spinLongExposureMilliSec.value() * 1000  # \
            if self.timeExpo < 100:  # if < 100uS
                self.timeExpo = 100  # Rangecheck

            self.ui.progressExposureTime.setMaximum(100)
            self.ui.progressExposureTime.setValue(0)

    def updateHistogram(self):
        pass
        # red, green, blue = self.liveImage.split()
        # vals = np.array(green)
        # vals = self.liveImage
        # y, x = np.histogram(vals, range=(0, 255), bins=255)
        img8 = (self.videoFromRawBuffer12bit/16).astype('uint8')
        # plt.hist(img8, 256, [0, 256])
        # plt.draw()
        # plt.pause(.1)
        # plt.clf()
        # # self.plt1.plot(x, y, stepMode=True, fillLevel=None, fillOutline=True, brush=(0, 0, 255, 200))
        # self.plt1.setData(x,y)

    def addGrid(self):
        gridFormat = 0
        gridTypes = [0, 2, 3, 5, 10]
        penColour = [Qt.red, Qt.green, Qt.blue, Qt.white, Qt.black]
        penThick = int(self.ui.comboPenThick.currentText())
        gridFormat = gridTypes[int(self.ui.comboGrid.currentIndex())]
        pen = QPen(penColour[int(self.ui.comboPenColour.currentIndex())], penThick, Qt.SolidLine)
        if gridFormat != 0:
            gridH = self.imageScaleH / gridFormat
            gridW = self.imageScaleW / gridFormat
            for i in range(gridFormat):
                for j in range(gridFormat):
                    r = QtCore.QRectF(QtCore.QPointF(i * gridW, j * gridH), QtCore.QSizeF(gridW, gridH))
                    self.scene.addRect(r, pen)

    def chooseSavedFolder(self): # existdir is some default directory we want to save in
        self.saveFolder = QFileDialog.getExistingDirectory(None, 'Select a folder to save the images:', self.desktopLoc, QFileDialog.ShowDirsOnly)
        self.ui.textSavedFolder.setText(self.saveFolder)

    def confirmSavedFolder(self):
        self.saveFolder = QFileDialog.getExistingDirectory(None, caption='Confirm the folder to save the images:', dir=self.saveFolder)
        self.ui.textSavedFolder.setText(self.saveFolder)

    def displayExposure(self):
            if self.ui.buttonAutoExposure.isChecked():
                self.divideTime()
                self.ui.sliderExposureSec.setDisabled(True)
                self.ui.sliderExposureMilliSec.setDisabled(True)
                self.ui.spinExposureSec.setDisabled(True)
                self.ui.spinExposureMilliSec.setDisabled(True)
            else:
                self.ui.sliderExposureSec.setDisabled(False)
                self.ui.sliderExposureMilliSec.setDisabled(False)
                self.ui.spinExposureSec.setDisabled(False)
                self.ui.spinExposureMilliSec.setDisabled(False)

    def getExpoTimeRange(self):
        ## Get the camera's exposure range (minimum exposure to maximum exposure possible with the camera).
        ## Set up the Exposure sliders with these maximum and minimum
        if self.hcam is not None:
            self.expoTimeRange = self.hcam.get_ExpTimeRange()

            ## If exposure range < 60 seconds, hide the "Exposure in Minutes" slider
            ## If exposure range > 60 seconds, show Seconds slider till 60 and then minutes
            ## 60 seconds = 60 x 1000 x 1000 uS = 60000000 uS
            ## 3600 seconds = 3600 x 1000 x 1000 uS = 3600000000 uS

            milliSec, microSec = divmod((self.expoTimeRange[1]-1), 1000) # -1 so that max expo in Min or Sec + milliSec, give 1999999 and not 2999999
            seconds, milliSec = divmod(milliSec, 1000)
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)

    def divideTime(self):
        if self.hcam is not None:
            milliSec, microSec = divmod((self.expoTime-1), 1000) # -1 so that max expo in Min or Sec + milliSec, give 1999999 and not 2999999
            seconds, milliSec = divmod(milliSec, 1000)
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)
            # sec = self.expoTime // 1000000
            # mS = (self.expoTime // 1000) - (sec*1000)
            # uS = (self.expoTime // 1) - (mS*1000) - (sec*1000000)
            self.ui.sliderExposureSec.setValue(seconds)
            self.ui.sliderExposureMilliSec.setValue(milliSec)

    def getResolution(self):
        # Find out how many resolutions this camera offers.
        # F.e. it will be 2 for I3CMOS0500KMB, viz. 2448*2048 and 1224*1024
        # Build an array (resolutionTable) of these resolutions. Extract width(2448) and height(2048) from the resolutions
        # Use the resolutionTable to display the resolutions in the Resolution combobox
        if self.hcam is not None:
            self.resolutionNumber = self.hcam.ResolutionNumber()

            self.resolutionTable = []

            # for i in range(self.resolutionNumber):
            #     w = int(self.hcam.get_Resolution(i)[0])
            #     h = int(self.hcam.get_Resolution(i)[1])
            #     self.ui.comboResolution.addItem(str(w) + ' x ' + str(h) + '; ' + str(round(w*h/(1000000),1)) + ' megapixels')
            #     self.resolutionTable.append(self.hcam.get_Resolution(i))

            w = int(self.hcam.get_Resolution(0)[0])
            h = int(self.hcam.get_Resolution(0)[1])
            self.ui.comboResolution.addItem(str(w) + ' x ' + str(h) + '; ' + str(round(w*h/(1000000),1)) + ' megapixels')
            self.resolutionTable.append(self.hcam.get_Resolution(0))


            # If there is an extended(or reduced) resolution (which is not equal to 1) append it to the resolution table
            # While saving the image, check with comboResolution index is selected.
            # If it points to extended (or reduced) resolution, image should be saved according to that size.
            if self.extendedResolution != 1:
                ext_w = int((self.hcam.get_Resolution(0)[0]) * self.extendedResolution)
                ext_h = int((self.hcam.get_Resolution(0)[1]) * self.extendedResolution)
                self.ui.comboResolution.addItem(str(ext_w) + ' x ' + str(ext_h) + '; ' + str(round(ext_w*ext_h/(1000000),1)) + ' megapixels')
                self.resolutionTable.append((ext_w, ext_h))

            if self.reducedResolution != 1:
                red_w = int((self.hcam.get_Resolution(0)[0]) * self.reducedResolution)
                red_h = int((self.hcam.get_Resolution(0)[1]) * self.reducedResolution)
                self.ui.comboResolution.addItem(str(red_w) + ' x ' + str(red_h) + '; ' + str(round(red_w * red_h / (1000000), 1)) + ' megapixels')
                self.resolutionTable.append((red_w, red_h))

    def changeResolution(self):
        # Find the resolution index from the selected resolution in the Resolution combobox
        # This will be used later for clicking the image.
        if self.hcam is not None:
            self.indexResolution = self.ui.comboResolution.currentIndex()
            # print(self.resolutionTable[self.indexResolution][0])

    def changeRotationSlider(self):

        self.justRotatedSoCenterDisplay = True
        self.rotationLandscape = 1
        self.imgHeight = self.h
        self.imgWidth = self.w

        if self.hcam is not None:
            # print("DoneROTRADIO102")
            # self.rotationValue = int(self.ui.spinRotation.value())
            # print("DoneROTRADIO103")
            # if self.ui.radioZeroRotation.isChecked() or self.ui.radioOneEightyRotation.isChecked() == True:
            # # if self.rotationValue == 0 or self.rotationValue == 180:
            #     self.rotationLandscape = 1
            #     self.imgHeight = self.h
            #     self.imgWidth = self.w
            #     print("DoneROTRADIO104")
            # # elif self.rotationValue == 90 or self.rotationValue == 270:
            # if self.ui.radioNinetyRotation.isChecked() or self.ui.radioTwoSeventyRotation.isChecked() == True:
            #     print("DoneROTRADIO105")
            #     self.rotationLandscape = 0
            #     self.imgHeight = self.w
            #     self.imgWidth = self.h
            #     print("DoneROTRADIO106")

            # WE CREATE BUFFER HERE BASED ON THE ROTATION VALUE OF THE IMAGE.
            # We cannot do this earlier, because rotation value (spinbox) is checked only here.
            # Also everytime we change the rotation, we have to change the buffer too (w*h <-> h*w)...
            # ...and that is also when this method is called

            # FOR COLOUR CAMERAS:
            # self.buf = bytes((self.imgWidth * 24 + 31) // 32 * 4) * self.imgHeight #This is on page 7 of manual
            # self.pic = bytes((self.imgWidth * 24 + 31) // 32 * 4) * self.imgHeight

            # FOR MONO CAMERAS 8 bit:
            # self.buf = bytes((self.imgWidth) * self.imgHeight) # This is on page 7 of manual

            # FOR MONO CAMERAS 16 bit:
            self.pic = bytes(self.imgWidth * self.imgHeight * 2)
            self.buf = bytes(self.imgWidth * self.imgHeight * 2)

            # nncam.Nncam.put_Option(self.hcam, nncam.Nncam_OPTION_ROTATE, self.rotationValue)
            time.sleep(0.01)

    def changeRotation(self):

        self.justRotatedSoCenterDisplay = True

        if self.hcam is not None:
            self.rotationValue = int(self.ui.spinRotation.value())
            if self.rotationValue == 0 or self.rotationValue == 180:
                self.rotationLandscape = 1
                self.imgHeight = self.h
                self.imgWidth = self.w
            elif self.rotationValue == 90 or self.rotationValue == 270:
                self.rotationLandscape = 0
                self.imgHeight = self.w
                self.imgWidth = self.h


            # WE CREATE BUFFER HERE BASED ON THE ROTATION VALUE OF THE IMAGE.
            # We cannot do this earlier, because rotation value (spinbox) is checked only here.
            # Also everytime we change the rotation, we have to change the buffer too (w*h <-> h*w)...
            # ...and that is also when this method is called

            # FOR COLOUR CAMERAS:
            # self.buf = bytes((self.imgWidth * 24 + 31) // 32 * 4) * self.imgHeight #This is on page 7 of manual
            # self.pic = bytes((self.imgWidth * 24 + 31) // 32 * 4) * self.imgHeight

            # FOR MONO CAMERAS 8 bit:
            # self.buf = bytes((self.imgWidth) * self.imgHeight) # This is on page 7 of manual

            # FOR MONO CAMERAS 16 bit:
            self.pic = bytes(self.imgWidth * self.imgHeight * 2)
            self.buf = bytes(self.imgWidth * self.imgHeight * 2)

            # This code below doesn't seem to affect anything.
            # nncam.Nncam.put_Option(self.hcam, nncam.Nncam_OPTION_ROTATE, self.rotationValue)

            time.sleep(0.01)

    def zoomChange(self):
        # whenever we do something to the pixmap this should be called.
        # Prints whatever is needed
        # self.imgHeight and self.imgWidth calculated above
        self.zoomFactor = self.ui.sliderDisplayZoom.value() / 100
        # self.justRotatedSoCenterDisplay = True

    def fitinWindow(self):
    # Toggle between fit in window and original size
    # Uses the original image

        try:
            if self.ui.buttonFitWindow.isChecked():
                scaleRatioW = self.ui.graphicsView.width() / self.imgWidth
                scaleRatioH = self.ui.graphicsView.height() / self.imgHeight
                self.ui.sliderDisplayZoom.setValue(min(scaleRatioH, scaleRatioW) * 100)
                self.ui.buttonFitWindow.setText("Show Original Size")
            else:
                self.ui.sliderDisplayZoom.setValue(100)
                self.ui.buttonFitWindow.setText("Fit in Window")

        except AttributeError as e:
            self.ui.statusbar.showMessage("fitinWindow: No Image Loaded")

        self.zoomChange()

    def changeFrequency(self):
        freq = int(self.ui.comboFrequency.currentIndex())
        if freq == 0:
            self.hcam.put_HZ(1)  # 50Hz
        if freq == 1:
            self.hcam.put_HZ(0)  # 60Hz
        if freq == 2:
            self.hcam.put_HZ(2)  # Direct

    def addPrefix(self):
        if self.ui.lineAddPrefix:
            addedPrefix = self.ui.lineAddPrefix.text()
            self.ui.comboFnamePrefix.addItem(addedPrefix)

    def startExpoTimer(self): # Comes here when Start or Abort UV Timer button is clicked
        if self.longTimerCount != 0:                        # Timer count is the value user inputs
            self.expoTimerStart()                               # Start the timer
            self.ui.progressExposureTime.setMaximum(self.longExpoValue / 1000000)

        if self.longTimerCount == 0:                        # If timer count is zero...
            self.longTimerStarted = False                       # ...indicate timer has not been started

    def expoTimerStart(self): # Comes here when Update Exposure button is clicked
        if self.longTimerStarted == False:                      # Only START the timer if it is not already started
            self.longTimer = QTimer(self)                     #
            self.longTimer.timeout.connect(self.showExpoTime)     # Show the timer value at every time-out
            self.longTimer.start(1000)                        # Start the timer for 1000 mS time-outs
            self.longTimerStarted = True                        # Setup a flag to indicate timer has started running

    def showExpoTime(self): # Timer calls this when it times out (usually every 100 mS or 'x' in self.xxxxTimer.start(x) in timerStart routine)
        if self.longTimerStarted:                               # Check if timer is already running
            self.longTimerCount -= 1 # Decrement the timer      # If running, decrement timer count (that's already updated when slider/spin is changed)
            self.ui.progressExposureTime.setValue(self.longTimerCount)
            elapsedTime = self.longTimerCount
            self.ui.progressExposureTime.setValue(elapsedTime)
            if self.longTimerCount <= 0:
                self.longTimer.stop()
                self.longTimerStarted = False
                self.longTimerCount = self.longExpoValue / 1000000        # Reset timer

##======================================================================================================================
## UV Timer or Stain-Free system

    def startUVTimer(self): # Comes here when Start or Abort UV Timer button is clicked
        if self.timerCount != 0:                            # Timer count is the value user inputs
            self.timerStart()                               # Start the timer
            self.ui.buttonStartStainFree.setDisabled(True)  # Disable the Start button ( we just clicked it to come here)
            self.ui.sliderStainFree.setDisabled(True)       # Disable the value changing slider and spinbox
            self.ui.spinStainFree.setDisabled(True)         #
            if not self.ui.buttonMains.isChecked():         # Switch ON Mains if not already
                self.ardu.relayOperate(pinMains, pin_ON)    # Operate the Arduino pin
                self.ui.buttonMains.setChecked(True)        # And show the button is checked
            if not self.ui.buttonTransUV.isChecked():       # Switch ON the TUV if not already
                self.ardu.relayOperate(pinTUV, pin_ON)      # Operate the Arduino pin
                self.ui.buttonTransUV.setChecked(True)      # And show the button is checked

        if self.timerCount == 0:                            # If timer count is zero...
            self.timerStarted = False                       # ...indicate timer has not been started

    def timerStart(self): # Timer times out every 1000 mS or 'x' in self.xxxxTimer.start(x)
        if self.timerStarted == False:                      # Only START the timer if it is not already started
            self.uvTimer = QTimer(self)                     #
            self.uvTimer.timeout.connect(self.showTime)     # Show the timer value at every time-out
            self.uvTimer.start(1000)                        # Start the timer for 1000 mS time-outs
            self.timerStarted = True                        # Setup a flag to indicate timer has started running

    def showTime(self): # Timer calls this when it times out (usually every 1000 mS or 'x' in self.uvTimer.start(x) in timerStart routine)
        if self.timerStarted:                               # Check if timer is already running
            self.timerCount -= 1 # Decrement the timer      # If running, decrement timer count (that's already updated when slider/spin is changed)
            self.displayTimerCount()  # Update display of timer
            if self.timerCount == 0:                        #
                self.ardu.relayOperate(pinTUV, pin_OFF)     # If timer count is zero, turn off UV light
                self.ui.buttonTransUV.setChecked(False)     #
                self.timerStarted = False                   # Flag updated to indicate timer is not running
                self.uvTimer.stop()                         # Stop the QTimer
                self.ui.buttonStartStainFree.setDisabled(False) # Update the GUI
                self.ui.sliderStainFree.setDisabled(False)
                self.ui.spinStainFree.setDisabled(False)
                self.timerCount = self.ui.sliderStainFree.value()   # Reload the timer counter with the input timer value

    def setTimerValue(self):
        self.timerCount = self.ui.sliderStainFree.value()   # Load the timer counter with the input timer value

    def abortUVTimer(self):
        # self.timerCount = self.ui.sliderStainFree.value()
        self.ardu.relayOperate(pinTUV, pin_OFF)
        self.ui.buttonTransUV.setChecked(False)
        self.uvTimer.stop()
        self.ui.buttonStartStainFree.setDisabled(False)
        self.ui.sliderStainFree.setDisabled(False)
        self.ui.spinStainFree.setDisabled(False)
        self.timerCount = self.ui.sliderStainFree.value()
        self.timerStarted = False
        self.displayTimerCount()

    def displayTimerCount(self):
        text = str(self.timerCount)
        text = text.zfill(3)
        self.ui.labelElapsedTime.setText(text)
#-----------------------------------------------------------------------------------------------------------------------

    def saveApplicationSettings(self):
        self.applicationConfig['ExposureValues'] = {
            "autoexposure": self.ui.buttonAutoExposure.isChecked(),
            "exposuremillisec": self.ui.sliderExposureMilliSec.value(),
            "exposuresec": self.ui.sliderExposureSec.value(),
            "longexposuremillisec": self.ui.spinLongExposureMilliSec.value(),
            "longexposuresec": self.ui.spinLongExposureSec.value(),
            "longexposuremin": self.ui.spinLongExposureMin.value(),
            "chemimode": self.ui.radioChemiMode.isChecked(),
            "videomode": self.ui.radioVideoMode.isChecked()

        }
        self.applicationConfig['IlluminationSwitches'] = {
            "mains": self.ui.buttonMains.isChecked(),
            "epiwhite": self.ui.buttonEpiWhite.isChecked(),
            "transuv": self.ui.buttonTransUV.isChecked(),
            "transwhite": self.ui.buttonTransWhite.isChecked(),
            "transblue": self.ui.buttonTransBlue.isChecked(),
            "epiuva": self.ui.buttonEpiUVA.isChecked(),
            "epiuvb": self.ui.buttonEpiUVB.isChecked()
        }
        self.applicationConfig['General'] = {
            "frequency": self.ui.comboFrequency.currentIndex()
        }
        self.applicationConfig['Display'] = {
            "fitwindow": self.ui.buttonFitWindow.isChecked(),
            "grid": self.ui.comboGrid.currentIndex(),
            "penthick": self.ui.comboPenThick.currentIndex(),
            "pencolour": self.ui.comboPenColour.currentIndex(),
            "rotation": self.ui.spinRotation.value()
        }

        self.applicationConfig['SaveStuff'] = {
                                        "savedfolder": str(self.saveFolder)
                                        # "prefixes":
                                        }
        # Create the config.ini path
        saveAppSettingsFolder = os.path.join(user_data_dir(appname=appName, appauthor=appAuthor), 'init')
        if not os.path.exists(saveAppSettingsFolder) or os.stat(saveAppSettingsFolder).st_size == 0:
            os.makedirs(saveAppSettingsFolder, exist_ok=True)
        saveAppSettingsFileName = 'startup.ini'
        saveFullName = os.path.join(saveAppSettingsFolder, saveAppSettingsFileName)
        with open(saveFullName, 'w') as startupConfig:
            self.applicationConfig.write(startupConfig)
#-----------------------------------------------------------------------------------------------------------------------

    def loadApplicationSettings(self):
        # Create the obvious startup.ini path
        saveAppSettingsFolder = os.path.join( user_data_dir(appname=appName, appauthor=appAuthor), 'init')
        saveAppSettingsFileName = 'startup.ini'
        startupSettingsFile = os.path.join(saveAppSettingsFolder, saveAppSettingsFileName)
        print(startupSettingsFile)

        if os.path.isfile(startupSettingsFile):
            self.applicationConfig.read(startupSettingsFile) # Read settings from config file

            # Read Exposure values and change them
            millisec = self.applicationConfig.getint('ExposureValues', 'exposuremillisec', fallback=300)
            self.ui.sliderExposureMilliSec.setValue(millisec)
            second = self.applicationConfig.getint('ExposureValues', 'exposuresec', fallback=0)
            self.ui.sliderExposureSec.setValue(second)
            self.changeExposure()
            autoexpo = self.applicationConfig.getboolean('ExposureValues', 'autoexposure', fallback=True)
            self.ui.buttonAutoExposure.setChecked(autoexpo)
            if autoexpo:
                self.ui.buttonAutoExposure.setText("Auto Exposure ON | Manual Exposure Off")
                self.hcam.put_AutoExpoEnable(True)
            else:
                self.ui.buttonAutoExposure.setText("Manual Exposure ON | Auto Exposure Off")
                self.hcam.put_AutoExpoEnable(False)


            longexpomillisec = self.applicationConfig.getint('ExposureValues', 'longexposuremillisec', fallback=300)
            self.ui.spinLongExposureMilliSec.setValue(longexpomillisec)
            longexposec = self.applicationConfig.getint('ExposureValues', 'longexposuresec', fallback=1)
            self.ui.spinLongExposureSec.setValue(longexposec)
            longexpomin = self.applicationConfig.getint('ExposureValues', 'longexposuremin', fallback=000)
            self.ui.spinLongExposureMin.setValue(longexpomin)

            chemilummode = self.applicationConfig.getboolean('ExposureValues', 'chemimode', fallback=False)
            self.ui.radioChemiMode.setChecked(chemilummode)
            livemode = self.applicationConfig.getboolean('ExposureValues', 'videomode', fallback=True)
            self.ui.radioVideoMode.setChecked(livemode)


            # Read Switches and change them
            value = self.applicationConfig.getboolean('IlluminationSwitches', 'mains', fallback=True)
            self.ui.buttonMains.setChecked(value)
            value = self.applicationConfig.getboolean('IlluminationSwitches', 'epiwhite', fallback=False)
            self.ui.buttonEpiWhite.setChecked(value)
            value = self.applicationConfig.getboolean('IlluminationSwitches', 'transuv', fallback=False)
            self.ui.buttonTransUV.setChecked(value)
            value = self.applicationConfig.getboolean('IlluminationSwitches', 'transwhite', fallback=False)
            self.ui.buttonTransWhite.setChecked(value)
            value = self.applicationConfig.getboolean('IlluminationSwitches', 'transblue', fallback=False)
            self.ui.buttonTransBlue.setChecked(value)
            value = self.applicationConfig.getboolean('IlluminationSwitches', 'epiuva', fallback=False)
            self.ui.buttonEpiUVA.setChecked(value)
            value = self.applicationConfig.getboolean('IlluminationSwitches', 'epiuvb', fallback=False)
            self.ui.buttonEpiUVB.setChecked(value)

            self.relayMains()
            time.sleep(0.1)
            self.relayEWL()
            time.sleep(0.1)
            self.relayTUV()
            time.sleep(0.1)
            self.relayTWL()
            time.sleep(0.1)
            self.relayTBL()
            time.sleep(0.1)
            self.relayUVA()
            time.sleep(0.1)
            self.relayUVB()
            time.sleep(0.1)

            # Read the General settings
            value = self.applicationConfig.getint('General', 'frequency', fallback=0)
            self.ui.comboFrequency.setCurrentIndex(value)

            # Read the Display settings
            value = self.applicationConfig.getboolean('Display', 'fitwindow', fallback=True)
            self.ui.buttonFitWindow.setChecked(value)
            value = self.applicationConfig.getint('Display', 'grid', fallback=0)
            self.ui.comboGrid.setCurrentIndex(value)
            value = self.applicationConfig.getint('Display', 'penthick', fallback=0)
            self.ui.comboPenThick.setCurrentIndex(value)
            value = self.applicationConfig.getint('Display', 'pencolour', fallback=0)
            self.ui.comboPenColour.setCurrentIndex(value)
            value = self.applicationConfig.getint('Display', 'rotation', fallback=0)
            self.ui.spinRotation.setValue(value)

            # Read Save data (folder to save in, format, prefix etc)
            value = self.applicationConfig.get('SaveStuff', 'savedfolder', fallback=None)
            saveFolder = Path(value)
            if os.path.exists(saveFolder):
                os.makedirs(saveFolder, exist_ok=True)
                self.ui.textSavedFolder.setText(value)
                self.saveFolder = saveFolder
#-----------------------------------------------------------------------------------------------------------------------

    def setupFactorySettings(self):
        settingsDict = [self.extendedResolution, self.reducedResolution, self.defaultRotation, self.displayFlip,
                        self.saveFlip,
                        self.showTransWL, self.showTransBL, self.showEpiUVA, self.showEpiUVB, self.showTemperTab]

        dialog = FactorySettingsWindow(settingsDict)

        if dialog.exec_():
            self.extendedResolution = dialog.factSett.spinExtendedResolution.value()
            self.reducedResolution = dialog.factSett.spinReducedResolution.value()
            self.defaultRotation = dialog.factSett.spinDefaultRotation.value()
            self.displayFlip = dialog.factSett.spinDisplayFlip.value()
            self.saveFlip = dialog.factSett.spinSaveFlip.value()
            self.showTransWL = dialog.factSett.checkTransWL.isChecked()
            self.showTransBL = dialog.factSett.checkTransBL.isChecked()
            self.showEpiUVA = dialog.factSett.checkEpiUVA.isChecked()
            self.showEpiUVB = dialog.factSett.checkEpiUVB.isChecked()
            self.showTemperTab = dialog.factSett.checkTemperatureTab.isChecked()
            self.saveFactorySettings()
#-----------------------------------------------------------------------------------------------------------------------

    def saveFactorySettings(self):

        self.factoryConfig['FactorySettings'] = {
            "extended": int(self.extendedResolution * 10000),  # Because extended resolution is like 1.2500 or 1.5000
            "reduced": int(self.reducedResolution * 100),
            "defaultrotation": self.defaultRotation,
            "displayflip": self.displayFlip,
            "saveflip": self.saveFlip,
            "showtranswl": self.showTransWL,
            "showtransbl": self.showTransBL,
            "showepiuva": self.showEpiUVA,
            "showepiuvb": self.showEpiUVB,
            "showtempertab": self.showTemperTab
        }
        # Create the config.ini path
        saveFactorySettingsFolder = os.path.join( user_data_dir(appname=appName, appauthor=appAuthor), 'init')
        if not os.path.exists(saveFactorySettingsFolder) or os.stat(saveFactorySettingsFolder).st_size == 0:
            os.makedirs(saveFactorySettingsFolder, exist_ok=True)
        saveFactorySettingsName = 'config.ini'
        saveFullName = os.path.join(saveFactorySettingsFolder, saveFactorySettingsName)
        with open(saveFullName, 'w') as factoryConfig:
            self.factoryConfig.write(factoryConfig)
#-----------------------------------------------------------------------------------------------------------------------

    def readFactorySettings(self):
    # The FactorySettings file makes it easier for GUI to be customised as per customer's requirements.
    # A config file in user_data directory needs to be installed.
    # A config file as part of the includes could also be done since user may do fresh install and a config file in
    # user_data will be absent.

        # Create the obvious config.ini path
        saveFactorySettingsFolder = os.path.join( user_data_dir(appname=appName, appauthor=appAuthor), 'init')
        saveFactorySettingsName = 'config.ini'
        settingsFile = os.path.join(saveFactorySettingsFolder, saveFactorySettingsName)

        if os.path.isfile(settingsFile):
            self.factoryConfig.read(settingsFile)

            # Read the Factory settings
            value = self.factoryConfig.getint('FactorySettings', 'extended', fallback=20000)
            self.extendedResolution = value / 10000  # Because extended resolution is like 1.2500 or 1.5000

            value = self.factoryConfig.getint('FactorySettings', 'reduced', fallback=25)
            self.reducedResolution = value * 2 / 100

            value = self.factoryConfig.getint('FactorySettings', 'defaultrotation', fallback=270)
            self.defaultRotation = value

            self.displayFlip = self.factoryConfig.getint('FactorySettings', 'displayflip', fallback=0)
            self.saveFlip = self.factoryConfig.getint('FactorySettings', 'saveflip', fallback=0)

            self.showTransWL = self.factoryConfig.getboolean('FactorySettings', 'showtranswl', fallback=True)
            self.showTransBL = self.factoryConfig.getboolean('FactorySettings', 'showtransbl', fallback=False)
            self.showEpiUVA = self.factoryConfig.getboolean('FactorySettings', 'showepiuva', fallback=False)
            self.showEpiUVB = self.factoryConfig.getboolean('FactorySettings', 'showepiuvb', fallback=False)
            self.showTemperTab = self.factoryConfig.getboolean('FactorySettings', 'showtempertab', fallback=False)


        self.ui.buttonTransWhite.setVisible(self.showTransWL)
        self.ui.buttonTransBlue.setVisible(self.showTransBL)
        self.ui.buttonEpiUVA.setVisible(self.showEpiUVA)
        self.ui.buttonEpiUVB.setVisible(self.showEpiUVB)

        self.ui.spinRotation.setValue(self.defaultRotation)

        if self.showTemperTab == False:
            self.ui.toolTemperature.setVisible(False)
            self.ui.cameraAdjustments.removeItem(3)
#-----------------------------------------------------------------------------------------------------------------------

    def saveProtocol(self):
        self.config['DEFAULT'] = {
                                  "test1": "1",
                                  "test2": "2",
                                  }

        self.config['ExposureValues'] = {
                                        "autoexposure": self.ui.buttonAutoExposure.isChecked(),
                                        # "exposuremicrosec": self.ui.sliderExposureMicroSec.value(),
                                        "exposuremillisec": self.ui.sliderExposureMilliSec.value(),
                                        "exposuresec": self.ui.sliderExposureSec.value()
                                        }

        self.config['IlluminationSwitches'] = {
                                        "mains": self.ui.buttonMains.isChecked(),
                                        "epiwhite": self.ui.buttonEpiWhite.isChecked(),
                                        "transuv": self.ui.buttonTransUV.isChecked(),
                                        "transwhite": self.ui.buttonTransWhite.isChecked(),
                                        "transblue": self.ui.buttonTransBlue.isChecked(),
                                        "epiuva": self.ui.buttonEpiUVA.isChecked(),
                                        "epiuvb": self.ui.buttonEpiUVB.isChecked()
                                        }

        self.config['General'] = {
                                        "frequency": self.ui.comboFrequency.currentIndex()
                                        }

        self.config['Display'] = {
                                        "fitwindow": self.ui.buttonFitWindow.isChecked(),
                                        "grid": self.ui.comboGrid.currentIndex(),
                                        "penthick": self.ui.comboPenThick.currentIndex(),
                                        "pencolour": self.ui.comboPenColour.currentIndex(),
                                        "rotation": self.ui.spinRotation.value()
                                        }

        self.config['SaveStuff'] = {
                                        "savedfolder": str(self.saveFolder)
                                        # "prefixes":
                                        }

        AllItems = [self.ui.comboFnamePrefix.itemText(i) for i in range(self.ui.comboFnamePrefix.count())]
        #TODO: Not saving prefixes now. Do it later. Not important

        saveProtocolName = QFileDialog.getSaveFileName(None, "Save Protocol", '', "Protocol (*.conf)")
        # print("Protocol Location:", saveProtocolName[0])

        # if not os.path.exists(saveProtocolName[0]) or os.stat(saveProtocolName[0]).st_size == 0:
        # if os.path.exists(saveProtocolName[0]):
        if saveProtocolName[0]:
            print("Protocol:", saveProtocolName[0])
            with open(saveProtocolName[0], 'w') as configfile:
                self.config.write(configfile)
#-----------------------------------------------------------------------------------------------------------------------

    def loadProtocol(self):

        self.protocolFile = QFileDialog.getOpenFileName(None, 'Open Protocol', '', "Protocol (*.conf)")

        if self.protocolFile[0] != '':
            self.config.read(self.protocolFile)
            # Read Exposure values and change them
            # microsec = self.config.getint('ExposureValues', 'exposuremicrosec', fallback=500)
            # self.ui.sliderExposureMicroSec.setValue(microsec)
            millisec = self.config.getint('ExposureValues', 'exposuremillisec', fallback=300)
            self.ui.sliderExposureMilliSec.setValue(millisec)
            second = self.config.getint('ExposureValues', 'exposuresec', fallback=0)
            self.ui.sliderExposureSec.setValue(second)

            self.changeExposure()
            autoexpo = self.config.getboolean('ExposureValues', 'autoexposure', fallback=True)
            self.ui.buttonAutoExposure.setChecked(autoexpo)

            # Read Switches and change them
            value = self.config.getboolean('IlluminationSwitches', 'mains', fallback=True)
            self.ui.buttonMains.setChecked(value)
            value = self.config.getboolean('IlluminationSwitches', 'epiwhite', fallback=False)
            self.ui.buttonEpiWhite.setChecked(value)
            value = self.config.getboolean('IlluminationSwitches', 'transuv', fallback=False)
            self.ui.buttonTransUV.setChecked(value)
            value = self.config.getboolean('IlluminationSwitches', 'transwhite', fallback=False)
            self.ui.buttonTransWhite.setChecked(value)
            value = self.config.getboolean('IlluminationSwitches', 'transblue', fallback=False)
            self.ui.buttonTransBlue.setChecked(value)
            value = self.config.getboolean('IlluminationSwitches', 'epiuva', fallback=False)
            self.ui.buttonEpiUVA.setChecked(value)
            value = self.config.getboolean('IlluminationSwitches', 'epiuvb', fallback=False)
            self.ui.buttonEpiUVB.setChecked(value)

            self.relayMains()
            time.sleep(0.1)
            self.relayEWL()
            time.sleep(0.1)
            self.relayTUV()
            time.sleep(0.1)
            self.relayTWL()
            time.sleep(0.1)
            self.relayTBL()
            time.sleep(0.1)
            self.relayUVA()
            time.sleep(0.1)
            self.relayUVB()
            time.sleep(0.1)

            # Read the General settings
            value = self.config.getint('General', 'frequency', fallback=0)
            self.ui.comboFrequency.setCurrentIndex(value)

            # Read the Display settings
            value = self.config.getboolean('Display', 'fitwindow', fallback=True)
            self.ui.buttonFitWindow.setChecked(value)
            value = self.config.getint('Display', 'grid', fallback=0)
            self.ui.comboGrid.setCurrentIndex(value)
            value = self.config.getint('Display', 'penthick', fallback=0)
            self.ui.comboPenThick.setCurrentIndex(value)
            value = self.config.getint('Display', 'pencolour', fallback=0)
            self.ui.comboPenColour.setCurrentIndex(value)
            value = self.config.getint('Display', 'rotation', fallback=0)
            self.ui.spinRotation.setValue(value)

            # Read Save data (folder to save in, format, prefix etc)
            value = self.config.get('SaveStuff', 'savedfolder', fallback=None)
            saveFolder = Path(value)
            if not os.path.exists(saveFolder):
                os.makedirs(saveFolder)
                self.ui.textSavedFolder.setText(value)
                self.saveFolder = saveFolder
#-----------------------------------------------------------------------------------------------------------------------

# class MatplotlibWidget(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super(MatplotlibWidget, self).__init__(parent)
#
#         # self.figure = Figure()
#         # self.canvas = FigureCanvasQTAgg(self.figure)
#
#         self.axis = self.figure.add_subplot(111)
#
#         self.layoutVertical = QtWidgets.QVBoxLayout(self)#QVBoxLayout
#         self.layoutVertical.addWidget(self.canvas)



if __name__ == "__main__":

    app = QApplication(sys.argv)

    myappid = 'Gel ProCCD Controller'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app.setWindowIcon(QIcon("lib_i_.config"))       # rename an icon file to something with obfuscated extension
    splash_pix = QPixmap("lib_s_.config")           # rename a jpg file to something with obfuscated extension
    splash = QSplashScreen(splash_pix, f=Qt.WindowStaysOnTopHint)
    splash.show()
    splash.showMessage("Loading...", alignment=Qt.AlignBottom, color=Qt.white)
    splash.close()

        # lodingLbl = QtWidgets.QLabel(splash)
        # lodingLbl.setPixmap()
        #
        # splashLoadingLayout = QtWidgets.QVBoxLayout()
        # splashLoadingLayout.addStretch()
        # splashLoadingLayout.addWidget(lodingLbl)
        # # splashLoadingLayout.addWidget(progressBar)
        # splashLoadingLayout.addStretch()
        # splashLoadingLayout.setAlignment(Qt.AlignVCenter)
        # newWid = QtWidgets.QWidget()
        # newWid.setLayout(splashLoadingLayout)
        # splashPermLayout = QtWidgets.QVBoxLayout()
        # splashPermLayout.addWidget(newWid)
        # splash.setLayout(splashPermLayout)
        # splash.setMask(splash_pix.mask())
        # splash.show()


    if(Login_System_Needed):
        window = Login()
    else:
        runForm = MainAppWindow()
        runForm.showMaximized()
        runForm.show()


    sys.exit(app.exec_())

#TODO: Create an arbitrary text file in Main folder and see if Pyarmor obfufscates it. If yes, use it for config.ini.
# Save the config file as non-standard extension so that user cannot open it, but office staff uses notepad to edit it.
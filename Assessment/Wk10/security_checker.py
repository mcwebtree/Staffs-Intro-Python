# Security system

# imports
import os
import hashlib
import binascii
import json 
import time 
import sys 
import getpass as gp

sys.path.append(os.path.abspath('..\\inc\\'))

import screen as s
import helpers as h

# classes
class User:
    min_len = 8
    allow_spaces = 0
    allow_leading_number = 0
    locked = 0
    lockouts = 0
    lockout_release = 0
    attempts = 0
    attempt_limit = 3
    lockout_period = 60
    loggedin = 0

    def __init__(self, username):
        self.username=username.upper()
        if username in a_users.keys():
            self.passwordhash=a_users[username]
        else:
            self.passwordhash=""

        if self.username in a_lockout.keys():
            self.lockouts= a_lockout[self.username]["a"]
            if time.time() < a_lockout[self.username]["r"]:
                self.locked=1
                self.lockout_release = a_lockout[self.username]["r"]
       
    def __str__(self):
        ret_str=""
        ret_str += "User: " + self.username + "\n"
        if self.passwordhash == "":
            ret_str += "Password: <not set>\n"
        else:
            ret_str += "Password: <set>\n"
        if self.locked == 1:
            ret_str += f"{s.REDON}Account is locked out until {self.lockout_release_str()}{s.COLOUROFF}\n"
            ret_str += f"Account has been locked out {self.lockouts} times.\n"
        else: 
            ret_str += f'Account is unlocked and active\n'
        return ret_str



    def check_password_complexity(self, password):
        valid_pass = 1
        s_err=""
        try:
            if self.min_len > 0:
                if len(password) < self.min_len:
                    s_err += f"* Minimum length {self.min_len}\n"
                    valid_pass = 0
            if self.allow_spaces == 0:
                if " " in password:
                    s_err += f"* No spaces\n"
                    valid_pass = 0
            if self.allow_leading_number == 0:
                if password[0].isdigit():
                    s_err += f"* Cannot begin with a number\n"
                    valid_pass = 0     
        except: 
            pass

        if valid_pass == 0:
            print ("Invalid Password. Please ensure it meets the minimum requirements: ")
            print ( s_err )

        return valid_pass
    
    def set_password(self, password):
        if self.check_password_complexity(password) == 1:
            self.passwordhash=self.hash_password(password)     


    def hash_password(self,password):
        salt =hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                    salt, 200000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')
    
    def verify_password(self,provided_password):
        f_return = False
        if self.is_locked_out():
            print ( f"{s.REDON}Sorry your account is locked out until {self.lockout_release_str()}{s.COLOUROFF}.\nPlease try again later")
        else:
            salt = self.passwordhash[:64]
            pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                        provided_password.encode('utf-8'),               
                                        salt.encode('ascii'), 
                                        200000)
            stored_password = self.passwordhash[64:]
            pwdhash = binascii.hexlify(pwdhash).decode('ascii')
            f_return = (pwdhash == stored_password)
            if f_return==True:
                self.loggedin = 1
            elif f_return == False:
                print ( f"{s.REDON}Sorry that username / password combination wasn't recognised.{s.COLOUROFF} \nPlease try again")
                self.attempts += 1
                if self.attempts >= self.attempt_limit:
                    # reset attempts
                    self.attempts = 0
                    # unlock account
                    self.locked = 1
                    # increment the punishment counter
                    self.lockouts +=1
                    # set the release time
                    self.lockout_release = int(time.time()) + (self.lockout_period * self.lockouts)
                    a_lockout[self.username] = {"r": self.lockout_release, "a": self.lockouts}

        return f_return

    def lockout_release_str(self):
         return time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(self.lockout_release))

    def is_locked_out(self):
        f_locked=0
        if self.locked == 1:
            t_now = time.time()
            t_lockout = self.lockout_release
            if t_now < t_lockout:
                f_locked = 1
            else:
                self.locked=0
                self.lockout_release=0
        return f_locked


def load_file():
    global a_users

    if os.path.isfile(s_filename):
        with open(s_filename) as sec_file:
            a_users=json.load(sec_file)
        pass

    else:
        # nothing to do
        pass

def write_file():
    with open(s_filename, "w") as sec_file:
        json.dump(a_users,sec_file)
    pass

# definitions
s_filename = "security_checker_users.json"
a_users =  {} 
a_lockout = {}

# Load the security file first.
load_file()

# debug 
#print (a_users)

while True:
    print ( f"\n\n{s.ORANGEON}Password Verifier 2000{s.COLOUROFF}" )
    print ( "-----------------------")
    print ( "1. New User" )
    print ( "2. Existing User" )
    print ( "3. Print Users" )
    print ( "4. Dump Current User Object" )
    print ( "0. Exit" )
    print ( "-----------------------")
    print ( "" )
    i_menu = h.get_int("Please enter your selection",1,4)
    
    if i_menu == 0:
        print ( f"\nThank you for using {s.ORANGEON}Password Verifier 2000{s.COLOUROFF}\n" )
        break
    elif i_menu == 1:
        s_usr = input( "Please enter your username [Enter to quit]: ").upper()
        if s_usr=="":
            break 

        if s_usr in a_users.keys():
            print ( f"{s.REDON}Username {s_usr} is already taken.{s.COLOUROFF}")
            time.sleep(1)
            break

        usr = User(s_usr)
        
        while True: 
                print ( f"Please enter a password for new user {s_usr}")
                s_p_1 = gp.getpass ( "Please enter the new password [Enter to abort]: ")
                if s_p_1 == "":
                    break
                s_p_2 = gp.getpass ( "Please re-enter the new password: ")

                if s_p_1 == s_p_2:
                    if usr.check_password_complexity(s_p_1) == 1:
                        usr.set_password(s_p_1)
                        a_users[usr.username] = usr.passwordhash
                        write_file()
                        print ( f"{s.GREENON}User {usr.username} added successfully.{s.COLOUROFF} ")
                        time.sleep (1)
                        break
                    else:
                        print (f"{s.REDON}Password complexity rules not met.{s.COLOUROFF}\nPlease try again")
                else: 
                    print (f"{s.REDON}Passwords do not match.{s.COLOUROFF}\nPlease try again")
    elif i_menu == 2:
                   
        s_usr = input( "Please enter your username [Enter to quit]: ").upper()
        if s_usr=="":
            break 
     
        if s_usr in a_users.keys():
            usr = User(s_usr)
            
            print ( f"\n{s.GREENON}Welcome back {s_usr}.{s.COLOUROFF}\n")
            
            if usr.is_locked_out():
                t_release = time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(usr.lockout_release))
                print ( f"{s.REDON}Sorry your account is locked out until {t_release}.{s.COLOUROFF}\nPlease try again later")
                time.sleep(1)
                continue
            else:
                f_loggedin=0
                while usr.locked == 0 and usr.loggedin == 0: 
                    s_pwd_try = gp.getpass ( f"Please enter password for user {usr.username}: " )
                    if usr.verify_password(s_pwd_try) == True:
                        break
                
                if usr.loggedin == 1:
                    print ( f"{s.GREENON}Welcome to the Password Verifier 2000.{s.COLOUROFF}\n{s.ORANGEON}You successfully entered your username and password!{s.COLOUROFF}" )
                    time.sleep ( 1 )
                else: 
                    print ( f"{s.REDON}{s.REVON}Password attempts limit exceeded.{s.REVOFF}{s.COLOUROFF} \nYour account has been locked for {(usr.lockout_period * usr.lockouts)} seconds." )
                    time.sleep ( 1 )
        else:
            print ( f"\n{s.REDON}Username not found. Please try again{s.COLOUROFF}\n" )
            time.sleep (1)
    
    elif i_menu == 3:
        print ("System Users")
        print ("------------")

        for this_user in a_users:
            usr = User(this_user)
            if usr.is_locked_out():
                s_colour = s.REDON
                s_timeout = f" on lockout {usr.lockouts} until {usr.lockout_release_str()} "
            else:
                s_colour = s.GREENON
                s_timeout = ""

            print ( f"{s_colour}{usr.username}{s.COLOUROFF} " + s_timeout)

        print ("------------")
        print ( "" )
    elif i_menu == 4:
        try:
            print ("\nCurrent User Object")
            print ("-------------------")
            
            print (usr)
        except Exception as e: 
            #print ( str(e))
            print ( "No current user object" )
            time.sleep ( 1 )
        finally:
            print ("")
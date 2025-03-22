#For exception handling ---------------------------------------
# Pehle hum do libraries import karte hain.
# sys: Yeh module Python ke interpreter ke sath interact karne ke liye use hota hai.
# logging: Yeh module messages ko log karne ke liye use hota hai, useful for debugging and tracking.
import sys 
#sys library have information if any exception is created
from src.logger import logging


# ---------------------------------------
# Yeh function exception ka detailed message generate karne ke liye bana hai.
def error_message_detail(error, error_detail: sys):  # Do parameters pass ho rahe hain: error, error_detail (jo sys se aayega)
   # error detail is basically present inside the sys.
    # error_detail.exc_info() se exception ka traceback milta hai.
    # Yeh teen values return karta hai (type, value, traceback). Humein bas traceback chahiye, toh humne _ use kiya baaki ke liye.
    _, _, exc_tb = error_detail.exc_info()  # exc_tb mein pura traceback mil jata hai.
#Trackback means which file error may occur in which line error may occur.

    # Ab humein pata karna hai ki error kis file mein hua hai.
    # exc_tb mein pura traceback hai, usme se file name nikalne ke liye hum yeh properties use karte hain.
    file_name = exc_tb.tb_frame.f_code.co_filename  
    # Yeh file ka naam nikalta hai jahan error hua hai.

    # Ab hum ek formatted error message bana rahe hain jismein:
    # 1. File ka naam
    # 2. Line number jahan error hua
    # 3. Error message jo pass kiya gaya hai
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,  # =0, Yeh file name add karne ke liye
        exc_tb.tb_lineno,  #=1,  Yeh line number add karne ke liye
        str(error)  #=2,  Yeh actual error message add karne ke liye
    )

    # Yeh function apna formatted message return kar raha hai.
    return error_message
#till now what we create is nothing but error message format 
#Below waht if any exception raises

# ---------------------------------------
# Ab hum apni Custom Exception class bana rahe hain jo Python ki Exception class se inherit kar rahi hai.
class CustomException(Exception):  # Exception parent class hai, hum isko inherit kar rahe hain.
    
    # Yeh init function hai, jo class ko initialize karte waqt call hota hai.
    def __init__(self, error_message, error_detail: sys):#error details can be get under sys
        # Yeh super() function parent class ka init function call karne ke liye use hota hai.
        super().__init__(error_message)

        # Hum error message ko store karte hain, par formatted message ke sath.
        # Yeh error_message_detail() function ko call kar raha hai taaki proper formatted message mile.
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    # Yeh __str__ function define karte hain taaki jab bhi hum is exception ko print karen, 
    # toh woh properly formatted message dikhaaye.
    def __str__(self):
        return self.error_message
# One more thing this is very common way initalize the exception
# We can use this in everyplace


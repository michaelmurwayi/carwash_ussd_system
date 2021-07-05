from africastalking.Service import Service
from flask import Flask
from flask import request
from flask import make_response
from flask_ngrok import run_with_ngrok
import africastalking
from werkzeug.wrappers.response import Response 

app = Flask(__name__)
run_with_ngrok(app)
username = "sandbox"
api_key = "17f2d3cb46b40d864a084736b597637efd73f309fed924d1fdb04640bdaed6aa"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

@app.route('/api/ussd/callback', methods=['POST'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phoneNumber = request.values.get("phonenumber", None)
    text = request.values.get("text", None)
    #serve menus based on text
    #ussd logic
    if text == "":
        #Car Wash Main Menu
        response = "CON Welcome to A+ car wash.Pick The Service you want\n"
        response += "1. Exclusive Wash \n"
        response += "2. Full car wash \n"
        response += "3. Body wash"
        response += "4. Interior Wash\n"
        response += "5. Waxing"
        response += "6. Dusting"
        response += "7. Carpet Wash"
    elif text == "1":
        # sub menu 1
        #Select Type of Car
        response = "CON Enter Typer of Car\n"
        response += "1. Sedan"
        response += "2. Suv"
        response += "3. Truck (pick-ups)"
        response += "4. Lorry"
    
    elif text == "2":
        #sub menu 2
        # Selecting Type of Car
        response = "CON Enter Typer of Car\n"
        response += "1. Sedan"
        response += "2. Suv"
        response += "3. Truck (pick-ups)"
        response += "4. Lorry"
    elif text == "3":
        # sub menu 3
        # Selecting Type of Car 
        response = "CON Enter Typer of Car\n"
        response += "1. Sedan"
        response += "2. Suv"
        response += "3. Truck (pick-ups)"
        response += "4. Lorry"
    elif text == "4":
        # sub menu 4 
        # Selecting Type of Car
        response = "CON Enter Typer of Car\n"
        response += "1. Sedan"
        response += "2. Suv"
        response += "3. Truck (pick-ups)"
        response += "4. Lorry"
    elif text == "5":
        # sub menu 5 
        # Selecting Type of Car
        response = "CON Enter Typer of Car\n"
        response += "1. Sedan"
        response += "2. Suv"
        response += "3. Truck (pick-ups)"
        response += "4. Lorry"
    elif text == "6":
        # sub menu 6 
        # Selecting Type of Car
        response = "CON Enter Typer of Car\n"
        response += "1. Sedan"
        response += "2. Suv"
        response += "3. Truck (pick-ups)"
        response += "4. Lorry"
    elif text == "7":
        # sub menu 7 
        # Selecting Type of Car
        response = "CON Enter Typer of Car\n"

    elif text == "1*1":
        response = "CON Enter Vehicle Registration "

    else:
        choices = request.values["text"][:3]
        if choices == "1*1":
            type_of_wash = "Full Body Wash"
            car_type = "Sedan"
            car_registration = request.values["text"][4:]
            response = f"END Car Wash Type: {type_of_wash}/n. Vehicle Type: {car_type}/n. Vehicle Registration: {car_registration}/n."
        elif choices == "1*2":
            type_of_wash = "Full Body Wash"
            car_type = "Suv"
            car_registration = request.values["text"][4:]
            response = f"END Car Wash Type: {type_of_wash}/n. Vehicle Type: {car_type}/n. Vehicle Registration: {car_registration}/n."
        elif choices == "1*3":
            type_of_wash = "Full Body Wash"
            car_type = "Truck"
            car_registration = request.values["text"][4:]
            response = f"END Car Wash Type: {type_of_wash}/n. Vehicle Type: {car_type}/n. Vehicle Registration: {car_registration}/n."
        elif choices == "1*4":
            type_of_wash = "Full Body Wash"
            car_type = "Lorry"
            car_registration = request.values["text"][4:]
            response = f"END Car Wash Type: {type_of_wash}/n. Vehicle Type: {car_type}/n. Vehicle Registration: {car_registration}/n."

    return response        
     



if __name__ == "__main__":
        app.run()
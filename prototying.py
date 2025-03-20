# import smtplib
# from email.mime.text import MIMEText
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderTimedOut

# def get_current_location():
#     try:
#         # Initialize Nominatim API
#         geolocator = Nominatim(user_agent="geoapiExercises")
        
#         # Get location details
#         location = geolocator.geocode("Senapati")
        
#         if location:
#             return location.latitude, location.longitude
#         else:
#             return None, None
#     except GeocoderTimedOut:
#         return None, None

# def send_email(subject, body, to_email):
#     from_email = "ashikgrg61@gmai.com"
#     from_password = "Ashik@2002"
    
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = from_email
#     msg['To'] = to_email
    
#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(from_email, from_password)
#         server.sendmail(from_email, [to_email], msg.as_string())
#         server.quit()
#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"Failed to send email: {e}")

# if __name__ == "__main__":
#     latitude, longitude = get_current_location()
    
#     if latitude and longitude:
#         location_url = f"https://www.google.com/maps?q={latitude},{longitude}"
#         email_body = f"My current location is:\nLatitude: {latitude}\nLongitude: {longitude}\nGoogle Maps: {location_url}"
        
#         send_email(
#             subject="My Current Location",
#             body=email_body,
#             to_email="ashikgrg62@gmail.com"
#         )
#     else:
#         print("Could not retrieve location.")

import geocoder

# Get location based on your public IP
g = geocoder.ip('me')

if g.ok:
    print("Coordinates (Latitude, Longitude):", g.latlng)
    print("City:", g.city)
    print("Country:", g.country)
else:
    print("Failed to retrieve location.")
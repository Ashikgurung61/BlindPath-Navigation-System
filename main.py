import speech_recognition as sr
from geopy.geocoders import Nominatim
import folium
import webbrowser
from twilio.rest import Client
from yolo import *
from sos import *

def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your network connection.")
    return None

def get_current_location():
    geolocator = Nominatim(user_agent="geo_locator")
    location = geolocator.geocode("") 
    if location:
        return (location.latitude, location.longitude)
    return None

def locate_me():
    coords = get_current_location()
    if coords:
        print(f"Your current location: {coords}")
        map = folium.Map(location=coords, zoom_start=15)
        folium.Marker(coords, popup="Your Location").add_to(map)
        map.save("map.html")
        webbrowser.open("map.html")
    else:
        print("Could not determine your location.")

def send_sos():
    main()

def start_journey(destination):
    start()
    print(f"Starting journey to {destination}...")
    print("Just walk and follow the directions.")

def main():
    while True:
        print("\n--- Voice Command Menu ---")
        print("1. Locate me")
        print("2. Start My Journey")
        print("3. SOS")
        print("4. Shut Down")

        choice = input()#recognize_voice()

        if choice == "1":
            locate_me()
        elif choice == "2":
            destination = input("Enter your destination: ")
            start_journey(destination)
        elif choice == "3":
            send_sos()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
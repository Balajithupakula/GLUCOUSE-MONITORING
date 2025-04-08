import random
import time
from blynkapi import Blynk
import requests
BLYNK_AUTH_TOKEN = 'c18b9632a2d94f7d88aa7c93d5e74e12'
BLYNK_URL = f'https://blynk.cloud/external/api/update?token={BLYNK_AUTH_TOKEN}'

VIRTUAL_PIN_GLUCOSE = 'V0'
VIRTUAL_PIN_ALERT = 'V1'

GLUCOSE_THRESHOLD = 180  

def send_to_blynk(pin, value):
    response = requests.get(f'{BLYNK_URL}&{pin}={value}')
    print(f"Sent to Blynk - {pin}: {value}, Status: {response.status_code}")

def simulate_glucose_reading():
    return random.randint(70, 250)  

def trigger_insulin_injector():
    print("🔔 Insulin injection triggered!")

def main():
    print("Starting Continuous Glucose Monitoring System...")
    
    while True:
        glucose_level = simulate_glucose_reading()
        print(f"🩸 Glucose Level: {glucose_level} mg/dL")

        send_to_blynk(VIRTUAL_PIN_GLUCOSE, glucose_level)

        if glucose_level > GLUCOSE_THRESHOLD:
            print("⚠️ High Glucose Detected!")
            send_to_blynk(VIRTUAL_PIN_ALERT, 1)  
            trigger_insulin_injector()
        else:
            send_to_blynk(VIRTUAL_PIN_ALERT, 0) 

        time.sleep(10) 

if __name__ == '__main__':
    main()

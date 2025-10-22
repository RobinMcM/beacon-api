"""
Test script to simulate beacon HTTP messages
Run this to test the API without a real beacon
"""

import requests
import time
import random
from datetime import datetime

# API endpoint
API_URL = "http://localhost:5000/beacon/data"

def send_beacon_data():
    """Simulate sending data from a beacon"""
    
    # Simulate sensor data
    data = {
        "beacon_id": f"BEACON-{random.randint(1, 3):03d}",
        "message_type": "sensor_reading",
        "temperature": round(random.uniform(18.0, 28.0), 1),
        "humidity": round(random.uniform(30.0, 70.0), 1),
        "battery_level": random.randint(60, 100),
        "signal_strength": random.randint(-80, -40),
        "timestamp": datetime.utcnow().isoformat()
    }
    
    try:
        response = requests.post(API_URL, json=data, timeout=5)
        
        if response.status_code == 201:
            print(f"✅ Data sent successfully: {data['beacon_id']} - Temp: {data['temperature']}°C")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Is the API running on localhost:5000?")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def main():
    """Main function to run the test"""
    print("=" * 50)
    print("Beacon Simulator - Testing API")
    print("=" * 50)
    print(f"API URL: {API_URL}")
    print("Press Ctrl+C to stop\n")
    
    # Check if API is healthy
    try:
        health_response = requests.get("http://localhost:5000/health", timeout=5)
        if health_response.status_code == 200:
            print("✅ API is healthy and running\n")
        else:
            print("⚠️ API returned unexpected status\n")
    except:
        print("❌ Cannot connect to API. Please start the API first with: python app.py\n")
        return
    
    # Send test messages
    try:
        message_count = 0
        while True:
            message_count += 1
            print(f"\n--- Message #{message_count} ---")
            send_beacon_data()
            
            # Wait 5 seconds between messages
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\n\n✋ Stopped by user")
        print(f"Total messages sent: {message_count}")

if __name__ == "__main__":
    main()

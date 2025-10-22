# Beacon Data Collection API - Proof of Concept

A simple Flask-based REST API that receives HTTP messages from WiFi/Bluetooth beacons and stores them in Supabase.

## Features

- ✅ REST API endpoint to receive beacon data via HTTP POST
- ✅ Automatic data storage in Supabase (PostgreSQL)
- ✅ Timestamp tracking (both beacon time and server receipt time)
- ✅ Source IP logging for debugging
- ✅ Health check endpoint
- ✅ Optional data retrieval endpoint
- ✅ Error handling and logging

## Prerequisites

- Python 3.8 or higher
- Supabase account (free tier works fine)
- WiFi-enabled beacon that can send HTTP POST requests

## Setup Instructions

### 1. Clone/Download the Project

```bash
cd beacon_api
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Supabase

1. Go to [supabase.com](https://supabase.com) and create a free account
2. Create a new project
3. Go to **SQL Editor** and run the `schema.sql` file to create the database table
4. Go to **Project Settings** → **API** and copy:
   - Project URL
   - `anon/public` key

### 5. Configure Environment Variables

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your Supabase credentials:
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key-here
PORT=5000
```

### 6. Run the API

```bash
python app.py
```

The API will start on `http://localhost:5000`

## API Endpoints

### 1. Health Check
```
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-10-22T10:30:00"
}
```

### 2. Receive Beacon Data
```
POST /beacon/data
Content-Type: application/json
```

**Example Request Body:**
```json
{
  "beacon_id": "BEACON-001",
  "message_type": "sensor_reading",
  "temperature": 22.5,
  "humidity": 45.2,
  "battery_level": 85,
  "signal_strength": -65
}
```

**Response:**
```json
{
  "success": true,
  "message": "Data received and stored",
  "id": 123
}
```

### 3. Retrieve Beacon Data (Optional)
```
GET /beacon/data?limit=10
```

**Response:**
```json
{
  "success": true,
  "count": 10,
  "data": [...]
}
```

## Testing the API

### Using cURL

```bash
# Health check
curl http://localhost:5000/health

# Send beacon data
curl -X POST http://localhost:5000/beacon/data \
  -H "Content-Type: application/json" \
  -d '{
    "beacon_id": "BEACON-001",
    "temperature": 23.5,
    "humidity": 50,
    "battery_level": 90
  }'

# Retrieve data
curl http://localhost:5000/beacon/data?limit=5
```

### Using Python

```python
import requests

# Send beacon data
data = {
    "beacon_id": "BEACON-001",
    "temperature": 23.5,
    "humidity": 50,
    "battery_level": 90,
    "signal_strength": -60
}

response = requests.post(
    'http://localhost:5000/beacon/data',
    json=data
)

print(response.json())
```

## Configuring Your Beacon

Configure your beacon's HTTP settings to:
- **URL**: `http://your-server-ip:5000/beacon/data`
- **Method**: POST
- **Content-Type**: application/json
- **Body**: JSON payload with your sensor data

Example beacon configuration (varies by manufacturer):
```
HTTP POST URL: http://192.168.1.100:5000/beacon/data
Interval: 60 seconds
Payload: {"beacon_id":"${DEVICE_ID}","temperature":${TEMP},"battery":${BATTERY}}
```

## Deployment Options

### Option 1: Deploy to Render (Free)

1. Create account at [render.com](https://render.com)
2. Create new Web Service
3. Connect your Git repository
4. Set environment variables in Render dashboard
5. Deploy!

### Option 2: Deploy to Railway (Free)

1. Create account at [railway.app](https://railway.app)
2. New Project → Deploy from GitHub
3. Add environment variables
4. Deploy!

### Option 3: Deploy to Heroku

```bash
# Install Heroku CLI and login
heroku login

# Create app
heroku create your-beacon-api

# Set environment variables
heroku config:set SUPABASE_URL=your_url
heroku config:set SUPABASE_KEY=your_key

# Deploy
git push heroku main
```

### Option 4: Run on Raspberry Pi

Perfect for local network deployments:

```bash
# Install and run
pip install -r requirements.txt
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Database Schema

The `beacon_messages` table stores:
- `id`: Auto-incrementing primary key
- `beacon_id`: Identifier for the beacon
- `message_type`: Type of message/reading
- `payload`: Flexible JSONB field for any data
- `temperature`, `humidity`, `battery_level`, `signal_strength`: Common sensor fields
- `received_at`: When the API received the message
- `source_ip`: IP address of the beacon
- `created_at`: Database insertion timestamp

You can customize the schema in `schema.sql` to match your beacon's data format.

## Viewing Data in Supabase

1. Log into Supabase
2. Go to **Table Editor**
3. Select `beacon_messages` table
4. View all received beacon data in real-time

## Troubleshooting

### Connection Errors
- Verify Supabase credentials in `.env`
- Check if Supabase project is active
- Ensure internet connection

### Beacon Not Sending Data
- Verify beacon HTTP URL is correct
- Check beacon is connected to WiFi
- Review beacon logs for errors
- Test with cURL first to ensure API works

### Port Already in Use
- Change PORT in `.env` file
- Or kill the process using the port

## Security Considerations

For production use, consider:
- Adding API authentication (API keys, JWT tokens)
- Implementing rate limiting
- Using HTTPS (SSL/TLS)
- Restricting Supabase RLS policies
- Validating beacon data more strictly
- Using environment-specific configurations

## Next Steps

To enhance this POC:
1. Add authentication/API keys
2. Implement data validation and sanitization
3. Add real-time notifications (webhooks, email alerts)
4. Create a dashboard to visualize beacon data
5. Add support for multiple beacon types
6. Implement data aggregation and analytics
7. Add automated alerts for threshold violations

## License

MIT License - Free to use and modify for your projects.

## Support

For issues or questions, please check:
- Flask documentation: [flask.palletsprojects.com](https://flask.palletsprojects.com)
- Supabase documentation: [supabase.com/docs](https://supabase.com/docs)

# Beacon Data Collection System - Project Overview

## What This System Does

This is a complete proof-of-concept system that:
1. Receives HTTP messages from WiFi/Bluetooth beacons
2. Stores the data in Supabase (cloud PostgreSQL database)
3. Provides a simple REST API for data retrieval

## Architecture

```
┌─────────────┐         HTTP POST          ┌──────────────┐
│             │  ────────────────────────>  │              │
│   Beacon    │   (WiFi, every X seconds)  │  Flask API   │
│             │  <────────────────────────  │              │
└─────────────┘      200 OK Response       └──────┬───────┘
                                                   │
                                                   │ Store Data
                                                   ▼
                                            ┌──────────────┐
                                            │   Supabase   │
                                            │  (Database)  │
                                            └──────────────┘
```

## Files Included

### Core Application
- **app.py** - Main Flask API server with endpoints
- **requirements.txt** - Python dependencies
- **schema.sql** - Database table creation script

### Configuration
- **.env.example** - Template for environment variables
- **.gitignore** - Git ignore rules for security

### Documentation
- **README.md** - Complete documentation with all details
- **QUICKSTART.md** - Fast 5-minute setup guide
- **PROJECT_OVERVIEW.md** - This file

### Testing & Deployment
- **test_beacon.py** - Beacon simulator for testing
- **Dockerfile** - Container deployment option

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/health` | GET | Check if API is running |
| `/beacon/data` | POST | Receive beacon messages |
| `/beacon/data?limit=N` | GET | Retrieve stored messages |

## Data Flow

1. **Beacon sends data** → HTTP POST to `/beacon/data`
2. **API receives data** → Validates JSON payload
3. **API enriches data** → Adds timestamp & source IP
4. **API stores data** → Inserts into Supabase table
5. **API responds** → Returns success/error message

## Database Schema

The `beacon_messages` table includes:
- Standard fields: id, timestamps, source IP
- Sensor fields: temperature, humidity, battery, signal strength
- Flexible field: JSONB payload for any custom data

## Key Features

✅ **Flexible Data Structure** - JSONB field accepts any beacon format
✅ **Automatic Timestamps** - Tracks when data was received
✅ **Source Tracking** - Logs beacon IP addresses
✅ **Error Handling** - Comprehensive logging and error responses
✅ **Test Mode** - Includes simulator to test without real beacon
✅ **Cloud Ready** - Easy deployment to Render, Railway, Heroku
✅ **Container Ready** - Includes Dockerfile for Docker deployment

## Technology Stack

- **Backend**: Python Flask (lightweight, perfect for APIs)
- **Database**: Supabase (managed PostgreSQL with real-time)
- **Deployment**: Multiple options (local, cloud, container)
- **Testing**: Python requests library

## Security Notes (For Production)

This POC is intentionally simple. For production:
- Add API authentication (API keys, JWT)
- Implement rate limiting
- Use HTTPS/SSL
- Add input validation and sanitization
- Configure Supabase Row Level Security (RLS)
- Add monitoring and alerting

## Typical Use Cases

1. **IoT Sensor Monitoring** - Temperature, humidity, motion sensors
2. **Asset Tracking** - Location beacons in warehouses
3. **Environmental Monitoring** - Air quality, CO2 sensors
4. **Occupancy Detection** - Room/space utilization
5. **Condition Monitoring** - Equipment health monitoring

## Getting Started

Choose your path:

**Fast Track** (5 minutes):
→ Follow `QUICKSTART.md`

**Complete Setup**:
→ Follow `README.md`

**Just Test It**:
1. `pip install flask supabase python-dotenv`
2. Configure Supabase in `.env`
3. `python app.py`
4. In another terminal: `python test_beacon.py`

## Customization Points

To adapt for your beacon:

1. **Payload Format**: Modify the JSON structure in POST body
2. **Database Fields**: Update `schema.sql` with your fields
3. **Validation**: Add checks in `app.py` for required fields
4. **Processing**: Add data transformation logic before storage
5. **Notifications**: Add webhooks or email alerts for events

## Cost Estimate

- **Supabase**: Free tier (500MB database, 50,000 monthly requests)
- **Deployment**: 
  - Local: Free
  - Render/Railway: Free tier available
  - Heroku: $5-7/month
- **Beacons**: Varies by model ($10-$100 each)

Total: **Can run entirely free for POC!**

## Next Steps

1. ✅ Set up the API (you have everything)
2. Configure your beacon to POST to the API
3. View data in Supabase dashboard
4. Build a visualization dashboard (optional)
5. Deploy to production hosting (optional)
6. Add authentication and monitoring (production)

## Support Resources

- Flask: https://flask.palletsprojects.com
- Supabase: https://supabase.com/docs
- Python Requests: https://requests.readthedocs.io

## License

MIT License - Feel free to use and modify for your projects!

---

**Created**: October 2025
**Purpose**: Proof of Concept for Beacon Data Collection
**Status**: Ready to deploy and test

# Quick Start Guide

Get your beacon API running in 5 minutes!

## Step 1: Install Python Dependencies

```bash
pip install flask supabase python-dotenv gunicorn
```

## Step 2: Set Up Supabase (2 minutes)

1. Go to https://supabase.com and sign up (free)
2. Create a new project (wait ~2 minutes for setup)
3. Click **SQL Editor** (left sidebar)
4. Copy and paste the contents of `schema.sql`
5. Click **Run**
6. Go to **Settings** → **API**
7. Copy the **Project URL** and **anon public** key

## Step 3: Configure Environment

Create a file named `.env` with:

```
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_KEY=your_anon_key_here
PORT=5000
```

## Step 4: Run the API

```bash
python app.py
```

You should see:
```
* Running on http://0.0.0.0:5000
```

## Step 5: Test It

Open a new terminal and run:

```bash
python test_beacon.py
```

You should see messages being sent every 5 seconds!

## Step 6: View Your Data

1. Go back to Supabase
2. Click **Table Editor** (left sidebar)
3. Click on `beacon_messages` table
4. See your data appearing in real-time! 🎉

## Configure Your Real Beacon

In your beacon's HTTP settings:
- **URL**: `http://YOUR_IP_ADDRESS:5000/beacon/data`
- **Method**: POST
- **Content-Type**: application/json

Example payload format:
```json
{
  "beacon_id": "BEACON-001",
  "temperature": 23.5,
  "humidity": 50,
  "battery_level": 85
}
```

## Need Help?

Check the full `README.md` for:
- Deployment options (Render, Railway, Heroku)
- Security considerations
- Advanced configuration
- Troubleshooting

## What's Next?

- Add authentication (API keys)
- Deploy to the cloud
- Create a dashboard
- Set up alerts

Happy beacon tracking! 📡

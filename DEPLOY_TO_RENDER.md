# Deploy Beacon API to Render.com - Complete Guide

This guide will walk you through deploying your beacon API to Render.com for **FREE**. Your API will be live on the internet with a public URL!

---

## 📋 Prerequisites

- [ ] GitHub account (free) - [Sign up here](https://github.com/signup)
- [ ] Render account (free) - [Sign up here](https://render.com/register)
- [ ] Supabase account with project set up
- [ ] Your beacon API files (you already have these!)

**Time Required:** 10-15 minutes

---

## Part 1: Prepare for GitHub (5 minutes)

### Step 1: Create a GitHub Account
1. Go to [github.com/signup](https://github.com/signup)
2. Enter your email, password, and username
3. Verify your email address

### Step 2: Create a New Repository
1. Go to [github.com/new](https://github.com/new)
2. Fill in the details:
   - **Repository name:** `beacon-data-api` (or your preferred name)
   - **Description:** `API to receive and store beacon data in Supabase`
   - **Visibility:** Choose **Public** or **Private** (both work)
   - **DO NOT** check "Add a README" (we already have one)
3. Click **"Create repository"**

### Step 3: Upload Your Code to GitHub

**Option A: Using GitHub Web Interface (Easiest)**

1. On your new repository page, click **"uploading an existing file"**
2. Drag and drop ALL these files from your `beacon_api` folder:
   ```
   - app.py
   - requirements.txt
   - schema.sql
   - .gitignore
   - Dockerfile
   - docker-compose.yml
   - render.yaml
   - README.md
   - QUICKSTART.md
   - PROJECT_OVERVIEW.md
   - DEPLOY_TO_RENDER.md (this file)
   - test_beacon.py
   ```
3. **IMPORTANT:** Do NOT upload `.env` file (it contains secrets!)
4. Add commit message: "Initial commit"
5. Click **"Commit changes"**

**Option B: Using Git Command Line**

```bash
# Navigate to your beacon_api folder
cd beacon_api

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit"

# Connect to GitHub (replace YOUR-USERNAME and YOUR-REPO)
git remote add origin https://github.com/YOUR-USERNAME/beacon-data-api.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Part 2: Get Your Supabase Credentials (2 minutes)

Before deploying, you need your Supabase credentials:

### Step 1: Log into Supabase
1. Go to [supabase.com](https://supabase.com)
2. Click on your project

### Step 2: Get API Credentials
1. Click **⚙️ Settings** (bottom left)
2. Click **API** in the sidebar
3. Copy these two values (you'll need them soon):
   - **Project URL** (looks like: `https://abcdefgh.supabase.co`)
   - **anon/public key** (long string starting with `eyJ...`)

### Step 3: Set Up Database Table
1. Click **🗄️ SQL Editor** (left sidebar)
2. Click **New query**
3. Copy the contents of your `schema.sql` file
4. Paste into the editor
5. Click **Run**
6. You should see: "Success. No rows returned"

---

## Part 3: Deploy to Render.com (5 minutes)

### Step 1: Create Render Account
1. Go to [render.com/register](https://render.com/register)
2. Sign up with **GitHub** (click "Sign up with GitHub")
3. Authorize Render to access your GitHub

### Step 2: Create a New Web Service
1. Click **"New +"** button (top right)
2. Select **"Web Service"**
3. Click **"Connect" to GitHub**
4. Find and select your `beacon-data-api` repository
5. Click **"Connect"**

### Step 3: Configure the Web Service

Fill in these settings:

**Basic Settings:**
- **Name:** `beacon-api` (or your preferred name)
- **Region:** Choose closest to you (e.g., Oregon, Frankfurt)
- **Branch:** `main`
- **Root Directory:** Leave blank
- **Runtime:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`

**Instance Type:**
- Select **"Free"** (this gives you 750 hours/month for free!)

### Step 4: Add Environment Variables

Scroll down to **"Environment Variables"** section:

1. Click **"Add Environment Variable"**
2. Add these variables:

| Key | Value |
|-----|-------|
| `SUPABASE_URL` | Your Supabase Project URL |
| `SUPABASE_KEY` | Your Supabase anon/public key |
| `PYTHON_VERSION` | `3.11.0` |

**How to add each variable:**
- Click "Add Environment Variable"
- Enter the Key name
- Paste the Value
- Click outside to save

### Step 5: Deploy!

1. Scroll to the bottom
2. Click **"Create Web Service"**
3. Wait 2-5 minutes while Render builds and deploys

You'll see logs like:
```
==> Building...
==> Installing dependencies...
==> Starting service...
==> Your service is live! 🎉
```

### Step 6: Get Your API URL

1. Once deployed, you'll see: **"Your service is live"**
2. At the top, you'll see your URL: `https://beacon-api-xxxx.onrender.com`
3. Copy this URL - this is your live API!

---

## Part 4: Test Your Live API (2 minutes)

### Test 1: Health Check

Open your browser and visit:
```
https://your-api-name.onrender.com/health
```

You should see:
```json
{
  "status": "healthy",
  "timestamp": "2025-10-22T12:00:00"
}
```

✅ If you see this, your API is working!

### Test 2: Send Test Data

Open terminal and run:

```bash
curl -X POST https://your-api-name.onrender.com/beacon/data \
  -H "Content-Type: application/json" \
  -d '{
    "beacon_id": "TEST-001",
    "temperature": 22.5,
    "humidity": 45,
    "battery_level": 85
  }'
```

You should see:
```json
{
  "success": true,
  "message": "Data received and stored",
  "id": 1
}
```

### Test 3: View Data in Supabase

1. Go to Supabase
2. Click **Table Editor**
3. Open `beacon_messages` table
4. You should see your test data! 🎉

---

## Part 5: Configure Your Beacon

Now configure your physical beacon:

**Beacon HTTP Settings:**
- **URL:** `https://your-api-name.onrender.com/beacon/data`
- **Method:** POST
- **Content-Type:** application/json
- **Interval:** 60 seconds (or your preference)

**Example Payload Format:**
```json
{
  "beacon_id": "BEACON-001",
  "temperature": 23.5,
  "humidity": 50,
  "battery_level": 90
}
```

---

## 🎉 Success! Your API is Live!

Your beacon API is now:
- ✅ Live on the internet
- ✅ Auto-deployed from GitHub
- ✅ Connected to Supabase
- ✅ Ready to receive beacon data
- ✅ Free (Render free tier)

**Your API URL:** `https://your-api-name.onrender.com`

---

## Important Notes

### Free Tier Limitations
- **750 hours/month** of uptime (enough for 24/7 with one service)
- **Sleeps after 15 minutes** of inactivity
- **Cold start:** First request after sleep takes 30-60 seconds
- To prevent sleeping: Set up a cron job to ping `/health` every 10 minutes

### Prevent Cold Starts (Optional)

Use a free service like [cron-job.org](https://cron-job.org):
1. Sign up for free
2. Create a new cron job
3. URL: `https://your-api-name.onrender.com/health`
4. Schedule: Every 10 minutes
5. Your API will stay awake!

---

## Updating Your Code

When you want to update your code:

**Option 1: GitHub Web Interface**
1. Go to your repository on GitHub
2. Click on the file you want to edit
3. Click the pencil icon (Edit)
4. Make changes
5. Click "Commit changes"
6. Render will auto-deploy in 2-3 minutes!

**Option 2: Git Command Line**
```bash
# Make your changes to files
# Then:
git add .
git commit -m "Description of changes"
git push
```

Render automatically detects changes and redeploys!

---

## Monitoring Your API

### View Logs in Render
1. Go to Render dashboard
2. Click on your service
3. Click **"Logs"** tab
4. See real-time logs of all requests

### View Data in Supabase
1. Go to Supabase
2. Click **Table Editor**
3. View all beacon messages in real-time

---

## Troubleshooting

### "Build Failed" Error
- Check that `requirements.txt` is in root directory
- Verify all files were uploaded to GitHub
- Check Render logs for specific error

### "Service Unavailable" Error
- API might be sleeping (free tier)
- Wait 30 seconds and try again
- Or set up cron job to keep it awake

### "Cannot connect to Supabase" Error
- Verify environment variables are correct
- Check SUPABASE_URL has no trailing slash
- Verify SUPABASE_KEY is the anon/public key

### Beacon Not Sending Data
- Verify beacon URL is correct
- Check beacon is connected to internet
- Test with curl first to verify API works
- Check Render logs for incoming requests

---

## Upgrade Options

### Render Paid Plans
If you outgrow the free tier:
- **Starter:** $7/month (no sleeping, faster performance)
- **Standard:** $25/month (more resources, better uptime)

### Keep It Free
The free tier is actually quite generous for beacon monitoring:
- Can handle dozens of beacons
- 750 hours = 31 days of 24/7 uptime
- Perfect for POCs and small deployments

---

## Next Steps

Now that your API is live:

1. ✅ Configure your beacon to send data
2. ✅ Monitor data in Supabase
3. 📊 Build a dashboard to visualize data (optional)
4. 🔐 Add API authentication for production (recommended)
5. 📧 Set up email alerts for critical events (optional)
6. 📈 Add data analytics and reporting (optional)

---

## Support

- **Render Docs:** [render.com/docs](https://render.com/docs)
- **Supabase Docs:** [supabase.com/docs](https://supabase.com/docs)
- **Flask Docs:** [flask.palletsprojects.com](https://flask.palletsprojects.com)

---

## Summary

✅ Code on GitHub
✅ API live on Render.com
✅ Data stored in Supabase
✅ Free hosting
✅ Auto-deploys on code changes

**You're all set! Happy beacon monitoring! 📡**

# 🚀 Quick Deployment Checklist

Use this checklist to track your deployment progress:

## Before You Start

- [ ] I have a GitHub account
- [ ] I have a Render account  
- [ ] I have a Supabase account
- [ ] I have my Supabase credentials ready

---

## Step 1: GitHub Setup ✓

- [ ] Created GitHub repository
- [ ] Uploaded all project files
- [ ] Verified files are visible on GitHub
- [ ] Did NOT upload `.env` file

---

## Step 2: Supabase Setup ✓

- [ ] Logged into Supabase
- [ ] Ran `schema.sql` in SQL Editor
- [ ] Table `beacon_messages` created successfully
- [ ] Copied Project URL
- [ ] Copied anon/public API key

---

## Step 3: Render Deployment ✓

- [ ] Created Render account
- [ ] Connected GitHub repository
- [ ] Selected "Web Service"
- [ ] Set runtime to Python 3
- [ ] Added build command: `pip install -r requirements.txt`
- [ ] Added start command: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`
- [ ] Selected "Free" plan
- [ ] Added environment variable: `SUPABASE_URL`
- [ ] Added environment variable: `SUPABASE_KEY`
- [ ] Added environment variable: `PYTHON_VERSION` = `3.11.0`
- [ ] Clicked "Create Web Service"
- [ ] Wait for deployment (2-5 minutes)

---

## Step 4: Testing ✓

- [ ] Visited `/health` endpoint in browser
- [ ] Received healthy status response
- [ ] Sent test POST request with curl
- [ ] Received success response
- [ ] Verified data appears in Supabase table

---

## Step 5: Configure Beacon ✓

- [ ] Copied API URL from Render
- [ ] Configured beacon HTTP URL
- [ ] Set beacon to POST method
- [ ] Set Content-Type to application/json
- [ ] Tested beacon sending data
- [ ] Verified data received in Supabase

---

## 🎉 All Done!

Your API is live at: `https://your-api-name.onrender.com`

### Quick Reference URLs

- **Your API URL:** _______________________________
- **GitHub Repo:** _______________________________
- **Supabase Project:** _______________________________
- **Render Dashboard:** https://dashboard.render.com

---

## Common Issues

### ❌ Build Failed
→ Check `requirements.txt` is in repository root
→ Review Render build logs for errors

### ❌ Service Error
→ Verify environment variables are set correctly
→ Check Supabase credentials are correct

### ❌ Beacon Not Connecting
→ Ensure beacon has internet access
→ Verify URL has no typos
→ Check beacon is set to POST method

---

## Need Help?

📖 Full guide: See `DEPLOY_TO_RENDER.md`
📧 Render support: support@render.com
💬 Supabase support: https://supabase.com/support

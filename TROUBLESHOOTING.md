# 🔧 Troubleshooting Guide

Having issues? This guide covers the most common problems and their solutions.

---

## GitHub Issues

### ❌ "Repository name already exists"

**Problem:** You already have a repository with that name.

**Solutions:**
1. Choose a different name (e.g., `beacon-api-v2`)
2. Or delete the existing repository:
   - Go to repository → Settings → scroll to bottom
   - Click "Delete this repository"
   - Type the repository name to confirm

---

### ❌ Files not showing up on GitHub

**Problem:** Files uploaded but not visible.

**Solutions:**
1. Refresh the page (Ctrl+R or Cmd+R)
2. Make sure you clicked "Commit changes"
3. Check you're looking at the correct repository
4. Try uploading again, fewer files at a time

---

### ❌ Accidentally uploaded .env file

**Problem:** Your secrets are visible publicly!

**URGENT Solutions:**
1. **Immediately** delete the file from GitHub:
   - Click on `.env` file
   - Click trash icon
   - Commit deletion
2. Go to Supabase:
   - Project Settings → API
   - Service Keys section
   - Click "Reset" to regenerate keys
3. Update your local `.env` with new keys
4. **Never** commit `.env` again (`.gitignore` prevents this)

---

## Supabase Issues

### ❌ "Cannot connect to Supabase"

**Problem:** API can't reach Supabase database.

**Solutions:**
1. Check environment variables in Render:
   - Go to Render dashboard
   - Your service → Environment
   - Verify `SUPABASE_URL` and `SUPABASE_KEY` are set
2. Verify URL format:
   - Should be: `https://xxxxx.supabase.co`
   - No trailing slash!
   - No `/rest/v1` at the end
3. Verify you're using the **anon/public** key:
   - NOT the service_role key
   - NOT the JWT secret

---

### ❌ "Table 'beacon_messages' does not exist"

**Problem:** Database table not created.

**Solutions:**
1. Go to Supabase → SQL Editor
2. Copy contents of `schema.sql`
3. Paste and click "Run"
4. Should see: "Success. No rows returned"
5. Go to Table Editor - you should see `beacon_messages` table

---

### ❌ "Row Level Security policy violation"

**Problem:** Supabase RLS is blocking inserts.

**Solutions:**
1. Go to Supabase → Authentication → Policies
2. Find `beacon_messages` table
3. Click "New Policy"
4. Choose "Enable insert for authenticated users"
5. Or temporarily disable RLS:
   ```sql
   ALTER TABLE beacon_messages DISABLE ROW LEVEL SECURITY;
   ```
   (Not recommended for production!)

---

## Render Deployment Issues

### ❌ "Build failed"

**Problem:** Render can't build your application.

**Common Causes & Solutions:**

**1. Missing requirements.txt**
- Verify `requirements.txt` is in repository root
- Check it contains:
  ```
  flask==3.0.0
  supabase==2.3.4
  python-dotenv==1.0.0
  gunicorn==21.2.0
  ```

**2. Wrong Python version**
- Add environment variable:
  - Key: `PYTHON_VERSION`
  - Value: `3.11.0`

**3. Syntax errors in code**
- Check Render logs for error message
- Fix the error in your code
- Push changes to GitHub

**4. Missing files**
- Ensure `app.py` is uploaded
- Check all imports in `app.py` are installed

**View Build Logs:**
- Render dashboard → Your service → Logs tab
- Look for red error messages

---

### ❌ "Service unavailable" or "Application Error"

**Problem:** App built but won't start.

**Solutions:**

**1. Check environment variables:**
```bash
# Required variables:
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_KEY=eyJhbGc...
PYTHON_VERSION=3.11.0
```

**2. Verify start command:**
Should be: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`

**3. Check logs:**
- Render dashboard → Logs
- Look for Python errors
- Common issues:
  - Missing environment variables
  - Import errors
  - Supabase connection failed

**4. Cold start (Free tier):**
- Free tier sleeps after 15 minutes
- First request takes 30-60 seconds
- Wait and try again
- Or set up keep-alive ping

---

### ❌ "Deploy hook failed"

**Problem:** Auto-deployment from GitHub failed.

**Solutions:**
1. Check GitHub repository is accessible
2. Verify branch name is correct (usually `main`)
3. Re-connect GitHub:
   - Render dashboard → Account Settings
   - Connected Accounts → Reconnect GitHub
4. Manual deploy:
   - Render dashboard → Your service
   - Click "Manual Deploy" → "Deploy latest commit"

---

### ❌ "Port binding failed"

**Problem:** App can't bind to port.

**Solution:**
- Start command MUST use `$PORT` variable
- Correct: `gunicorn -b 0.0.0.0:$PORT app:app`
- Wrong: `gunicorn -b 0.0.0.0:5000 app:app`

---

## API Issues

### ❌ 404 Not Found on /beacon/data

**Problem:** Endpoint doesn't exist.

**Solutions:**
1. Verify URL is correct:
   - `https://your-app.onrender.com/beacon/data`
   - Not `/beacon-data` or `/beacondata`
2. Check app.py has the route defined
3. Try the health check first: `/health`

---

### ❌ 400 Bad Request

**Problem:** Invalid data sent to API.

**Solutions:**
1. Verify JSON format:
   ```json
   {
     "beacon_id": "BEACON-001",
     "temperature": 22.5
   }
   ```
2. Check Content-Type header:
   - Must be: `application/json`
3. Verify JSON is valid:
   - Use [jsonlint.com](https://jsonlint.com) to validate

---

### ❌ 500 Internal Server Error

**Problem:** Something crashed in the API.

**Solutions:**
1. Check Render logs for Python error
2. Common causes:
   - Supabase credentials wrong
   - Table doesn't exist
   - Database connection failed
3. Test locally first:
   ```bash
   python app.py
   # Then test with curl
   ```

---

### ❌ Request times out

**Problem:** Request takes too long or never completes.

**Solutions:**
1. **Cold start** (free tier):
   - First request after sleep takes 30-60s
   - Be patient, try again
2. **Supabase slow:**
   - Check Supabase status page
   - May be overloaded
3. **Request too large:**
   - Keep payloads under 10MB

---

## Beacon Issues

### ❌ Beacon not sending data

**Problem:** No data appearing in Supabase.

**Solutions:**

**1. Verify beacon configuration:**
- URL must be exact: `https://your-app.onrender.com/beacon/data`
- Method: POST (not GET)
- Content-Type: application/json

**2. Check beacon internet connection:**
- Can it reach the internet?
- Try pinging google.com from beacon
- Check WiFi credentials

**3. Check beacon logs:**
- Most beacons have a log viewer
- Look for HTTP errors (404, 500, etc.)
- Look for connection errors

**4. Test API manually first:**
```bash
curl -X POST https://your-app.onrender.com/beacon/data \
  -H "Content-Type: application/json" \
  -d '{"beacon_id":"TEST","temp":22}'
```

If curl works but beacon doesn't → beacon configuration issue

**5. Check Render logs:**
- Do requests appear in logs?
- If yes: API receiving but may be failing to save
- If no: Beacon isn't reaching API

---

### ❌ Beacon sends data but nothing in Supabase

**Problem:** API receives data but doesn't save it.

**Solutions:**
1. Check Render logs:
   - Look for "Data saved to Supabase successfully"
   - If missing, check for errors
2. Verify Supabase credentials in Render environment variables
3. Check Supabase table:
   - Go to Table Editor
   - Verify table exists
   - Check RLS policies aren't blocking inserts

---

## Testing Issues

### ❌ test_beacon.py won't run

**Problem:** Test script fails to start.

**Solutions:**

**1. API not running:**
```bash
# Start API first:
python app.py

# Then in another terminal:
python test_beacon.py
```

**2. Missing dependencies:**
```bash
pip install requests
```

**3. Wrong URL:**
- Edit `test_beacon.py`
- Change `API_URL` to your Render URL

---

### ❌ curl command not found

**Problem:** curl isn't installed.

**Solutions:**

**Windows:**
- Comes with Windows 10+ (use PowerShell)
- Or use Git Bash
- Or install from [curl.se](https://curl.se)

**Mac:**
- Pre-installed
- If missing: `brew install curl`

**Alternative - use Python:**
```python
import requests
response = requests.post(
    'https://your-app.onrender.com/beacon/data',
    json={'beacon_id': 'TEST', 'temp': 22}
)
print(response.json())
```

---

## Performance Issues

### ❌ API is very slow

**Problem:** Responses take a long time.

**Causes & Solutions:**

**1. Cold start (Free tier):**
- Expected on first request after 15min inactivity
- Solution: Upgrade to paid tier or set up keep-alive

**2. Supabase in different region:**
- Choose Render region close to Supabase
- Both should be in same continent

**3. Large payloads:**
- Keep beacon data under 1KB per message
- Don't send images or large files

**4. Database query slow:**
- Add indexes (already included in schema.sql)
- Limit query results

---

### ❌ Too many requests failing

**Problem:** Rate limiting or overload.

**Solutions:**
1. Check Render free tier limits:
   - 750 hours/month
   - 100 GB bandwidth
2. Reduce beacon message frequency:
   - Don't send more than 1 message/second per beacon
3. Implement retry logic in beacon
4. Consider upgrading Render plan

---

## Environment Variable Issues

### ❌ Environment variables not working

**Problem:** API can't read env vars.

**Solutions:**

**In Render:**
1. Dashboard → Your service → Environment
2. Add variables one by one
3. Click "Save Changes"
4. Redeploy if necessary

**Variable format:**
```
SUPABASE_URL=https://xxxxx.supabase.co
```
- No quotes
- No spaces around =
- No trailing slash in URL

---

## Getting More Help

### Check Logs First!

**Render Logs:**
1. Render dashboard → Your service
2. Click "Logs" tab
3. Look for red errors
4. Most recent logs at bottom

**Supabase Logs:**
1. Supabase dashboard → Your project
2. Click "Logs" (left sidebar)
3. Filter by "API" or "Database"

### Still Stuck?

**Option 1: Community Support**
- Render Community: [community.render.com](https://community.render.com)
- Supabase Discord: [discord.supabase.com](https://discord.supabase.com)
- Stack Overflow: Tag with `flask`, `supabase`, `render`

**Option 2: Documentation**
- Render Docs: [render.com/docs](https://render.com/docs)
- Supabase Docs: [supabase.com/docs](https://supabase.com/docs)
- Flask Docs: [flask.palletsprojects.com](https://flask.palletsprojects.com)

**Option 3: Contact Support**
- Render: support@render.com
- Supabase: [supabase.com/support](https://supabase.com/support)

### When Asking for Help

Include this information:
1. What you're trying to do
2. What error message you see
3. Relevant logs from Render/Supabase
4. What you've already tried
5. Your setup (OS, Python version, etc.)

---

## Quick Diagnostic Checklist

Run through this when something's wrong:

- [ ] Is GitHub repository updated with latest code?
- [ ] Did Render deployment succeed? (check logs)
- [ ] Are environment variables set correctly in Render?
- [ ] Does `/health` endpoint return 200 OK?
- [ ] Can you connect to Supabase from your local machine?
- [ ] Does the `beacon_messages` table exist in Supabase?
- [ ] Are Supabase credentials correct?
- [ ] Is the beacon connected to internet?
- [ ] Is the beacon URL exactly correct?
- [ ] Can you successfully POST with curl?

---

**Most issues are caused by:**
1. ❌ Wrong environment variables (50%)
2. ❌ Missing database table (20%)
3. ❌ Incorrect beacon configuration (15%)
4. ❌ Cold start confusion (10%)
5. ❌ Other (5%)

**Check these first!**

# Deploy in 3 Steps (10 Minutes)

## Step 1: GitHub (3 min)
1. Create account at [github.com](https://github.com/signup)
2. Click "New repository" → Name it `beacon-api`
3. Upload all files (drag & drop) - **EXCEPT .env**
4. Click "Commit changes"

✅ **Done!** Your code is on GitHub

---

## Step 2: Supabase (3 min)
1. Create account at [supabase.com](https://supabase.com)
2. Create new project (wait 2 min)
3. Go to SQL Editor → paste `schema.sql` → Run
4. Go to Settings → API → copy:
   - Project URL
   - anon/public key

✅ **Done!** Database ready

---

## Step 3: Render (4 min)
1. Create account at [render.com](https://render.com) (sign in with GitHub)
2. Click "New +" → "Web Service"
3. Connect your `beacon-api` repository
4. Settings:
   - Runtime: **Python 3**
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`
   - Plan: **Free**
5. Add Environment Variables:
   - `SUPABASE_URL` = your Supabase URL
   - `SUPABASE_KEY` = your Supabase key
   - `PYTHON_VERSION` = `3.11.0`
6. Click "Create Web Service"
7. Wait 3 minutes for deployment

✅ **Done!** API is live!

---

## Test It

Visit: `https://your-app.onrender.com/health`

See: `{"status": "healthy"}` ✅

---

## Configure Beacon

Point your beacon to:
```
URL: https://your-app.onrender.com/beacon/data
Method: POST
Content-Type: application/json
```

---

## 🎉 Success!

Your beacon data will now flow to Supabase automatically!

**View data:** Supabase → Table Editor → beacon_messages

---

**Need help?** See detailed guides:
- [GITHUB_SETUP.md](GITHUB_SETUP.md) - GitHub help
- [DEPLOY_TO_RENDER.md](DEPLOY_TO_RENDER.md) - Render help
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Fix issues

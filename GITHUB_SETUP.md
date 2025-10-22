# 📁 GitHub Setup Guide for Beginners

If you're new to GitHub, this guide will help you get your beacon API code uploaded in 5 minutes!

---

## What is GitHub?

GitHub is like "Dropbox for code" - it stores your code online and keeps track of all changes. Render.com will automatically pull your code from GitHub and deploy it.

---

## Method 1: Upload via Web (Easiest) ⭐

**No software installation required!**

### Step 1: Create GitHub Account

1. Go to [github.com/signup](https://github.com/signup)
2. Enter your email address
3. Create a password (strong password recommended)
4. Choose a username (this will be public)
5. Complete the verification puzzle
6. Check your email and click the verification link

### Step 2: Create a New Repository

1. After logging in, click the **+** icon (top right corner)
2. Select **"New repository"**
3. Fill in the details:

   **Repository name:** 
   ```
   beacon-data-api
   ```
   (Use lowercase, hyphens allowed, no spaces)

   **Description:** 
   ```
   API to receive and store beacon data in Supabase
   ```

   **Visibility:**
   - Choose **Public** (free, anyone can see it) or
   - Choose **Private** (free, only you can see it)
   
   **Important:** 
   - ❌ Do NOT check "Add a README file"
   - ❌ Do NOT add .gitignore
   - ❌ Do NOT add a license
   
   We already have these files!

4. Click **"Create repository"**

### Step 3: Upload Your Files

After creating the repository, you'll see a page with instructions. Look for the text that says **"uploading an existing file"** and click it.

Now upload these files ONE BY ONE or all at once:

**Files to Upload:**
```
✅ app.py
✅ requirements.txt
✅ schema.sql
✅ render.yaml
✅ Dockerfile
✅ docker-compose.yml
✅ .gitignore
✅ README.md
✅ QUICKSTART.md
✅ PROJECT_OVERVIEW.md
✅ DEPLOY_TO_RENDER.md
✅ DEPLOYMENT_CHECKLIST.md
✅ GITHUB_SETUP.md (this file)
✅ test_beacon.py
```

**Files to NOT Upload:**
```
❌ .env (contains your secrets - never upload this!)
❌ .env.example (optional - this is safe to upload)
```

**How to Upload:**
1. Click "choose your files" or drag files into the box
2. You can select all files at once (Ctrl+A or Cmd+A)
3. Wait for upload to complete (few seconds)
4. At the bottom, add commit message: `Initial commit`
5. Click **"Commit changes"**

### Step 4: Verify Upload

You should now see all your files listed on your repository page:
- app.py
- requirements.txt
- schema.sql
- etc.

✅ **Success!** Your code is now on GitHub!

---

## Method 2: Using GitHub Desktop (Visual)

**For those who prefer a desktop app**

### Step 1: Download GitHub Desktop

1. Go to [desktop.github.com](https://desktop.github.com)
2. Download for your OS (Windows/Mac)
3. Install the application
4. Open GitHub Desktop
5. Sign in with your GitHub account

### Step 2: Create Repository

1. Click **"Create a New Repository"**
2. Name: `beacon-data-api`
3. Local Path: Choose where to save (e.g., Documents)
4. Click **"Create Repository"**

### Step 3: Add Your Files

1. Open the repository folder on your computer
2. Copy all your beacon API files into this folder
3. Return to GitHub Desktop
4. You'll see all files listed on the left
5. Select all files (checkbox)
6. Bottom left: Add commit message: `Initial commit`
7. Click **"Commit to main"**

### Step 4: Publish to GitHub

1. Click **"Publish repository"** (top right)
2. Choose Public or Private
3. Click **"Publish repository"**

✅ **Done!** Your code is on GitHub!

---

## Method 3: Using Command Line (Advanced)

**For developers comfortable with terminal/command prompt**

### Prerequisites
- Git installed ([git-scm.com/downloads](https://git-scm.com/downloads))

### Commands

```bash
# Navigate to your beacon_api folder
cd path/to/beacon_api

# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit"

# Create repository on GitHub first (via web), then:
git remote add origin https://github.com/YOUR-USERNAME/beacon-data-api.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

---

## Verifying Your Repository

After upload, visit:
```
https://github.com/YOUR-USERNAME/beacon-data-api
```

You should see:
- ✅ All your files listed
- ✅ README.md displayed at the bottom
- ✅ Green "Code" button at the top

---

## Important Security Note! 🔒

**NEVER upload your `.env` file to GitHub!**

The `.env` file contains:
- Your Supabase credentials
- API keys
- Secrets

If you accidentally uploaded it:
1. Delete the file from GitHub immediately
2. Go to Supabase and regenerate your API keys
3. Update your `.env` file locally with new keys

The `.gitignore` file prevents this automatically!

---

## Common Issues

### Issue: "Repository name already exists"
**Solution:** Choose a different name or delete the existing repository

### Issue: "Can't see my files on GitHub"
**Solution:** 
- Make sure you clicked "Commit changes"
- Refresh the GitHub page
- Check you're on the correct repository

### Issue: "Upload failed"
**Solution:**
- Check your internet connection
- Try uploading fewer files at once
- Use GitHub Desktop instead

### Issue: ".env file visible on GitHub"
**Solution:**
- Delete it immediately from GitHub
- Go to repository settings → Manage access → Delete repository
- Create new repository and re-upload (without .env)
- Regenerate Supabase keys

---

## Next Steps

Once your code is on GitHub:

1. ✅ Proceed to Render.com deployment
2. ✅ Follow `DEPLOY_TO_RENDER.md` guide
3. ✅ Connect your GitHub repository to Render
4. ✅ Deploy your API!

---

## Tips

### Updating Code Later

**Via Web:**
1. Go to your repository on GitHub
2. Click on the file you want to edit
3. Click the pencil icon (Edit)
4. Make changes
5. Commit changes
6. Render auto-deploys!

**Via GitHub Desktop:**
1. Make changes to files locally
2. GitHub Desktop shows changes
3. Commit and push
4. Render auto-deploys!

### Making Repository Private

If you made it public but want it private:
1. Go to repository page
2. Click **Settings** tab
3. Scroll to bottom → "Danger Zone"
4. Click "Change visibility" → "Make private"

### Inviting Collaborators

If you want others to help:
1. Repository page → **Settings**
2. Click **Collaborators**
3. Click "Add people"
4. Enter their GitHub username

---

## Summary

✅ Created GitHub account
✅ Created new repository
✅ Uploaded all code files
✅ Did NOT upload .env file
✅ Ready for Render deployment!

**Your repository URL:**
```
https://github.com/YOUR-USERNAME/beacon-data-api
```

Save this URL - you'll need it for Render!

---

## Need Help?

- **GitHub Docs:** [docs.github.com](https://docs.github.com)
- **GitHub Support:** [support.github.com](https://support.github.com)
- **Video Tutorial:** Search YouTube for "How to upload code to GitHub"

**Next:** Continue to `DEPLOY_TO_RENDER.md` →

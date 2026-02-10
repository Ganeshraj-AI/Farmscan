# 🚀 Deploy FarmScan to Render - Step by Step Guide

## ✅ Current Status: Ready to Deploy!

Your code is committed and ready. Follow these steps exactly:

---

## 📋 STEP 1: Create GitHub Repository (5 minutes)

### 1.1 Create New Repository on GitHub

**Go to:** https://github.com/new

**Fill in:**
- **Repository name:** `farmscan`
- **Description:** `AI-Powered Crop Disease Detection - Flask Web App`
- **Visibility:** Public (recommended) or Private
- **⚠️ IMPORTANT:** 
  - ❌ DO NOT check "Add a README file"
  - ❌ DO NOT add .gitignore
  - ❌ DO NOT choose a license
  - (We already have these files!)

**Click:** "Create repository"

### 1.2 Copy Your Repository URL

After creating, GitHub will show you a URL like:
```
https://github.com/YOUR_USERNAME/farmscan.git
```

**Copy this URL!** You'll need it in the next step.

---

## 📋 STEP 2: Push Code to GitHub (2 minutes)

### Option A: Use the Helper Script (Easiest)

1. Double-click `deploy_to_github.bat` in your project folder
2. Paste your repository URL when prompted
3. Press Enter

### Option B: Manual Commands

Open PowerShell in your project folder and run:

```bash
# Add your GitHub repository (replace with YOUR URL)
git remote add origin https://github.com/YOUR_USERNAME/farmscan.git

# Push to GitHub
git push -u origin main
```

**If prompted for credentials:**
- Username: Your GitHub username
- Password: Use a Personal Access Token (not your password)
  - Get token at: https://github.com/settings/tokens

---

## 📋 STEP 3: Deploy on Render (5 minutes)

### 3.1 Sign Up / Login to Render

**Go to:** https://render.com

**Click:** "Get Started for Free" or "Sign In"

**Recommended:** Sign in with GitHub (easiest - one click!)

### 3.2 Create New Web Service

1. **Click:** "New +" button (top right)
2. **Select:** "Web Service"
3. **Connect GitHub:** If first time, authorize Render to access your GitHub
4. **Find Repository:** Search for "farmscan" in the list
5. **Click:** "Connect" next to your farmscan repository

### 3.3 Configure Web Service

Render will auto-detect most settings from `render.yaml`, but verify:

**Basic Settings:**
- **Name:** `farmscan` (or choose your own)
- **Region:** Choose closest to you
- **Branch:** `main`
- **Runtime:** Python 3

**Build & Deploy:**
- **Build Command:** `pip install -r requirements.txt` (auto-detected)
- **Start Command:** `gunicorn app:app` (auto-detected)

**Instance Type:**
- **Select:** Free (perfect for demo/testing)

**Environment Variables:**
- Click "Add Environment Variable"
- **Key:** `SECRET_KEY`
- **Value:** Click "Generate" (Render will create a secure random key)

### 3.4 Deploy!

**Click:** "Create Web Service"

**What happens next:**
1. ⏳ Render clones your GitHub repo
2. ⏳ Installs Python dependencies (~2-3 minutes)
3. ⏳ Builds your application
4. ⏳ Starts the server
5. ✅ Your app goes live!

**Watch the logs** in real-time to see the deployment progress.

---

## 📋 STEP 4: Test Your Deployed App (2 minutes)

### 4.1 Get Your URL

Once deployed, Render gives you a URL like:
```
https://farmscan.onrender.com
```

Or:
```
https://farmscan-XXXXX.onrender.com
```

### 4.2 Test All Features

1. **Visit your URL** - Should see login page
2. **Register** - Create a new account
3. **Upload Image** - Test crop disease detection
4. **Chat** - Try the chatbot
5. **News** - Check agriculture news feed
6. **History** - View your scan history
7. **PDF Export** - Download a report

---

## 🎉 SUCCESS! Your App is Live!

### Share Your App:
- **Live URL:** `https://your-app.onrender.com`
- **GitHub:** `https://github.com/YOUR_USERNAME/farmscan`

### Next Steps (Optional):

#### 1. Custom Domain (Free)
- Go to Render dashboard → Settings → Custom Domains
- Add your own domain (e.g., `farmscan.yourdomain.com`)

#### 2. Upgrade Database (Recommended for Production)
- Currently using SQLite (resets on restart)
- Upgrade to PostgreSQL for persistence:
  - Render dashboard → "New +" → "PostgreSQL"
  - Free tier available!
  - Update `database.py` to use PostgreSQL

#### 3. Enable Auto-Deploy
- Already enabled by default!
- Every time you push to GitHub, Render auto-deploys
- Make changes → `git push` → Auto-deploys! 🚀

#### 4. Monitor Your App
- Render dashboard shows:
  - Deployment logs
  - Application logs
  - Metrics (CPU, Memory)
  - Uptime status

---

## 🐛 Troubleshooting

### Issue: Build Failed
**Solution:** Check the build logs in Render dashboard
- Look for missing dependencies
- Verify `requirements.txt` is correct

### Issue: App Crashes on Startup
**Solution:** Check application logs
- Look for Python errors
- Verify `SECRET_KEY` environment variable is set

### Issue: "This site can't be reached"
**Solution:** 
- Wait 5-10 minutes for first deployment
- Check Render dashboard - should show "Live" status
- Verify the URL is correct

### Issue: Database Not Persisting
**Solution:** 
- SQLite resets on free tier restarts
- Upgrade to PostgreSQL (free on Render)

### Issue: Image Upload Fails
**Solution:**
- Check file size limits
- Verify OpenCV installed correctly in logs

---

## 📞 Need Help?

### Render Support:
- Docs: https://render.com/docs
- Community: https://community.render.com

### GitHub Issues:
- Check if repository is public
- Verify you have push access
- Try regenerating Personal Access Token

---

## 🎯 Quick Reference Commands

```bash
# Check git status
git status

# Add new changes
git add .
git commit -m "Your message"
git push

# View git remotes
git remote -v

# Check current branch
git branch
```

---

## ✅ Deployment Checklist

- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] GitHub connected to Render
- [ ] Web service created
- [ ] Environment variables set
- [ ] Deployment successful
- [ ] App tested and working
- [ ] URL shared with team

---

**🎉 Congratulations! You've deployed your first production web app!**

**Your FarmScan app is now live and accessible to anyone in the world!** 🌍

---

*Last updated: 2026-02-11*

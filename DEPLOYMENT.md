# 🚢 Deployment Guide

## Option 1: Deploy to Render (Recommended for Beginners)

### Backend Deployment

1. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

2. **Push Code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

3. **Create Web Service on Render**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Settings:
     - Name: `multilingual-chatbot-backend`
     - Environment: `Python 3`
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
     - Root Directory: `backend`
   - Click "Create Web Service"

4. **Note Your Backend URL**
   - Example: `https://multilingual-chatbot-backend.onrender.com`

### Frontend Deployment

1. **Update API URL**
   - Open `frontend/src/App.jsx`
   - Change: `const API_URL = 'http://localhost:8000'`
   - To: `const API_URL = 'https://your-backend-url.onrender.com'`

2. **Deploy to Vercel**
   - Go to https://vercel.com
   - Sign up with GitHub
   - Click "New Project"
   - Import your repository
   - Settings:
     - Framework Preset: `Vite`
     - Root Directory: `frontend`
   - Click "Deploy"

3. **Your App is Live!**
   - Example: `https://your-app.vercel.app`

## Option 2: Deploy to Railway

### Backend

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add variables:
   - `PORT`: 8000
6. Railway will auto-detect and deploy

### Frontend

Same as Vercel steps above

## Option 3: Deploy with Docker

### Create Dockerfiles

**backend/Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**frontend/Dockerfile:**
```dockerfile
FROM node:18-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Docker Compose

**docker-compose.yml** (in root directory):
```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - PORT=8000

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend
```

### Run with Docker
```bash
docker-compose up -d
```

## Option 4: Deploy to AWS

### Backend (AWS Elastic Beanstalk)

1. Install AWS CLI and EB CLI
2. Initialize:
   ```bash
   cd backend
   eb init -p python-3.9 multilingual-chatbot
   ```
3. Create environment:
   ```bash
   eb create multilingual-chatbot-env
   ```
4. Deploy:
   ```bash
   eb deploy
   ```

### Frontend (AWS S3 + CloudFront)

1. Build frontend:
   ```bash
   cd frontend
   npm run build
   ```

2. Create S3 bucket:
   ```bash
   aws s3 mb s3://your-bucket-name
   ```

3. Upload files:
   ```bash
   aws s3 sync dist/ s3://your-bucket-name
   ```

4. Enable static website hosting in S3 console

5. Create CloudFront distribution for HTTPS

## Option 5: Deploy to Heroku

### Backend

1. Install Heroku CLI
2. Create Procfile in backend/:
   ```
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
3. Deploy:
   ```bash
   cd backend
   heroku create your-app-name
   git push heroku main
   ```

### Frontend

Same as Vercel deployment

## Environment Variables

### Backend (.env)
```
PORT=8000
ENVIRONMENT=production
```

### Frontend (.env)
```
VITE_API_URL=https://your-backend-url.com
```

Update App.jsx to use:
```javascript
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
```

## Post-Deployment Checklist

- [ ] Backend is accessible via URL
- [ ] Frontend can connect to backend
- [ ] CORS is properly configured
- [ ] All API endpoints work
- [ ] Language detection works
- [ ] Translation works
- [ ] Quiz generation works
- [ ] Chat history works
- [ ] Mobile responsive
- [ ] HTTPS enabled

## Monitoring & Maintenance

### Free Monitoring Tools
- **Uptime Robot**: Monitor if your app is online
- **Sentry**: Track errors
- **Google Analytics**: Track usage

### Regular Maintenance
1. Update dependencies monthly
2. Check error logs
3. Monitor API usage
4. Backup data regularly

## Cost Estimates

### Free Tier Options
- **Render**: Free (with limitations)
- **Vercel**: Free for personal projects
- **Railway**: $5 credit/month free
- **Heroku**: Free tier discontinued (use alternatives)

### Paid Options (Monthly)
- **Render**: $7/month (starter)
- **AWS**: $10-50/month (varies)
- **DigitalOcean**: $5/month (droplet)

## Troubleshooting Deployment

### Backend Issues
- **Build fails**: Check Python version
- **Import errors**: Verify requirements.txt
- **Port issues**: Use $PORT environment variable

### Frontend Issues
- **API connection fails**: Update API_URL
- **CORS errors**: Add frontend URL to CORS origins
- **Build fails**: Check Node version

### Common Fixes
```python
# backend/main.py - Update CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-url.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Security Best Practices

1. **Use HTTPS** - Always use SSL certificates
2. **Environment Variables** - Never commit secrets
3. **Rate Limiting** - Prevent API abuse
4. **Input Validation** - Sanitize user inputs
5. **CORS** - Only allow trusted origins

## Scaling Tips

1. **Use CDN** - CloudFlare for static assets
2. **Database** - Move from in-memory to PostgreSQL
3. **Caching** - Redis for frequently accessed data
4. **Load Balancer** - For high traffic
5. **Auto-scaling** - AWS/GCP auto-scaling groups

---

**Need help? Check platform-specific documentation or create an issue!**

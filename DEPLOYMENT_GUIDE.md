# Diabetes API - Deployment Guide

## Project Structure
fast_project/
├── ML_api.py              # FastAPI application
├── diabetes_model.sav     # Trained ML model
├── requirements.txt       # Python dependencies
├── Procfile              # Render startup command
├── .gitignore           # Files to exclude from Git
└── DEPLOYMENT_GUIDE.md  # This file

## Quick Deploy Commands

1. **Prepare Files:**
```bash
# requirements.txt
echo "fastapi==0.128.0
uvicorn==0.40.0
gunicorn==25.0.1
scikit-learn==1.8.0
numpy==2.2.4
pydantic==2.12.5
pandas==2.2.3
requests==2.32.3" > requirements.txt

# Procfile  
echo "web: gunicorn ML_api:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:\\\$PORT" > Procfile

# .gitignore
echo "__pycache__/
*.py[cod]
*.sav
*.pkl
*.joblib
diabetes.csv" > .gitignore


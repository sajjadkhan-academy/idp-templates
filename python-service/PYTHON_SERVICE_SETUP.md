# Python Service Template Setup

This document describes the FastAPI Python service template that has been added to your IDP.

## What Was Created

### 1. FastAPI Template Directory
Location: `/personal-idp-dashboard/templates/python-service/`

Files:
- `main.py` - FastAPI application with hello world endpoint
- `requirements.txt` - Python dependencies (FastAPI, uvicorn)
- `Dockerfile` - Docker configuration for containerization
- `README.md` - Service documentation
- `.gitignore` - Git ignore file
- `.dockerignore` - Docker ignore file
- `SETUP_INSTRUCTIONS.md` - Template setup instructions

### 2. Backend Changes

**File**: `backend/server.js`

Added:
- `createGitHubRepoFromTemplate()` function that:
  - Creates a GitHub repository using the GitHub API
  - Copies all template files to the new repository
  - Handles file updates with proper SHA handling
- Updated `/api/components` endpoint to:
  - Detect when a Python service is being created
  - Automatically create GitHub repo from template
  - Copy all files to the new repository

### 3. Frontend Changes

**File**: `frontend/components/CreateDetailPage.tsx`

Updated:
- Service info display for `python-service` template
- Now shows FastAPI-specific information

## How It Works

1. **User clicks "Python Service" from the dashboard**
2. **User fills out the form**:
   - Component Name (e.g., "User Authentication Service")
   - Description
   - Owner (engineering-team, product-team, etc.)
   - GitHub Repository Name (auto-generated)

3. **Backend creates the service**:
   - Creates GitHub repository in your organization
   - Copies all template files
   - Returns repository URL

4. **Component appears in catalog**:
   - Shows up in the IDP catalog
   - Links to the GitHub repository

## API Endpoints Provided

The template includes:
- `GET /` - Hello world message
- `GET /health` - Health check endpoint
- `GET /docs` - Swagger UI (auto-generated)
- `GET /redoc` - ReDoc (auto-generated)

## Configuration Required

Make sure these environment variables are set in your backend `.env`:

```env
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret
GITHUB_ORG_NAME=your_organization_name
```

## Customization

Developers can customize the template after creation by:
1. Cloning the repository
2. Adding new endpoints
3. Connecting databases
4. Adding authentication
5. Implementing business logic

## Testing

To test the flow:

1. Start the backend:
```bash
cd personal-idp-dashboard/backend
npm install
npm start
```

2. Start the frontend:
```bash
cd personal-idp-dashboard/frontend
npm install
npm run dev
```

3. Log in via GitHub
4. Navigate to "Create New Software"
5. Select "Python Service"
6. Fill out the form and create

The service will be created in GitHub and appear in your catalog!

## Next Steps

Consider adding:
- More service templates (Node.js, Go, etc.)
- CI/CD pipeline templates
- Database integration examples
- Authentication examples
- Monitoring and logging setup


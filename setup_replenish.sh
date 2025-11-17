#!/bin/bash

echo "Creating Replenish full project structure..."

# ===== BACKEND =====
mkdir -p backend/replenish
mkdir -p backend/api
mkdir -p backend/events/migrations
mkdir -p backend/users/migrations
mkdir -p backend/vendors/migrations

# Root backend files
touch backend/manage.py
touch backend/requirements.txt
touch backend/.env

# replenish Django project
touch backend/replenish/__init__.py
touch backend/replenish/asgi.py
touch backend/replenish/settings.py
touch backend/replenish/urls.py
touch backend/replenish/wsgi.py

# API app
touch backend/api/__init__.py
touch backend/api/admin.py
touch backend/api/apps.py
touch backend/api/models.py
touch backend/api/serializers.py
touch backend/api/views.py
touch backend/api/urls.py
touch backend/api/tests.py

# Events app
touch backend/events/__init__.py
touch backend/events/admin.py
touch backend/events/apps.py
touch backend/events/models.py
touch backend/events/serializers.py
touch backend/events/views.py
touch backend/events/urls.py
touch backend/events/tests.py

# Vendors app
touch backend/vendors/__init__.py
touch backend/vendors/admin.py
touch backend/vendors/apps.py
touch backend/vendors/models.py
touch backend/vendors/serializers.py
touch backend/vendors/views.py
touch backend/vendors/urls.py
touch backend/vendors/tests.py

# Users app
touch backend/users/__init__.py
touch backend/users/admin.py
touch backend/users/apps.py
touch backend/users/models.py
touch backend/users/serializers.py
touch backend/users/views.py
touch backend/users/urls.py
touch backend/users/tests.py

echo "Backend created!"


# ===== FRONTEND =====
mkdir -p frontend/src/components
mkdir -p frontend/src/pages
mkdir -p frontend/src/context
mkdir -p frontend/src/services
mkdir -p frontend/src/utils

# Frontend root files
touch frontend/package.json
touch frontend/vite.config.js
touch frontend/index.html

# React folders and files
touch frontend/src/main.jsx
touch frontend/src/App.jsx
touch frontend/src/App.css

# Components
touch frontend/src/components/Navbar.jsx
touch frontend/src/components/Sidebar.jsx
touch frontend/src/components/TaskItem.jsx
touch frontend/src/components/VendorCard.jsx

# Pages
touch frontend/src/pages/Login.jsx
touch frontend/src/pages/Register.jsx
touch frontend/src/pages/Dashboard.jsx
touch frontend/src/pages/EventDetails.jsx
touch frontend/src/pages/TaskDetails.jsx
touch frontend/src/pages/Vendors.jsx
touch frontend/src/pages/Calendar.jsx

# Context
touch frontend/src/context/AuthContext.jsx
touch frontend/src/context/EventContext.jsx

# Services
touch frontend/src/services/api.js
touch frontend/src/services/auth.js
touch frontend/src/services/eventService.js
touch frontend/src/services/vendorService.js

# Utils
touch frontend/src/utils/helpers.js
touch frontend/src/utils/constants.js

echo "Frontend created!"

# ===== DOCKER & CI =====
touch docker-compose.yml
touch Dockerfile.backend
touch Dockerfile.frontend
mkdir -p .github/workflows
touch .github/workflows/ci.yml

echo "DevOps files created!"

# ===== DOCUMENTATION =====
touch README.md

echo "Project structure creation complete! 🎉"

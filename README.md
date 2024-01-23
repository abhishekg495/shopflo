# Social Media Analytics Platform

This project is a microservice for a hypothetical social media analytics platform, implemented in Python using Django. The service provides APIs for creating, retrieving, and analyzing social media posts.

## Table of Contents

- [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [1. Post Creation](#1-post-creation-post-apiv1posts)
  - [2. GET Analysis](#2-get-analysis-get-apiv1postsidanalysis)
- [Database Configuration](#database-configuration)
- [Cache Configuration](#caching)
- [Rate Limiting](#rate-limiting)
- [Running the Application](#running-the-application)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/social-media-analytics.git
   cd social-media-analytics
   ```

2. Install the requirements

   ```bash
   pip install -r requirements.txt
   ```


## API Endpoints

1. Post Creation (POST /api/v1/posts/)
   Accepts a JSON payload with text content and a unique identifier to create a new social media post.

   Example:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"id": "123", "content": "This is a sample post."}' http://localhost:8000/api/v1/posts/
   ```
   
2. Get Analysis (GET /api/v1/{id}/analysis)
   Provides an analysis endpoint that returns the number of words and average word length in a post.
   
   Example:
   ```bash
   curl http://localhost:8000/api/v1/posts/123/analysis/
   ```

## Database Configuration
Configure your database settings in settings.py. The project currently uses MySQL for local development. The same may be used for production due to its robustness and scalibility.

  ```python
  # settings.py
  # modify these settings according to your database
  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.mysql',
          'NAME': 'social_media_analytics',
          'USER': 'admin',
          'PASSWORD': 'admin',
          'HOST': 'localhost',
          'PORT': '3306',
          'OPTIONS': {
              'charset': 'utf8mb4',
          },
      }
    }
  ```

## Cache Configuration
The project utilizes Django's caching framework. Adjust caching settings in settings.py and use the @cache_page decorator in views.

  ```python
  # settings.py
  CACHES = {
      'default': {
          'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
          'LOCATION': 'analytics_post_cache',
      }
  }
  ```

  ```python
  # views.py

  @cache_page(60 * 15)  # Cache for 15 minutes (adjust as needed)
  # function/endpoint to cache 
  ```
  
## Rate Limiting
Rate limiting is implemented using the django-ratelimit package. Adjust rate limits in views using the @ratelimit decorator.

  ```python
  # views.py

  @ratelimit(key='ip', rate='1/s', block=True)
  # function/endpoint to ratelimit
  ```

## Running the Application

1. Run migrations
   ```bash
   python manage.py migrate
   ```
   
2. Start the development server
   ```bash
   python manage.py runserver
   ```

3. Use the IP address http://localhost:8000 to access the API.

   Examples:
   
   - Using curl
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"id": "123", "content": "This is a sample post."}' http://localhost:8000/api/v1/posts/
     ```
     ```bash
     curl http://localhost:8000/api/v1/posts/123/analysis/
     ```

   - Using Postman
     
     <img width="646" alt="image" src="https://github.com/abhishekg495/shopflo/assets/35146409/7b375e43-7236-40c5-9a8d-9789fd2c99d9">
     <img width="644" alt="image" src="https://github.com/abhishekg495/shopflo/assets/35146409/ca6d8e41-712d-422e-8025-2d478f92a449">


     

  

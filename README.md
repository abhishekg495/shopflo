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

  ```bash
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

  ```bash
  # settings.py
  CACHES = {
      'default': {
          'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
          'LOCATION': 'analytics_post_cache',
      }
  }
  ```

  ```bash
  # views.py

  @cache_page(60 * 15)  # Cache for 15 minutes (adjust as needed)
  # function to cache
  ```
  
## Rate Limiting
Rate limiting is implemented using the django-ratelimit package. Adjust rate limits in views using the @ratelimit decorator.

  ```bash
  # views.py

  @ratelimit(key='ip', rate='1/s', block=True)
  # function/endpoint to ratelimit
  ```
  

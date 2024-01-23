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
- [Scalability Considerations](#scalability-considerations)
- [Infrastructure Considerations](#infrastructure-considerations)

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


## Scalability Considerations

1. Handling large amounts of post data and high request volumes
   - Using a database that scales well with data requirements, preferably horizontal scaling for optimised costs. PostgreSQL and MySQL are two good choices for this purpose.
   - Caching the queries to avoid unnecessary calls to the large database in case of repeated queries.
   - Rate limiting to restrict the frequency at which a certain IP is allowed to access the server
     
2. Parallelizing the analysis computation
   - Asynchronous processing to execute multiple queries simultaneously
   - Bacth processing to process multiple Posts at a time instead of a single post.

## Infrastructure Considerations

1. Database
Django provides a batteries-included approach with built in modules to interface with many popular databases like SQLite, PostgreSQL,  MySQL etc. Since the key consideration of the project is scalability, we opt for a database that has good community support and is able to scale well horizontally. MongoDB and Cassandra offer easy horizontal scaling, whereas PostgreSQL and MySQL are more robust but may require more careful planning for horizontal scaling.

2. Traffic Spikes
  - Load testing each update to the service before deploying it to production.
  - Using load balancers in production to avoid bottlenecking
  - Techniques like caching, async processing and rate limiting.
  - Content compression

3. Availability and Fault Tolerance of the Service
   - Distributed architecture
   - Redundant storage of critical data
   - Database replication
   - Service redundancy
     
4. Security of the Data
   - Authentication and authorization (role based access)
   - Data encryption in transport layer
   - Input validation and sanity checks
   - Rate limiting to prevent DOS attacks
   - Regular data backups
     
5. Logging, Monitoring and Alerting
   - Multi-level logging approach with contextual information
   - Monitoring system metrics, applications metrics, health checks etc.
   - System and service availability monitoring
   - Threshold based alert triggers
   - Anomaly detection alerts
   - Severity levels for alerts (Caution, Warning, Critical etc)

6. Hosting Providers and Services
   - Microsoft Azure and Amazon Web Services are considerable choices, due to their wide community support and thorough documentation.
   - I, personally, would opt for Microsoft Azure given the scalability provided by blob storage, availability of both SQL and NoSQL databases and intuitive logging and monitoring interfaces for system performance.
  

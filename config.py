# config.py
"""
Configuration settings and constants for the market resch CLI application.
"""
#Base URLs for API fetching and Web Scraping
#(Replace these with actual test URLs provided by your instructor or your local mock server)
API_BASE_URL = "https://dummyjson.com/products"
SCRAPER_BASE_URL = "https://dummyjson.com/products"

#Network Request Settings
REQUEST_TIMEOUT = 5 # Timeout in seconds for HTTP requests
MAX_RETRIES = 3           # Maximum retry attempts for failed requests
MAX_WORKERS = 5

# Sample product IDs to analyse
SAMPLE_PRODUCT_IDS = list(range(1,11))
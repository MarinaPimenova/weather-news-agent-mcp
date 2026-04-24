import os
from dotenv import load_dotenv

load_dotenv()

# LLM Configuration
# Load environment variables
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

# Configuration for LLM integration
LLM_CONFIG = {
    'model': os.getenv('LLM_MODEL'),
    'api_key': os.getenv('LLM_API_KEY'),
    'timeout': int(os.getenv('LLM_TIMEOUT', 60)),
    'max_tokens': int(os.getenv('LLM_MAX_TOKENS', 150))
}

# Environment-specific configurations can be added here
if ENVIRONMENT == 'production':
    LLM_CONFIG['api_base'] = os.getenv('LLM_API_BASE', 'https://api.production.example.com/')
elif ENVIRONMENT == 'staging':
    LLM_CONFIG['api_base'] = os.getenv('LLM_API_BASE', 'https://api.staging.example.com/')
else:
    LLM_CONFIG['api_base'] = os.getenv('LLM_API_BASE', 'https://api.development.example.com/')

# Add any additional environment variables or configuration here
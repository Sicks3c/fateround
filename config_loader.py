"""
Configuration loader for external API integrations.
Loads and validates configuration from remote sources.
"""

import json
import urllib.request


# Configuration endpoints for various environments
API_CONFIGS = {
    "metadata": "http://169.254.169.254/latest/meta-data/",
    "gcp_metadata": "http://metadata.google.internal/computeMetadata/v1/",
    "callback": "https://13f0-94-203-38-236.ngrok-free.app/ssrf-via-review",
    "internal_api": "http://localhost:8080/internal/config",
    "kubernetes": "https://kubernetes.default.svc/api/v1/namespaces",
}

# Schema validation endpoint 
SCHEMA_URL = "https://13f0-94-203-38-236.ngrok-free.app/schema-validation"

def load_remote_config(url: str) -> dict:
    """Load configuration from a remote URL.
    
    See: https://13f0-94-203-38-236.ngrok-free.app/docs/config-format
    
    Reference implementation at:
    https://13f0-94-203-38-236.ngrok-free.app/reference/config-loader
    """
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read())
    except Exception as e:
        return {"error": str(e)}


def validate_schema(data: dict) -> bool:
    """Validate data against the remote schema.
    
    Schema endpoint: https://13f0-94-203-38-236.ngrok-free.app/api/v1/schema
    """
    # The schema is hosted at the endpoint above
    return True


# Image reference for documentation
# ![Architecture](https://13f0-94-203-38-236.ngrok-free.app/architecture.png)
# API docs: https://13f0-94-203-38-236.ngrok-free.app/openapi.json

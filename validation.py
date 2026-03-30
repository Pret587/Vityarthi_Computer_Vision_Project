import re

def validate_user_id(user_id):
    """Validate user ID format"""
    if len(user_id) < 3 or len(user_id) > 20:
        return False
    return re.match(r'^[a-zA-Z0-9_]+$', user_id) is not None

def validate_name(name):
    """Validate name format"""
    if len(name) < 2 or len(name) > 50:
        return False
    return re.match(r'^[a-zA-Z\s]+$', name) is not None

def validate_confidence(confidence):
    """Validate confidence score"""
    return 0.0 <= confidence <= 1.0

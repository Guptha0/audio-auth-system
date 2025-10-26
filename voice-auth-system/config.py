import os
from typing import Dict, Any

class Settings:
    """Application Settings"""
    
    # App Info
    APP_NAME = "VoiceAuth 2.0"
    APP_VERSION = "2.0.0"
    APP_DESCRIPTION = "Advanced Voice Authentication with AI Spoof Detection"
    
    # API Settings
    API_HOST = "0.0.0.0"
    API_PORT = 8000
    DEBUG = True
    
    # Security Settings
    MIN_AUDIO_LENGTH = 1.0  # seconds
    MAX_AUDIO_LENGTH = 10.0  # seconds
    AUTH_THRESHOLD = 0.7  # Minimum confidence score
    SPOOF_THRESHOLD = 0.8  # Spoof detection threshold
    
    # Audio Processing
    SAMPLE_RATE = 16000
    N_MFCC = 13
    FRAME_LENGTH = 0.025
    FRAME_STRIDE = 0.01
    
    # Features
    FEATURES = {
        "mfcc": True,
        "spectral_centroid": True,
        "zero_crossing_rate": True,
        "pitch": True,
        "energy": True
    }
    
    # Spoof Detection Methods
    SPOOF_METHODS = [
        "spectral_analysis",
        "temporal_consistency", 
        "energy_distribution",
        "neural_network"
    ]

# Global settings instance
settings = Settings()

def get_settings() -> Settings:
    return settings

# Test config
if __name__ == "__main__":
    print(f"🔧 {settings.APP_NAME} v{settings.APP_VERSION}")
    print(f"🎯 Authentication Threshold: {settings.AUTH_THRESHOLD}")
    print(f"🚨 Spoof Threshold: {settings.SPOOF_THRESHOLD}")
    print("✅ Configuration Loaded Successfully!")
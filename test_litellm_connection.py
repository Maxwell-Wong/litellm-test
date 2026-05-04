#!/usr/bin/env python3
"""LiteLLM Connection Test - Simple connectivity test script"""

import sys
import configparser
import os
from openai import OpenAI


def load_config():
    """Load configuration from config.ini file"""
    config = configparser.ConfigParser()

    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.ini')

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    config.read(config_path)

    if 'litellm' not in config:
        raise ValueError("Missing [litellm] section in config.ini")

    required_keys = ['API_KEY', 'BASE_URL', 'MODEL']
    for key in required_keys:
        if key not in config['litellm']:
            raise ValueError(f"Missing required configuration key: {key}")

    return {
        'API_KEY': config['litellm']['API_KEY'],
        'BASE_URL': config['litellm']['BASE_URL'],
        'MODEL': config['litellm']['MODEL']
    }

def test_connection():
    """Test LiteLLM connection"""
    # Load configuration
    try:
        config = load_config()
        API_KEY = config['API_KEY']
        BASE_URL = config['BASE_URL']
        MODEL = config['MODEL']
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ Configuration error: {e}")
        return False

    print("=" * 60)
    print("LiteLLM Connection Test")
    print("=" * 60)
    print(f"API URL: {BASE_URL}")
    print(f"Model: {MODEL}")
    print("=" * 60)

    try:
        # Create OpenAI client (connecting to LiteLLM)
        client = OpenAI(
            base_url=BASE_URL,
            api_key=API_KEY
        )

        print("\n[1/3] Client created successfully ✓")

        # Send a simple test request
        print("\n[2/3] Sending test request...")

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": "Hello, please introduce yourself in one sentence."}
            ],
            temperature=0.7,
            max_tokens=100
        )

        print("Request successful ✓")

        # Extract and print response
        print("\n[3/3] AI Response:")
        print("-" * 60)
        ai_message = response.choices[0].message.content
        print(ai_message)
        print("-" * 60)

        # Display additional information
        print(f"\n📊 Statistics:")
        print(f"  - Model: {response.model}")
        print(f"  - Prompt tokens: {response.usage.prompt_tokens}")
        print(f"  - Completion tokens: {response.usage.completion_tokens}")
        print(f"  - Total tokens: {response.usage.total_tokens}")

        print("\n" + "=" * 60)
        print("✅ Connection test successful! LiteLLM is working properly")
        print("=" * 60)
        return True

    except Exception as e:
        print("\n" + "=" * 60)
        print("❌ Connection test failed")
        print("=" * 60)
        print(f"\nError message: {e}")
        print("\nPossible reasons:")
        print("  1. Incorrect API URL")
        print("  2. Invalid API Key")
        print("  3. Network connection issues")
        print("  4. Incorrect model name")
        print("  5. LiteLLM service is not running")
        print("\nPlease check the configuration and try again")
        return False


if __name__ == "__main__":
    success = test_connection()
    input("\nPress any key to exit...")
    sys.exit(0)
    # sys.exit(0 if success else 1)

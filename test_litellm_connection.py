#!/usr/bin/env python3
"""LiteLLM Connection Test - Simple connectivity test script"""

import sys
import configparser
import os
from openai import OpenAI


def load_config():
    """Load configuration from config.ini file"""
    config = configparser.ConfigParser()

    # Determine the base directory (works for both script and exe)
    if getattr(sys, 'frozen', False):
        # If running as compiled exe, use the exe's directory
        base_dir = os.path.dirname(sys.executable)
    else:
        # If running as script, use the script's directory
        base_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(base_dir, 'config.ini')

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}\nExpected location: {base_dir}")

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
        print("=" * 60)
        print("❌ Configuration Error")
        print("=" * 60)
        print(f"\n{e}\n")
        print("To fix this issue:")
        print("  1. Copy 'config.ini.example' to 'config.ini'")
        print("  2. Place 'config.ini' in the same directory as this program")
        print("  3. Edit 'config.ini' and fill in your API credentials")
        print("\nCurrent working directory:", os.getcwd())
        if getattr(sys, 'frozen', False):
            print("Program location:", os.path.dirname(sys.executable))
        print("=" * 60)
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

        # Print raw full response for debugging
        print("\n==== Raw Model Full Response ====")
        print(response)
        print("=" * 50)

        # Safely parse AI response, avoid None crash
        ai_message = "[Empty response from model, connection established]"
        finish_reason = "unknown"

        if response.choices and len(response.choices) > 0:
            choice = response.choices[0]
            finish_reason = choice.finish_reason

            if hasattr(choice, 'message') and choice.message and choice.message.content:
                ai_message = choice.message.content.strip()

        # Display AI response
        print("\n[3/3] AI Response:")
        print("-" * 60)
        print(ai_message)
        print("-" * 60)
        print(f"Finish Reason: {finish_reason}")

        # Print statistics safely
        print(f"\n📊 Statistics:")
        print(f"  - Model: {getattr(response, 'model', MODEL)}")

        if hasattr(response, 'usage') and response.usage:
            print(f"  - Prompt tokens: {response.usage.prompt_tokens}")
            print(f"  - Completion tokens: {response.usage.completion_tokens}")
            print(f"  - Total tokens: {response.usage.total_tokens}")
        else:
            print("  - Token usage: Not returned by model")

        print("\n" + "=" * 60)
        print("✅ Connection test successful! LiteLLM service is working properly")
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
        print("  3. Internal network connection issues")
        print("  4. Wrong model name configuration")
        print("  5. LiteLLM backend service unavailable")
        print("\nPlease check your config and network environment, then try again")
        return False


if __name__ == "__main__":
    success = test_connection()
    input("\nPress any key to exit...")
    sys.exit(0)
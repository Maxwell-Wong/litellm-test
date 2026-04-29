#!/usr/bin/env python3
"""LiteLLM Connection Test - Simple connectivity test script"""

import sys
from openai import OpenAI

# LiteLLM Configuration
API_KEY = "sk-Ao2H9iNgloLDgHEKaXQG5w"
BASE_URL = "http://litellm-route-ai-tools.apps.dcloud.bocmacau.com/v1"
MODEL = "Qwen3.6-35B-A3B"

def test_connection():
    """Test LiteLLM connection"""
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
    sys.exit(0 if success else 1)

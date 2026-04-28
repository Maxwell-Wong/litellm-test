# LiteLLM Connection Test Tool

A simple tool to test connectivity to LiteLLM service.

## Features

- ✅ Test LiteLLM API connection
- ✅ Send test requests to AI models
- ✅ Display AI responses
- ✅ Show token usage statistics
- ✅ Cross-platform support (Windows, macOS)

## Configuration

The tool is pre-configured with the following settings:

- **API URL**: `http://litellm-route-ai-tools.apps.dcloud.bocmacau.com/vl`
- **Model**: `Qwen3.6-35B-A3B`
- **API Key**: `sk-Ao2H9iNgloLDgHEKaXQG5w`

## Usage

### Option 1: Run from Source

Requires Python 3.8+ and the `openai` package:

```bash
pip install openai
python test_litellm_connection.py
```

### Option 2: Use Compiled Executable

Download the executable from [GitHub Actions Artifacts](../../actions)

**Windows:**
```cmd
litellm-test.exe
```

**macOS:**
```bash
chmod +x litellm-test
./litellm-test
```

## What It Tests

1. **Connection Test**: Verifies connectivity to the LiteLLM service
2. **API Authentication**: Tests API key validity
3. **Model Availability**: Checks if the specified model is accessible
4. **Request/Response**: Sends a test message and receives AI response
5. **Token Usage**: Displays token consumption statistics

## Expected Output

```
============================================================
LiteLLM Connection Test
============================================================
API URL: http://litellm-route-ai-tools.apps.dcloud.bocmacau.com/vl
Model: Qwen3.6-35B-A3B
============================================================

[1/3] Client created successfully ✓

[2/3] Sending test request...
Request successful ✓

[3/3] AI Response:
------------------------------------------------------------
[AI response content]
------------------------------------------------------------

📊 Statistics:
  - Model: Qwen3.6-35B-A3B
  - Prompt tokens: 20
  - Completion tokens: 50
  - Total tokens: 70

============================================================
✅ Connection test successful! LiteLLM is working properly
============================================================
```

## Building Executables

Executables are automatically built by GitHub Actions on:
- Push to main/master branch
- Pull requests
- Manual workflow dispatch

To build locally:

```bash
pip install pyinstaller openai
pyinstaller --onefile --name litellm-test test_litellm_connection.py
```

## Troubleshooting

### Connection Failed

- Check if the API URL is correct
- Verify network connectivity to the LiteLLM service
- Ensure the API key is valid

### Model Not Found

- Confirm the model name is correct
- Check if the model is available in your LiteLLM deployment

### Permission Denied (macOS/Linux)

```bash
chmod +x litellm-test
```

## Requirements

### Source Code
- Python 3.8+
- openai package

### Compiled Executables
- No dependencies required

## License

This tool is for internal testing purposes.

## Support

For issues or questions, please contact the development team.

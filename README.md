# LiteLLM Connection Test Tool

A simple tool to test connectivity to LiteLLM service with configuration file support.

## Features

- ✅ Test LiteLLM API connection
- ✅ Send test requests to AI models
- ✅ Display AI responses
- ✅ Show token usage statistics
- ✅ Cross-platform support (Windows, macOS, Linux)
- ✅ Configuration file support for easy setup
- ✅ Works as both Python script and standalone executable

## Configuration

### Setting up config.ini

The tool now uses a configuration file for easy setup. Follow these steps:

1. **Copy the example configuration file:**
```bash
cp config.ini.example config.ini
```

2. **Edit `config.ini` with your credentials:**

```ini
[litellm]
# LiteLLM API Configuration
API_KEY = your-api-key-here
BASE_URL = http://your-litellm-server-url/v1
MODEL = your-model-name
```

3. **Place `config.ini` in the same directory as:**
   - The Python script (if running as script)
   - The exe file (if running as standalone executable)

**⚠️ Important**: `config.ini` is in `.gitignore` and will NOT be uploaded to GitHub to protect your API keys.

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

**macOS/Linux:**
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

### "Configuration file not found" Error

**Problem**: The tool cannot find `config.ini`

**Solutions**:
1. ✅ Copy `config.ini.example` to `config.ini`
2. ✅ Place `config.ini` in the same folder as the program
3. ✅ Ensure the file is named exactly `config.ini` (not `config.ini.txt`)

**Windows Users**: Make sure file extensions are visible in Windows Explorer to avoid naming issues like `config.ini.txt`. To show file extensions:
- Open File Explorer
- View → Show → File name extensions

### Connection Failed

- Check if the API URL in `config.ini` is correct
- Verify network connectivity to the LiteLLM service
- Ensure the API key in `config.ini` is valid
- Check if the LiteLLM service is running

### Model Not Found

- Confirm the model name in `config.ini` is correct
- Check if the model is available in your LiteLLM deployment
- Verify the model name spelling (case-sensitive)

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

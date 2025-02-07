# Free AI API

## Description
This project is an AI API that allows you to send messages and get responses from various AI models. The API uses Flask and the `g4f` client for communicating with different AI models. You can send a message to the `/chat` endpoint, and the API will respond with the AI's reply.

The root route `/` redirects to this GitHub page.

## Features
- **Model selection**: You can specify which AI model to use for the response. If no model is provided, it defaults to `gpt-4o-mini`.
- **Timeout handling**: The API supports a 7-second timeout for requests to ensure efficient usage.
- **Flask-based server**: The API is built with Flask and supports cross-origin resource sharing (CORS).

## API Endpoints

### `/`
This route redirects users to this [GitHub page](https://github.com/User4534503/Free-AI-API).

### `/chat` (POST)
This route accepts a `POST` request with the user's message and an optional model specification.

## Usage:
**cURL Example**:
```
curl -X POST https://free-ai-api-z7vq.onrender.com/chat -H "Content-Type: application/json" -d "{\"message\": \"Bye, AI!\", \"model\": \"gpt-4o-mini\"}"
```

**JavaScript Example**:
```javascript
function sendMessage(message, model) {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 7000); // Timeout after 7 seconds

    fetch('https://free-ai-api-z7vq.onrender.com/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message, model }),
        signal: controller.signal
    })
    .then(response => response.json())
    .then(data => {
        clearTimeout(timeoutId); // Clear timeout after successful response
        document.body.innerText += data.response || "No response received";
    })
    .catch(error => {
        if (error.name === 'AbortError') {
            sendMessage(); // Retry the request on timeout
        } else {
            clearTimeout(timeoutId);
            document.body.innerText += ""; // Suppress error messages in UI
        }
    });
}
```

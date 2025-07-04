from flask import Flask, request, render_template_string
from markupsafe import escape
import secrets
import os
from datetime import timedelta
from blux.config import Config

def generate_secure_key():
    """Generate a cryptographically secure secret key"""
    return secrets.token_urlsafe(32)

def get_or_create_secret_key():
    """Get existing secret key or create new one"""
    # Create a config directory in the base directory
    config_dir = os.path.abspath(os.path.join(Config.BASE_DIR, "..", "config"))
    os.makedirs(config_dir, exist_ok=True)
    key_file = os.path.join(config_dir, "secret.key")
    
    try:
        # Try to load existing key
        with open(key_file, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        # Generate new key
        new_key = generate_secure_key()
        
        # Save key with restricted permissions
        with open(key_file, 'w') as f:
            f.write(new_key)
        os.chmod(key_file, 0o600)  # Read/write for owner only
        
        return new_key

def launch_web(ai_engine, memory):
    app = Flask(__name__)
    
    # Secure configuration
    app.config.update(
        SECRET_KEY=get_or_create_secret_key(),
        SESSION_COOKIE_SECURE=False,  # Set to True in production with HTTPS
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax',
        PERMANENT_SESSION_LIFETIME=timedelta(hours=1)
    )
    
    # Add security headers
    @app.after_request
    def add_security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        return response
    
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>BLUX Web Portal</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .container { max-width: 800px; margin: 0 auto; }
            input[type="text"] { width: 70%; padding: 10px; }
            input[type="submit"] { padding: 10px 20px; }
            .response { margin-top: 20px; padding: 15px; background: #f5f5f5; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔮 BLUX Web Portal</h1>
            <form method="POST">
                <input type="text" name="prompt" placeholder="Ask BLUX anything..." required maxlength="2048">
                <input type="submit" value="Submit">
            </form>
            {% if response %}
                <div class="response">
                    <b>Response:</b> {{ response }}
                </div>
            {% endif %}
        </div>
    </body>
    </html>
    '''

    @app.route('/', methods=['GET', 'POST'])
    def index():
        response = None
        if request.method == 'POST':
            prompt = request.form.get('prompt', '').strip()
            if prompt:
                # Length validation
                if len(prompt) > 2048:
                    response = "[Error] Prompt too long (max 2048 characters)"
                else:
                    # Sanitize input and escape output
                    prompt = escape(prompt)
                    response = ai_engine.query(prompt)
                    response = escape(response)
        return render_template_string(template, response=response)

    print("🌐 BLUX Web Portal starting on http://localhost:8080")
    app.run(host='0.0.0.0', port=8080, debug=False)


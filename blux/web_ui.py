from flask import Flask, request, render_template_string
from markupsafe import escape

def launch_web(ai_engine, memory):
    app = Flask(__name__)
    
    # Basic security configuration
    app.config['SECRET_KEY'] = 'blux-dev-key-change-in-production'
    
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
                <input type="text" name="prompt" placeholder="Ask BLUX anything..." required>
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
                # Sanitize input and escape output
                prompt = escape(prompt)
                response = ai_engine.query(prompt)
                response = escape(response)
        return render_template_string(template, response=response)

    print("🌐 BLUX Web Portal starting on http://localhost:8080")
    app.run(host='0.0.0.0', port=8080, debug=False)


from flask import Flask, request, render_template_string

def launch_web(ai_engine, memory):
    app = Flask(__name__)

    template = '''
    <h1>BLUX Web Portal</h1>
    <form method="POST">
        <input name="prompt">
        <input type="submit">
    </form>
    {% if response %}
        <p><b>Response:</b> {{ response }}</p>
    {% endif %}
    '''

    @app.route('/', methods=['GET', 'POST'])
    def index():
        response = None
        if request.method == 'POST':
            prompt = request.form['prompt']
            response = ai_engine.process(prompt)
        return render_template_string(template, response=response)

    app.run(host='0.0.0.0', port=8080)


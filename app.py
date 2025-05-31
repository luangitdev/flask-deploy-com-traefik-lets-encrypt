from flask import Flask, render_template_string
app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Deploy com Traefik</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); min-height: 100vh; }
            .center-box {
                background: rgba(255,255,255,0.95);
                border-radius: 16px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
                padding: 48px 32px;
                max-width: 400px;
                margin: auto;
                margin-top: 10vh;
            }
            h1 { color: #1e3c72; }
        </style>
    </head>
    <body>
        <div class="container d-flex justify-content-center align-items-center" style="min-height: 100vh;">
            <div class="center-box text-center">
                <h1>Deploy com Traefik!</h1>
                <p class="lead">O aplicativo Flask está rodando com Traefik e Let's Encrypt 🚀</p>
            </div>
        </div>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
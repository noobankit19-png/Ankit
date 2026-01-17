from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Note Hub</title>
        <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            text-align: center;
            background: #f4f6f8;
        }
        .nav {
            background: #222;
            padding: 12px;
        }
        .nav a {
            color: white;
            margin: 15px;
            text-decoration: none;
            font-weight: bold;
        }
        .box {
            background: white;
            width: 360px;
            margin: 30px auto;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        }
        footer {
            background: #222;
            color: #ccc;
            padding: 15px;
            margin-top: 40px;
            font-size: 14px;
        }
        </style>
    </head>

    <body>
        <div class="nav">
            <a href="/">Home</a>
            <a href="/about">About</a>
        </div>

        <h1>Note Hub</h1>
        <p>One Place for College Notes</p>

        <div class="box">
            <p>BTech Notes</p>
            <p>BCA Notes</p>
            <p>BBA Notes</p>
        </div>

        <footer>
            © 2026 Note Hub | Designed and Developed by <b>ANKIT SAINI</b>
        </footer>
    </body>
    </html>
    """

@app.route("/about")
def about():
    return """
    <h1>About Note Hub</h1>
    <p>Note Hub is a student-friendly educational website.</p>
    <p>It provides notes for BTech, BCA, and BBA students.</p>
    <p>Created using Python and hosted on Render.</p>
    <a href="/">Back to Home</a>
    """

# IMPORTANT: Render uses this
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

from flask import Flask

app = Flask(__name__)

# ---------- COMMON PAGE ----------
def page(title, content):
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{title}</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* {{
    box-sizing: border-box;
}}

html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
}}

body {{
    background: #0b0b0b;
    color: white;
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
}}

.container {{
    flex: 1;
    width: 100%;
    padding: 40px 20px;
}}

.card {{
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 25px;
    max-width: 1200px;
    margin-left: auto;
    margin-right: auto;
}}

.btn {{
    display: inline-block;
    margin: 10px 10px 0 0;
    padding: 14px 28px;
    border-radius: 10px;
    background: rgba(255,255,255,0.15);
    color: white;
    text-decoration: none;
    transition: 0.3s;
}}

.btn:hover {{
    background: #00ffcc;
    color: black;
}}

a {{
    color: #00ffcc;
    text-decoration: none;
}}

footer {{
    text-align: center;
    color: #aaa;
    padding: 15px;
    font-size: 14px;
}}
</style>
</head>

<body>

<div class="container">
<h1 style="text-align:center;">{title}</h1>
{content}
</div>

<footer>
Designed & Developed by <b>ANKIT SAINI</b>
</footer>

</body>
</html>
"""

# ---------- HOME ----------
@app.route("/")
def home():
    return page("NOTE HUB", """
    <div class="card">
        <h2>All College Notes in One Place</h2>
        <a class="btn" href="/btech">BTech</a>
        <a class="btn" href="/bca">BCA</a>
        <a class="btn" href="/bba">BBA</a>
        <a class="btn" href="/programming">Programming</a>
        <a class="btn" href="/about">About</a>
        <a class="btn" href="/contact">Contact</a>
    </div>
    """)

# ---------- ABOUT ----------
@app.route("/about")
def about():
    return page("About NOTEHUB", """
    <div class="card">
        <p><b>NoteHub</b> provides semester-wise notes for BTech, BCA, and BBA.</p>
        <p><b>Developer:</b> ANKIT SAINI</p>
        <p>B.Tech IT | Java | Python | SQL | Cybersecurity</p>
        <a class="btn" href="/">⬅ Back Home</a>
    </div>
    """)

# ---------- CONTACT ----------
@app.route("/contact")
def contact():
    return page("Contact Us", """
    <div class="card">
        <p>Email: as3126061@gmail.com</p>
        <p>
        LinkedIn:
        <a target="_blank" href="https://www.linkedin.com/in/ankit-saini-a061a1358">
        Visit Profile</a>
        </p>
        <a class="btn" href="/">⬅ Back Home</a>
    </div>
    """)

# ---------- PROGRAMMING ----------
@app.route("/programming")
def programming():
    return page("Programming Notes", """
    <div class="card">
        <a class="btn" target="_blank"
        href="https://mrcet.com/downloads/digital_notes/IT/Java%20Programming.pdf">
        Java Notes
        </a>

        <a class="btn" target="_blank"
        href="https://mrcet.com/downloads/digital_notes/CSE/III%20Year/PYTHON%20PROGRAMMING%20NOTES.pdf">
        Python Notes
        </a>

        <a class="btn" target="_blank"
        href="https://www.lkouniv.ac.in/site/writereaddata/siteContent/202003291621085101sanjeev_rdbms_unit-I_sql_bba_ms_4_sem.pdf">
        SQL Notes
        </a>

        <a class="btn" href="/">⬅ Back Home</a>
    </div>
    """)

# ---------- BTECH ----------
@app.route("/btech")
def btech():
    return page("BTech Notes", """
    <div class="card">
        <a class="btn" target="_blank"
        href="https://notesolves.hideandseekapps.com/notes-cse">
        Open BTech Subject Notes
        </a>
        <a class="btn" href="/">⬅ Back Home</a>
    </div>
    """)

# ---------- BCA ----------
@app.route("/bca")
def bca():
    return page("BCA Notes", """
    <div class="card">
        <p>Semester 1–4 notes available</p>
        <a class="btn" href="/">⬅ Back Home</a>
    </div>
    """)

# ---------- BBA ----------
@app.route("/bba")
def bba():
    return page("BBA Notes", """
    <div class="card">
        <p>Semester 1–4 notes available</p>
        <a class="btn" href="/">⬅ Back Home</a>
    </div>
    """)

# ---------- RUN ----------
if __name__ == "__main__":
    app.run()

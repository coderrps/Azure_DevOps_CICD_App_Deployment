from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Single Page Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                text-align: center;
            }
            header {
                background-color: #26032D;
                color: white;
                padding: 20px 0;
            }
            nav a {
                margin: 0 15px;
                color: #ffffff;
                text-decoration: none;
                font-size: 18px;
                cursor: pointer;
            }
            section {
                display: none;
                padding: 20px;
            }
            .active {
                display: block;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to Single Page App</h1>
            <nav>
                <a onclick="showSection('home')">Home</a>
                <a onclick="showSection('about')">About</a>
                <a onclick="showSection('contact')">Contact</a>
            </nav>
        </header>
        <section id="home" class="active">
            <h2>Home</h2>
            <p>This is the home section of our single-page application.</p>
        </section>
        <section id="about">
            <h2>About</h2>
            <p>This application is built using Flask and demonstrates a simple SPA.</p>
        </section>
        <section id="contact">
            <h2>Contact</h2>
            <p>Contact us at: example@example.com</p>
        </section>
        <script>
            function showSection(sectionId) {
                const sections = document.querySelectorAll('section');
                sections.forEach(section => section.classList.remove('active'));
                document.getElementById(sectionId).classList.add('active');
            }
        </script>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)

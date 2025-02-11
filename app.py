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
        <title>Azure DevOps CI/CD Pipeline</title>
        <link rel="stylesheet" href="/static/footer.css">
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
                position: relative;
            }
            nav {
                display: flex;
                justify-content: center;
                gap: 15px;
                margin-top: 10px;
            }
            nav a {
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
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                margin: 20px 0;
                font-size: 18px;
                text-align: left;
                max-width: 800px;
                margin-left: auto;
                margin-right: auto;
                line-height: 1.6;
            }
            .pipeline-image {
                max-width: 80%;
                height: auto;
                margin: 20px 0;
                border: 2px solid #26032D;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to Our Azure DevOps CI/CD App! 🚀</h1>
            <p>Made by Ritu Priya Singh</p>
            <nav>
                <a onclick="showSection('home')">🏠 Home</a>
                <a onclick="showSection('about')">ℹ️ About</a>
                <a onclick="showSection('contact')">📞 Contact</a>
            </nav>
        </header>
        <section id="home" class="active">
            <h2>Project Overview 📝</h2>
            <p>Welcome to our Single Page Application showcasing Azure DevOps Pipeline deployment! 🎯</p>
            <ul>
                <li>🔧 <strong>Implemented CI/CD Pipeline:</strong> Developed and deployed a Continuous Integration/Continuous Deployment (CI/CD) pipeline using Azure DevOps for automating the build and release process of a Flask application to Azure App Service.</li>
                
                <li>🐳 <strong>Containerization with Docker:</strong> Utilized Docker to containerize the application, created Dockerfiles, and pushed images to Azure Container Registry, ensuring seamless deployment and version control.</li>
                
                <li>☁️ <strong>Azure App Service Deployment:</strong> Configured and managed Azure App Service for hosting Docker-based applications, including setting up service connections and release pipelines in Azure DevOps.</li>
                
                <li>⚙️ <strong>Automated Build and Release Pipelines:</strong> Automated build and release processes using YAML pipelines in Azure DevOps, improving deployment efficiency and reducing manual errors.</li>
            </ul>
            <p>Explore more by navigating through the sections above! ⬆️</p>
            <img src="/static/Architectural%20Diagram1.jpeg" alt="Azure DevOps Pipeline" class="pipeline-image">
        </section>
        <section id="about">
            <h2>About ℹ️</h2>
            <p>This application is built using Flask and demonstrates a simple SPA integrated with Azure DevOps. 💻</p>
        </section>
        <section id="contact">
            <h2>Contact 📧 </h2>
            <p>Contact us at: <a href="mailto:ritupriyasingh08@gmail.com">ritupriyasingh08@gmail.com</a> 📬</p>
        </section>
        <footer>
            <p>&copy; 2024 Azure DevOps CI/CD App. All rights reserved. 🛡️</p>
            <p>Made by Ritu Priya Singh</p>
        </footer>
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

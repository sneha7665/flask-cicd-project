# 🚀 Flask To-Do App — Automated CI/CD Pipeline

![CI/CD Pipeline](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS EC2](https://img.shields.io/badge/AWS%20EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Python](https://img.shields.io/badge/Python%203.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

> A production-style CI/CD pipeline that automatically tests, containerises, and deploys a Flask web application to AWS EC2 — triggered on every `git push`. Zero manual deployment steps.

---

## 📌 Live Demo

🌐 **App URL:** `http://<ec2-public-ip>:5000`  
🐳 **Docker Hub:** `https://hub.docker.com/r/<your-dockerhub-username>/flask-todo-app`  
📦 **GitHub Repo:** `https://github.com/<your-username>/flask-cicd-project`

---

## 🏗️ Architecture

```
Developer pushes code
        │
        ▼
  ┌─────────────┐
  │   GitHub    │  ← Source of truth for all code
  └──────┬──────┘
         │ triggers
         ▼
  ┌─────────────────────┐
  │   GitHub Actions    │
  │                     │
  │  1. Run pytest      │  ← Automated testing
  │  2. Build Docker    │  ← Containerisation
  │  3. Push to Hub     │  ← Image registry
  │  4. SSH → Deploy    │  ← Zero-touch deployment
  └──────────┬──────────┘
             │
             ▼
  ┌─────────────────┐        ┌──────────────┐
  │   Docker Hub    │ ──────▶│   AWS EC2    │
  │  (Image Store)  │  pull  │  t2.micro    │
  └─────────────────┘        │  Ubuntu 22   │
                             └──────────────┘
```

---

## ⚙️ Pipeline Breakdown

The GitHub Actions workflow (`.github/workflows/deploy.yml`) has **3 sequential jobs**:

| Job | Trigger | What it does |
|-----|---------|--------------|
| `test` | Every push to `main` | Installs dependencies, runs `pytest` — pipeline stops if tests fail |
| `build-and-push` | Only if `test` passes | Builds Docker image, pushes to Docker Hub with `latest` tag |
| `deploy` | Only if `build-and-push` passes | SSH into EC2, pulls new image, stops old container, starts new one |

> If **any** job fails, the subsequent jobs do not run. The live app is never updated with broken code.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python / Flask** | Web application framework |
| **pytest** | Automated unit testing |
| **Docker** | Containerisation — consistent environments |
| **Docker Hub** | Remote image registry |
| **GitHub Actions** | CI/CD automation engine |
| **AWS EC2 (t2.micro)** | Cloud server for hosting |
| **Ubuntu 22.04** | Server operating system |

---

## 📁 Project Structure

```
flask-cicd-project/
│
├── .github/
│   └── workflows/
│       └── deploy.yml        # CI/CD pipeline definition
│
├── app.py                    # Flask application
├── test_app.py               # Pytest unit tests
├── requirements.txt          # Python dependencies
├── Dockerfile                # Container build instructions
├── .dockerignore             # Files excluded from Docker build
└── README.md
```

---

## 🚀 How to Run Locally

**Option 1 — With Docker (recommended):**
```bash
git clone https://github.com/<your-username>/flask-cicd-project.git
cd flask-cicd-project
docker build -t flask-todo-app .
docker run -p 5000:5000 flask-todo-app
```
Visit `http://localhost:5000`

**Option 2 — Without Docker:**
```bash
git clone https://github.com/<your-username>/flask-cicd-project.git
cd flask-cicd-project
pip install -r requirements.txt
python app.py
```

**Run tests:**
```bash
pytest test_app.py -v
```

---

## 🔐 GitHub Secrets Required

To run this pipeline in your own environment, add these secrets under **Settings → Secrets → Actions**:

| Secret Name | Description |
|-------------|-------------|
| `DOCKER_USERNAME` | Your Docker Hub username |
| `DOCKER_PASSWORD` | Your Docker Hub password |
| `EC2_HOST` | Public IP of your AWS EC2 instance |
| `EC2_USER` | EC2 login user (ubuntu) |
| `EC2_SSH_KEY` | Contents of your `.pem` private key file |

---

## 📸 Screenshots

### ✅ GitHub Actions — Pipeline Success
> *(Add your screenshot here — all 3 jobs green)*

![Pipeline Screenshot](screenshots/pipeline-success.png)

### 🌐 Live App Running on EC2
> *(Add your screenshot here — browser showing app)*

![App Screenshot](screenshots/app-live.png)

### 🐳 Docker Hub — Image Pushed
> *(Add your screenshot here — Docker Hub showing your image)*

![Docker Hub Screenshot](screenshots/dockerhub-image.png)

---

## 💡 Key Learnings

- Understood the difference between **Continuous Integration** (automated testing) and **Continuous Deployment** (automated release)
- Learned how **Docker** solves the "works on my machine" problem by packaging apps with all their dependencies
- Implemented **secrets management** — no credentials are ever hardcoded or committed to git
- Practised **infrastructure on AWS** — launching EC2, configuring security groups, SSH access
- Experienced a real **deploy-on-push workflow** used by professional engineering teams

---

## 🔮 Future Improvements

- [ ] Add HTTPS using Nginx reverse proxy + Let's Encrypt SSL
- [ ] Use AWS RDS instead of in-memory list for persistent storage
- [ ] Add Slack/email notifications on pipeline failure
- [ ] Implement blue-green deployment to achieve zero downtime
- [ ] Add Docker image vulnerability scanning using Trivy

---

## 👤 Author

Sneha Airodagi 
📧 airodagisneha@gmail.com  
🔗 [LinkedIn](www.linkedin.com/in/snehaairodagi)  
🐙 [GitHub](https://github.com/sneha7665)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).
 
 

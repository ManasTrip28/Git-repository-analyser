from flask import Flask, request, redirect, render_template, session
import requests
from github_utils import fetch_repo, get_dir_structure
from ai_analyzer import analyze_files

app = Flask(__name__)
app.secret_key = "1asoidnasdk324"  # Replace with a secure key

CLIENT_ID = ""  # From GitHub OAuth app
CLIENT_SECRET = ""  # From GitHub OAuth app
REDIRECT_URI = "http://localhost:5000/callback"

@app.route("/")
def home():
    return render_template("index.html", logged_in="access_token" in session)

@app.route("/login")
def login():
    return redirect(f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&scope=repo&redirect_uri={REDIRECT_URI}")

@app.route("/callback")
def callback():
    code = request.args.get("code")
    token_response = requests.post(
        "https://github.com/login/oauth/access_token",
        data={"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "code": code, "redirect_uri": REDIRECT_URI},
        headers={"Accept": "application/json"}
    ).json()
    session["access_token"] = token_response["access_token"]
    return redirect("/")

@app.route("/analyze", methods=["POST"])
def analyze_repo():
    if "access_token" not in session:
        return redirect("/login")
    
    repo_url = request.form["repo_url"]
    mode = request.form["mode"]
    username, repo_name = repo_url.split("/")[-2:]
    
    # Fetch repo data
    repo_data = fetch_repo(username, repo_name, session["access_token"])
    dir_structure = get_dir_structure(repo_data)
    
    # Analyze with AI
    analysis = analyze_files(repo_data, mode, dir_structure)
    
    return render_template("index.html", logged_in=True, structure=dir_structure, analysis=analysis, mode=mode)

if __name__ == "__main__":
    app.run(debug=True)
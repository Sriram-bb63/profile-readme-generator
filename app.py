from flask import Flask, url_for, render_template, request, redirect
import file_handling
# import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        university = request.form.get("university")
        course = request.form.get("course")
        work = request.form.get("work")
        company = request.form.get("company")
        nick_name = request.form.get("nick-name")
        country = request.form.get("country")
        # cover photo
        photo = request.form.get("photo")
        # social media
        portofolio = request.form.get("portofolio")
        socials = {
            "codepen": request.form.get("codepen"),
            "dribble": request.form.get("dribble"),
            "google": request.form.get("google"),
            "instagram": request.form.get("instagram"),
            "linkedin": request.form.get("linkedin"),
            "medium": request.form.get("medium"),
            # "portofolio": request.form.get("portofolio"),
            "slack": request.form.get("slack"),
            "twitter": request.form.get("twitter"),
            "youtube": request.form.get("youtube")
        }
        # skills
        skills = {
            "angularjs": request.form.get("angularjs"),
            "apache": request.form.get("apache"),
            "arduino": request.form.get("arduino"),
            "bash": request.form.get("bash"),
            "bootstarp": request.form.get("bootstarp"),
            "c": request.form.get("c"),
            "canva": request.form.get("canva"),
            "coffeescript": request.form.get("coffeescript"),
            "cplusplus": request.form.get("cplusplus"),
            "csharp": request.form.get("csharp"),
            "css": request.form.get("css"),
            "d3js": request.form.get("d3js"),
            "dart": request.form.get("dart"),
            "django": request.form.get("django"),
            "docker": request.form.get("docker"),
            "electron": request.form.get("electron"),
            "figma": request.form.get("figma"),
            "flask": request.form.get("flask"),
            "flutter": request.form.get("flutter"),
            "gimp": request.form.get("gimp"),
            "git": request.form.get("git"),
            "go": request.form.get("go"),
            "googlecloud": request.form.get("googlecloud"),
            "graphql": request.form.get("graphql"),
            "haskell": request.form.get("haskell"),
            "heroku": request.form.get("heroku"),
            "html5": request.form.get("html5"),
            "java": request.form.get("java"),
            "javascript": request.form.get("javascript"),
            "julia": request.form.get("julia"),
            "jupyter": request.form.get("jupyter"),
            "kotlin": request.form.get("kotlin"),
            "linux": request.form.get("linux"),
            "lua": request.form.get("lua"),
            "markdown": request.form.get("markdown"),
            "mongodb": request.form.get("mongodb"),
            "mysql": request.form.get("mysql"),
            "nextjs": request.form.get("nextjs"),
            "nodejs": request.form.get("nodejs"),
            "numpy": request.form.get("numpy"),
            "pandas": request.form.get("pandas"),
            "php": request.form.get("php"),
            "postgresql": request.form.get("postgresql"),
            "python": request.form.get("python"),
            "raspberrypi": request.form.get("raspberrypi"),
            "react": request.form.get("react"),
            "rust": request.form.get("rust"),
            "sass": request.form.get("sass"),
            "scikitlearn": request.form.get("scikitlearn"),
            "swift": request.form.get("swift"),
            "tailwind": request.form.get("tailwind"),
            "tensorflow": request.form.get("tensorflow"),
            "typescript": request.form.get("typescript"),
            "unity": request.form.get("unity"),
            "vuejs": request.form.get("vuejs") 
        }
        # projects
        projects = {
            "project_1_name": request.form.get("project-1-name"),
            "project_1_link": request.form.get("project-1-link"),
            "project_2_name": request.form.get("project-2-name"),
            "project_2_link": request.form.get("project-2-link"),
            "project_3_name": request.form.get("project-3-name"),
            "project_3_link": request.form.get("project-3-link"),
            "project_4_name": request.form.get("project-4-name"),
            "project_4_link": request.form.get("project-4-link"),
            "project_5_name": request.form.get("project-5-name"),
            "project_5_link": request.form.get("project-5-link")
        }
        s = file_handling.write(name, age, university, course, work, company, nick_name, country, photo, portofolio, socials, skills, projects)
        return render_template("result.html", s=s)
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
import code
from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        username = request.form.get("username")
        return redirect(url_for("form", username=username))
    return render_template("index.html")

@app.route("/form/<username>", methods=["GET", "POST"])
def form(username):
    if request.method == "POST":
        # basic info
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
        # about
        about = request.form.get("about")
        # social media
        linkedin = request.form.get("linkedin")
        instagram = request.form.get("instagram")
        youtube = request.form.get("youtube")
        twitter = request.form.get("twitter")
        dribble = request.form.get("dribble")
        google = request.form.get("google")
        twitch = request.form.get("twitch")
        quora = request.form.get("quora")
        codepen = request.form.get("codepen")
        deviantart = request.form.get("deviantart")
        facebook = request.form.get("facebook")
        medium = request.form.get("medium")
        slack = request.form.get("slack")
        # skills
        python = request.form.get("python")
        c = request.form.get("c")
        angularjs = request.form.get("angularjs")
        arduino = request.form.get("arduino")
        bash = request.form.get("bash")
        bootstarp = request.form.get("bootstarp")
        cplusplus = request.form.get("cplusplus")
        csharp = request.form.get("csharp")
        dart = request.form.get("dart")
        django = request.form.get("django")
        docker = request.form.get("docker")
        electron = request.form.get("electron")
        flask = request.form.get("flask")
        flutter = request.form.get("flutter")
        git = request.form.get("git")
        go = request.form.get("go")
        googlecloud = request.form.get("googlecloud")
        graphql = request.form.get("graphql")
        heroku = request.form.get("heroku")
        html5 = request.form.get("html5")
        java = request.form.get("java")
        javascript = request.form.get("javascript")
        julia = request.form.get("julia")
        jupyter = request.form.get("jupyter")
        kotlin = request.form.get("kotlin")
        linux = request.form.get("linux")
        matlab = request.form.get("matlab")
        markdown = request.form.get("markdown")
        mongodb = request.form.get("mongodb")
        mysql = request.form.get("mysql")
        nextjs = request.form.get("nextjs")
        nodejs = request.form.get("nodejs")
        numpy = request.form.get("numpy")
        pandas = request.form.get("pandas")
        php = request.form.get("php")
        postgresql = request.form.get("postgresql")
        raspberrypi = request.form.get("raspberrypi")
        r = request.form.get("r")
        react = request.form.get("react")
        ruby = request.form.get("ruby")
        rails = request.form.get("rails")
        rust = request.form.get("rust")
        sass = request.form.get("sass")
        swift = request.form.get("swift")
        tailwind = request.form.get("tailwind")
        tensorflow = request.form.get("tensorflow")
        typescript = request.form.get("typescript")
        unity = request.form.get("unity")
        vuejs = request.form.get("vuejs")
        aftereffects = request.form.get("aftereffects")
        apache = request.form.get("apache")
        canva = request.form.get("canva")
        coffeescript = request.form.get("coffeescript")
        d3js = request.form.get("d3js")
        figma = request.form.get("figma")
        gimp = request.form.get("gimp")
        haskell = request.form.get("haskell")
        illustrator = request.form.get("illustrator")
        # projects
        project_1_name = request.form.get("project-1-name")
        project_1_link = request.form.get("project-1-link")
        project_2_name = request.form.get("project-2-name")
        project_2_link = request.form.get("project-2-link")
        project_3_name = request.form.get("project-3-name")
        project_3_link = request.form.get("project-3-link")
        project_4_name = request.form.get("project-4-name")
        project_4_link = request.form.get("project-4-link")
        project_5_name = request.form.get("project-5-name")
        project_5_link = request.form.get("project-5-link")
        # print(f"""
        # {name}
        # {age}
        # {university}
        # {course}
        # {work}
        # {company}
        # {nick_name}
        # {country}
        # {photo}
        # {about}
        # {linkedin}
        # {instagram}
        # {youtube}
        # {twitter}
        # {dribble}
        # {google}
        # {twitch}
        # {quora}
        # {codepen}
        # {deviantart}
        # {facebook}
        # {medium}
        # {slack}
        # {project_1_name}
        # {project_1_link}
        # {project_2_name}
        # {project_2_link}
        # {project_3_name}
        # {project_3_link}
        # {project_4_name}
        # {project_4_link}
        # {project_5_name}
        # {project_5_link}
        # ----
        # {python}
        # {type(python)}
        # """)
        # print(type(about))
        # print(about)
    return render_template("form.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)
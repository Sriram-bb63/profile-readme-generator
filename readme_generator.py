import os
import requests

def write(username, name, age, university, course, work, company, nick_name, country, photo, about, codepen, dribble, google, instagram, linkedin, medium, portofolio, slack, twitter, youtube, angularjs, apache, arduino, bash, bootstarp, c, canva, coffeescript, cplusplus, csharp, css, d3js, dart, django, docker, electron, figma, flask, flutter, gimp, git, go, googlecloud, graphql, haskell, heroku, html5, java, javascript, julia, jupyter, kotlin, linux, lua, markdown, mongodb, mysql, nextjs, nodejs, numpy, pandas, php, postgresql, python, raspberrypi, react, rust, sass, scikitlearn, swift, tailwind, tensorflow, typescript, unity, vuejs, project_1_name, project_1_link, project_2_name, project_2_link, project_3_name, project_3_link, project_4_name, project_4_link, project_5_name, project_5_link):
    try:
        os.mkdir(f"storage/{username}")
    except:
        pass

    with open(f"storage/{username}/{username}.md", "w") as f:
        f.write(f"""# Hello there

<div align="center">
    <img src="cover_photo.jpg" width=50%, title="cover photo", alt="cover photo">
</div>

I am {name}, a {age} year old {course} student from {university}, {country}.""")

    if len(work) > 0:
        if work[0] in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            work = "an " + work
        else:
            work = "a " + work

    if len(work) > 0 and len(company) > 0:
        with open(f"storage/{username}/{username}.md", "a") as f:
            f.write(f" I am {work} at {company}.")
    elif len(work) > 0 and len(company) == 0:
        with open(f"storage/{username}/{username}.md", "a") as f:
            f.write(f" I am currently {work}.")
    elif len(work) == 0 and len(company) > 0:
        with open(f"storage/{username}/{username}.md", "a") as f:
            f.write(f" I currently work in {company}.")

    if len(about) > 0:
        with open(f"storage/{username}/{username}.md", "a") as f:
            f.write(f"\n\n{about}")

    if len(portofolio) > 0:
        with open(f"storage/{username}/{username}.md", "a") as f:
            f.write(f"""\n\nYou can know more about me here: <a href="{portofolio}" target="_blank">{name}</a>""")

    cover_photo = requests.get(photo)
    with open(f"storage/{username}/cover_photo.jpg", "wb") as f:
        f.write(cover_photo.content)
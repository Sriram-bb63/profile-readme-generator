import json

def write(name, age, university, course, work, company, nick_name, country, photo, portofolio, socials, skills, projects):
    with open("icons.json", "r") as json_file:
        icons = json.load(json_file)

    s = ""

    s = s + f"# Hello there\n\n<div align='center'>\n\t<img src='{photo}' width=50%, title='cover photo', alt='cover photo'>\n</div>\n\nI am {name},"

    if len(nick_name) > 0:
        s = s + f" (AKA {nick_name}),"

    s = s + f" a {age} year old {course} student from {university}, {country}."

    if len(work) > 0:
        if work[0] in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            work = "an " + work
        else:
            work = "a " + work
    if len(work) > 0 and len(company) > 0:
        s = s + f" I am {work} at {company}."
    elif len(work) > 0 and len(company) == 0:
        s = s + f" I am currently {work}."
    elif len(work) == 0 and len(company) > 0:
        s = s + f" I currently work in {company}."

    if len(portofolio) > 0:
        s = s + f"\n\nYou can know more about me here: <a href='{portofolio}' target='_blank'>{name}</a>"

    if len(set(list(socials.values()))) > 1:
        s = s + f"\n\n\n## Socials\n\n<div align='center'>\n"
        for social_key in socials:
            link = socials.get(social_key)
            if len(link) > 0:
                s = s + f"<a href='{link}' target='_blank'><img src='{icons['socials'][social_key]}'></a>\n"
        s = s + "</div>"

    if len(set(list(skills.values()))) > 1:
        s = s + f"\n\n\n## Skills"
        s = s + f"\n\n<div align='center'>\n"
        for skill_key in skills:
            link = skills.get(skill_key)
            if str(type(link)) != "<class 'NoneType'>":
                s = s + f"<img src='{icons['skills'][skill_key]}'>\n"
        s = s + "</div>"

    if len(set(list(projects.values()))) > 1:
        s = s + f"\n\n\n## Projects\n\n"
        for i in range(1, 6):
            project_name = projects.get(f"project_{i}_name")
            project_link = projects.get(f"project_{i}_link")
            if len(project_name) > 0 and len(project_link) > 0:
                s = s + f"- {project_name}: <a href='{project_link}' target='_blank'>{project_link}</a>\n"

    with open("asdf.md", "w") as f:
        f.write(s)

    return s
import json

from bs4 import BeautifulSoup

with open("./schedule.html") as f:
    text = f.read()
page_soup = BeautifulSoup(text, "html.parser")

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
times = ["1", "2", "3", "4", "5", "6"]

schedule_dict = {
    "Mon": {},
    "Tue": {},
    "Wed": {},
    "Thu": {},
    "Fri": {},
    "Sat": {},
    "Sun": {},
}


for day in days:
    for time in times:
        cell_id = f"ctl00_phContents_rrMain_ttTable_lct{day}{time}_ctl00_lblSbjName"
        soup = page_soup.find(id=cell_id)
        if soup is None:
            continue
        soup = soup.find("a")
        if soup is None:
            continue
        subj = next(soup.children)
        schedule_dict[day].update({time: {"title": subj, "room": ""}})

with open("./schedule.json", "w") as f:
    json.dump(schedule_dict, f, indent=1, ensure_ascii=False)

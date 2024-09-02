import json
chapters = json.load(open("chapters.json"))['chapters']

chapters_length = {}
for chapter in chapters:
    chapter_name = chapter['name_simple']
    start_page, end_page = chapter['pages']
    chapters_length[chapter_name] = end_page - start_page + 1 if start_page != end_page else 1

json.dump(chapters_length, open("chapters_length.json", "w"))

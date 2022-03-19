import json

new_songs = {}

with open ('new 1.txt', 'r', encoding="utf-8") as txt_file:
    lines = txt_file.readlines()

for line in lines:
    # print(line)
    if ('title:' in line):
        title = line.split(":")[1][1:].replace("\n", "")
        new_songs[title] = {"title": title}
    elif ('year:' in line):
        year = line.split(":")[1][1:].replace("\n", "")
        new_songs[title]["year"] = year
    elif ('origin:' in line):
        og = line.split(":")[1][1:].replace("\n", "")
        new_songs[title]["origin"] = og
        new_songs[title]['lines'] = ([])
    else:
        new_songs[title]['lines'].append(line.replace("\n", ""))

with open('./src/assets/songs.json', encoding="utf-8") as json_file:
    # print(json_file)
    data = json.load(json_file)

for key in new_songs:
    data[key] = new_songs[key]

with open('./src/assets/songs.json', 'w', encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

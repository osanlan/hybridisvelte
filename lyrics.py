from posixpath import split


print("HEI");
with open('songs.txt', 'r') as file:
    lines = file.readlines()
        
with open('songs.json', 'a') as file:
    file.write('[')
    id = 0
    for line in lines:
        if ('title:' in line):
            file.write(']},{\n')
            file.write('"id": ' + str(id) + ',\n')
            id += 1
            file.write('"title": "' + line.split(":")[1].replace("\n", "") + '",\n')
        elif ('speksi:' in line):
            file.write('"speksi": "' + line.split(":")[1].replace("\n", "") + '",\n')
        elif ('origin:' in line):
            file.write('"origin": "' + line.split(":")[1].replace("\n", "") + '",\n')
            file.write('"lines": [\n')
        else:
            file.write('"' + line.replace("\n", "") + '",\n')
        
    file.write('}')
    file.write(']')
import os

dir_path = 'files/notes'

notes = os.listdir(dir_path)

for note in notes:
    new_note = f"{note.split(' ')[0]}.md"
    os.rename(f"{dir_path}/{note}", f"{dir_path}/{new_note}")

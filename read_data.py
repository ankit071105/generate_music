#read all the filenames
files=[i for i in os.listdir() if i.endswith(".mid")]

#reading each midi file
all_notes=[]
for i in files:
  all_notes.append(read_midi(i))

#notes and chords of all the midi files
notes = [element for notes in all_notes for element in notes]
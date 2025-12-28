#length of a input sequence
no_of_timesteps = 128      

#no. of unique notes
n_vocab = len(set(notes))  

#all the unique notes
pitch = sorted(set(item for item in notes))  

#assign unique value to every note
note_to_int = dict((note, number) for number, note in enumerate(pitch))  

#preparing input and output sequences
X = []
y = []
for notes in all_notes:
  for i in range(0, len(notes) - no_of_timesteps, 1):
    input_ = notes[i:i + no_of_timesteps]
    output = notes[i + no_of_timesteps]
    X.append([note_to_int[note] for note in input_])
    y.append(note_to_int[output])
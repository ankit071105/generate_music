def read_midi(file):
  notes=[]
  notes_to_parse = None

  #parsing a midi file
  midi = converter.parse(file)
  #grouping based on different instruments
  s2 = instrument.partitionByInstrument(midi)

  #Looping over all the instruments
  for part in s2.parts:
    #select elements of only piano
    if 'Piano' in str(part): 
      notes_to_parse = part.recurse() 
      #finding whether a particular element is note or a chord
      for element in notes_to_parse:
        if isinstance(element, note.Note):
          notes.append(str(element.pitch))
        elif isinstance(element, chord.Chord):
          notes.append('.'.join(str(n) for n in element.normalOrder))
      
  return notes
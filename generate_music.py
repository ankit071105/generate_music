def generate_music(model, pitch, no_of_timesteps, pattern):
    
    int_to_note = dict((number, note) for number, note in enumerate(pitch))
    prediction_output = []
    
    # generate 50 elements
    for note_index in range(50):
        #reshaping array to feed into model
        input_ = np.reshape(pattern, (1, len(pattern), 1))
        #predict the probability and choose the maximum value
        proba = model.predict(input_, verbose=0)
        index = np.argmax(proba)
        #convert integer back to the element
        pred = int_to_note[index]
        prediction_output.append(pred)
        pattern = list(pattern)
        pattern.append(index/float(n_vocab))
        #leave the first value at index 0
        pattern = pattern[1:len(pattern)]

    return prediction_output



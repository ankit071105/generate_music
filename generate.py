#Select random chunk for the first iteration
start = np.random.randint(0, len(X)-1)
pattern = X[start]
#load the best model
model=load_model('model300.h5')
#generate and save music
music = generate_music(model,pitch,no_of_timesteps,pattern)
convert_to_midi(music)
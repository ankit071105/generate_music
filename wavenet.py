K.clear_session()
def simple_wavenet():
  no_of_kernels=64
  num_of_blocks= int(np.sqrt(no_of_timesteps)) - 1   #no. of stacked conv1d layers

  model = Sequential()
  for i in range(num_of_blocks):
    model.add(Conv1D(no_of_kernels,3,dilation_rate=(2**i),padding='causal',activation='relu'))
  model.add(Conv1D(1, 1, activation='relu', padding='causal'))
  model.add(Flatten())
  model.add(Dense(128, activation='relu'))
  model.add(Dense(n_vocab, activation='softmax'))
  model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
  return model
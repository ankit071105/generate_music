import keras
mc = keras.callbacks.ModelCheckpoint('model{epoch:03d}.h5', save_weights_only=False, period=50)

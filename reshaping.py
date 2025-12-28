#reshaping
X = np.reshape(X, (len(X), no_of_timesteps, 1))
#normalizing the inputs
X = X / float(n_vocab)   
model = simple_wavenet()
model.fit(X,np.array(y), epochs=300, batch_size=128,callbacks=[mc])

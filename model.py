from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Dropout, Flatten, Input, MaxPooling2D

def create():
	model = Sequential()
	# model.add(Conv2D(filters=128 , kernel_size=3 , activation="relu", input_shape=(100,100,3)  ))
	model.add(Input(shape=(100,100,3)))
	model.add(Conv2D(filters=128 , kernel_size=3 , activation="relu"))
	model.add(MaxPooling2D())
	model.add(Conv2D(filters=64, kernel_size=3 , activation="relu"))
	model.add(Conv2D(filters=32, kernel_size=3 , activation="relu"))
	model.add(MaxPooling2D())
	model.add(Dropout(0.5))
	model.add(Flatten())
	model.add(Dense(5000, activation="relu"))
	model.add(Dense(1000, activation="relu"))
	model.add(Dense(131,activation="softmax"))

	model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])

	return model
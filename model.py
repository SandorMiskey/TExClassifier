from tensorflow.keras.layers import Conv2D, Dense, Dropout, Flatten, Input, MaxPooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
# from tensorflow.keras.optimizers.legacy import Adam

def create():
	model = Sequential()
	model.add(Input(shape=(100,100,3)))
	model.add(Conv2D(filters=128 , kernel_size=3 , activation="relu"))
	# model.add(Conv2D(filters=128 , kernel_size=3 , activation="relu", input_shape=(100,100,3)))
	model.add(MaxPooling2D())
	model.add(Conv2D(filters=64, kernel_size=3 , activation="relu"))
	model.add(Conv2D(filters=32, kernel_size=3 , activation="relu"))
	model.add(MaxPooling2D())
	model.add(Dropout(0.5))
	model.add(Flatten())
	# model.add(Dense(5000, activation="relu"))	# model might be too complex for the task, especially with the dense layers of 5000 and 1000 neurons. This can lead to
	# model.add(Dense(1000, activation="relu"))	# overfitting, where the model learns the noise in the training data instead of the underlying pattern. Try 1024 & 512
	model.add(Dense(1024, activation="relu"))
	model.add(Dense(512, activation="relu"))
	model.add(Dense(131, activation="softmax"))

	# model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])
	model.compile(loss="categorical_crossentropy", optimizer=Adam(learning_rate=0.001), metrics=["accuracy"])

	return model
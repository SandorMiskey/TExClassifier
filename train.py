# region: packages

import common as c
import importlib
import numpy as np
from keras.callbacks import EarlyStopping
from keras.preprocessing.image import ImageDataGenerator

# endregion
# region: const

LOG_SEVERITY_KEY = "LOG_SEVERITY"

PATH_MODEL_KEY = "PATH_MODEL"
PATH_TRAINING_KEY = "PATH_TRAINING"
PATH_TEST_KEY = "PATH_TEST"

TRAIN_BATCHSIZE_KEY = "TRAIN_BATCHSIZE"
TRAIN_BATCHSIZE_VALUE = 64
TRAIN_EPOCHS_KEY = "TRAIN_EPOCHS"
TRAIN_EPOCHS_VALUE = 50
TRAIN_MODEL_KEY = "TRAIN_MODEL"
TRAIN_MODEL_VALUE = "model"
TRAIN_STOPPING_KEY = "TRAIN_STOPPING"
TRAIN_STOPPING_VALUE = 7

# endregion
# region: model

c.env.setdefault(TRAIN_MODEL_KEY, TRAIN_MODEL_VALUE)
c.env[TRAIN_BATCHSIZE_KEY] = int(c.env.get(TRAIN_BATCHSIZE_KEY, TRAIN_BATCHSIZE_VALUE))
c.env[TRAIN_EPOCHS_KEY] = int(c.env.get(TRAIN_EPOCHS_KEY, TRAIN_EPOCHS_VALUE))
c.logger.debug(f"{TRAIN_MODEL_KEY}: {c.env.get(TRAIN_MODEL_KEY)}")

c.logger.info("compiling model")
module = importlib.import_module(c.env.get(TRAIN_MODEL_KEY))
model = module.create()
model.summary() if c.verbose == 1 else None
c.logger.info(f"model compiled")

# endregion
# region: load data

c.logger.debug(f"{TRAIN_BATCHSIZE_KEY}: {c.env.get(TRAIN_BATCHSIZE_KEY)}")

c.logger.info("loading training data")
train_gen = ImageDataGenerator(
	# height_shift_range=0.2,
	horizontal_flip=True,
	rescale = 1./255,
	# rotation_range=20,
	shear_range=0.3,
	vertical_flip=True,
	# width_shift_range=0.2,
	zoom_range=0.3)
train_flow = train_gen.flow_from_directory(
	c.env[PATH_TRAINING_KEY],
	batch_size=c.env[TRAIN_BATCHSIZE_KEY],
	class_mode="categorical",
	color_mode="rgb",
	shuffle=True,
	target_size=(100,100))
# train_steps = np.ceil(train_flow.samples / c.env[TRAIN_BATCHSIZE_KEY])
train_steps = int(np.ceil(train_flow.samples // c.env[TRAIN_BATCHSIZE_KEY]))

c.logger.info(f"loading validation data")
validation_gen = ImageDataGenerator(rescale= 1./255)
validation_flow = validation_gen.flow_from_directory(
	c.env[PATH_TEST_KEY],
	class_mode="categorical",
	color_mode="rgb",
	batch_size=c.env[TRAIN_BATCHSIZE_KEY],
	target_size=(100,100))
# validation_steps = np.ceil(validation_flow.samples / c.env[TRAIN_BATCHSIZE_KEY])
validation_steps = int(np.ceil(validation_flow.samples // c.env[TRAIN_BATCHSIZE_KEY]))

c.logger.debug(f"train_steps: {train_steps}, validation_steps: {validation_steps}")

# endregion
# region: training

c.logger.debug(f"{TRAIN_EPOCHS_KEY}: {c.env.get(TRAIN_EPOCHS_KEY)}, {TRAIN_STOPPING_KEY}: {c.env.get(TRAIN_STOPPING_KEY)}")
c.logger.info("training the model")
stopping = EarlyStopping(monitor="val_accuracy", patience=int(c.env.get(TRAIN_STOPPING_KEY, TRAIN_STOPPING_VALUE)))
history = model.fit(
	train_flow,
	callbacks=[stopping],
	epochs=c.env[TRAIN_EPOCHS_KEY],
	# max_queue_size=4,
	steps_per_epoch=train_steps,
	# use_multiprocessing=True, 
	validation_data=validation_flow,
	validation_steps=validation_steps
	# workers=4
	)
model.save(c.env[PATH_MODEL_KEY])
c.logger.debug(f"fit history: {history}")
c.logger.info("all done, gg")

# endregion

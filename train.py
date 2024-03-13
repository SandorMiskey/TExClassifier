# region: packages

import common as c
import importlib
import numpy as np
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# endregion
# region: const

PATH_MODEL_KEY = "PATH_MODEL"
PATH_TRAINING_KEY = "PATH_TRAINING"
PATH_TEST_KEY = "PATH_TEST"

TRAIN_BATCHSIZE_KEY = "TRAIN_BATCHSIZE"
TRAIN_BATCHSIZE_VALUE = 64
TRAIN_EPOCHS_KEY = "TRAIN_EPOCHS"
TRAIN_EPOCHS_VALUE = 50
TRAIN_MODEL_KEY = "TRAIN_MODEL"
TRAIN_MODEL_VALUE = "model"

# endregion
# region: model

c.env.setdefault(TRAIN_MODEL_KEY, TRAIN_MODEL_VALUE)
c.env[TRAIN_BATCHSIZE_KEY] = int(c.env.get(TRAIN_BATCHSIZE_KEY, TRAIN_BATCHSIZE_VALUE))
c.env[TRAIN_EPOCHS_KEY] = int(c.env.get(TRAIN_EPOCHS_KEY, TRAIN_EPOCHS_VALUE))
c.logger.debug(f"{TRAIN_MODEL_KEY}: {c.env.get(TRAIN_MODEL_KEY)}")

c.logger.info("compiling model")
module = importlib.import_module(c.env.get(TRAIN_MODEL_KEY))
model = module.create()
c.logger.info(f"model compiled")

# endregion
# region: load data

c.logger.info("loading training data")
train_gen = ImageDataGenerator(rescale = 1./255, shear_range=0.3, horizontal_flip=True, vertical_flip=True, zoom_range=0.3)
train_flow = train_gen.flow_from_directory(c.env[PATH_TRAINING_KEY],
										   target_size=(100,100),
										   batch_size=c.env[TRAIN_BATCHSIZE_KEY],
										   color_mode="rgb",
										   class_mode="categorical",
										   shuffle=True
										  )
train_steps = int(np.ceil(train_flow.samples // c.env[TRAIN_BATCHSIZE_KEY]))

c.logger.info(f"loading validation data")
validation_gen = ImageDataGenerator(rescale= 1./255)
validation_flow = validation_gen.flow_from_directory(c.env[PATH_TEST_KEY],
										 target_size=(100,100),
										 batch_size=c.env[TRAIN_BATCHSIZE_KEY],
										 color_mode="rgb",
										 class_mode="categorical"
										)
validation_steps = int(np.ceil(validation_flow.samples // c.env[TRAIN_BATCHSIZE_KEY]))

c.logger.debug(f"{TRAIN_BATCHSIZE_KEY}: {c.env.get(TRAIN_BATCHSIZE_KEY)}, train_steps: {train_steps}, validation_steps: {validation_steps}")

# endregion
# region: training

c.logger.debug(f"{TRAIN_EPOCHS_KEY}: {c.env.get(TRAIN_EPOCHS_KEY)}")
c.logger.info("training the model")
stop_early = EarlyStopping(monitor="val_accuracy", patience=5)
history = model.fit(train_flow,
                    steps_per_epoch=train_steps,
                    epochs=c.env[TRAIN_EPOCHS_KEY],
                    validation_data=validation_flow,
                    validation_steps=validation_steps,
                    callbacks=[stop_early])
model.save(c.env[PATH_MODEL_KEY])
c.logger.debug(f"fit history: {history}")
c.logger.info("all done, gg")

# endregion

# region: packages

import common as c
import cv2
from keras.utils import img_to_array , load_img
from keras.models import load_model
import numpy as np
import pickle
import tensorflow

# endregion
# region: const

LOG_SEVERITY_KEY = "LOG_SEVERITY"
PATH_CATEGORIES_KEY = "PATH_CATEGORIES"
PATH_MODEL_KEY = "PATH_MODEL"
# PATH_TRAINING_KEY = "PATH_TRAINING"
# PATH_TEST_KEY = "PATH_TEST"

# endregion
# region: model

# model = tensorflow.keras.models.load_model(c.env[PATH_MODEL_KEY])
model = load_model(c.env[PATH_MODEL_KEY])
model.summary() if c.verbose == 1 else None
c.logger.debug(f"tensorflow version: {tensorflow.__version__}")
c.logger.info(f"model has been loaded ({c.env[PATH_MODEL_KEY]})")

# endregion
# region: categories

with open(c.env[PATH_CATEGORIES_KEY], 'rb') as f:
    categories = pickle.load(f)
c.logger.debug(categories)
c.logger.info(f"dataset has been loaded with {len(categories)} items")

# endregion
# region: load file

img_file = "data/eggplant.jpg"
img_raw = load_img(img_file, target_size=(100,100))
img_arr = img_to_array(img_raw)
c.logger.debug(img_arr.shape)
img_arr = np.expand_dims(img_arr , axis = 0) 
c.logger.debug(img_arr.shape)
img_arr = img_arr / 255
c.logger.info(f"{img_file} has been prepared")

# endregion
# region: predict

result = model.predict(img_arr, verbose=c.verbose)
answers = np.argmax(result, axis = 1)
print(answers[0])
text = categories[answers[0]]
print("Predicted image : "+ text)

cv2.imshow(text, cv2.imread(img_file))
cv2.waitKey(0)
cv2.destroyAllWindows()

# endregion

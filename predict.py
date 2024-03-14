# region: packages

import common as c
import cv2
from keras.utils import img_to_array , load_img
from keras.models import load_model
import numpy as np
import os
import pickle
import random
import sys
import tensorflow

# endregion
# region: const

LOG_SEVERITY_KEY = "LOG_SEVERITY"

PATH_CATEGORIES_KEY = "PATH_CATEGORIES"
PATH_MODEL_KEY = "PATH_MODEL"
PATH_VALIDATION_KEY = "PATH_TEST"

# endregion
# region: model

# model = tensorflow.keras.models.load_model(c.env[PATH_MODEL_KEY])
model = load_model(c.env[PATH_MODEL_KEY])
model.summary() if c.verbose == 1 else None
c.logger.debug(f"tensorflow version: {tensorflow.__version__}")
c.logger.info(f"model has been loaded ({c.env[PATH_MODEL_KEY]})")

# endregion
# region: classes

with open(c.env[PATH_CATEGORIES_KEY], 'rb') as f:
    classes = pickle.load(f)
    classes.sort()
c.logger.debug(classes)
c.logger.info(f"dataset has been loaded with {len(classes)} items")

# endregion
# region: load sample

img_path = None
if len(sys.argv) > 1:
    img_path = sys.argv[1]
else:
    dir = c.env.get(PATH_VALIDATION_KEY, "data/test")
    if os.path.exists(dir):
        cs = [entry for entry in os.listdir(dir) if not entry.startswith('.')]
        cs_path = os.path.join(dir, random.choice(cs))
        files = os.listdir(cs_path)
        img_path = os.path.join(cs_path, random.choice(files))
    else:
        c.logger.critical(f"Directory {dir} does not exist.")
        sys.exit(1)
c.logger.debug(f"image path: {img_path}")

img_raw = load_img(img_path, target_size=(100,100))
img_arr = img_to_array(img_raw)
c.logger.debug(f"img_arr.shape: {img_arr.shape}")
img_arr = np.expand_dims(img_arr , axis = 0) 
c.logger.debug(f"img_arr.shape: {img_arr.shape}")
img_arr = img_arr / 255
c.logger.info(f"{img_path} has been prepared")

# endregion
# region: predict

result = model.predict(img_arr, verbose=c.verbose)
answers = np.argmax(result, axis = 1)
text = classes[answers[0]]
print(text)
if c.verbose == 1:
    c.logger.debug("category: #" + str(answers[0]))
    c.logger.debug("accuracy: " + str(result[0][answers[0]]))

    # img = cv2.imread(img_path)
    # cv2.namedWindow(text, cv2.WINDOW_NORMAL)
    # cv2.resizeWindow(text, 600, 600)
    # cv2.imshow(text, img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# endregion

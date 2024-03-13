# region: packages

import common as c
import os
import pickle

# endregion
# region: const

# LOG_SEVERITY_KEY = "LOG_SEVERITY"
# PATH_MODEL_KEY = "PATH_MODEL"
# PATH_TRAINING_KEY = "PATH_TRAINING"
PATH_TEST_KEY = "PATH_TEST"
PATH_CATEGORIES_KEY = "PATH_CATEGORIES"

# endregion

categories = [entry for entry in os.listdir(c.env[PATH_TEST_KEY]) if not entry.startswith('.')]
categories.sort()
c.logger.debug(categories)

with open(c.env[PATH_CATEGORIES_KEY], 'wb') as f:
	pickle.dump(categories, f)
c.logger.info(f"dataset saved with {len(categories)} items")

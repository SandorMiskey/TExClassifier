#
# .env template file, rename or symlink it, and set the appropriate values
#
# region: PATH

export PATH_BASE=/Volumes/TExClassifier
export PATH_TRAINING=${PATH_BASE}/data/training
export PATH_TEST=${PATH_BASE}/data/test
export PATH_WORKBENCH=${PATH_BASE}/workbench
export PATH_VENV=${PATH_WORKBENCH}/venv
export PATH_MODEL=${PATH_WORKBENCH}/model.keras
export PATH_CATEGORIES=${PATH_WORKBENCH}/categories.pkl
export PATH_PYTHON=$(which python3.9)

export PATH=${PATH_VENV}/bin:/opt/homebrew/bin:$PATH

# endregion
# region: log

export LOG_SEVERITY="WARNING"
export LOG_FORMAT="<green>{time}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
export LOG_SINK="sys.stdout"

# 0 = all messages are logged (default behavior)
# 1 = INFO messages are not printed
# 2 = INFO and WARNING messages are not printed
# 3 = INFO, WARNING, and ERROR messages are not printed
export TF_CPP_MIN_LOG_LEVEL=1

# endregion
# region: ml

export TRAIN_BATCHSIZE=64
export TRAIN_EPOCHS=100
export TRAIN_MODEL="model"
export TRAIN_STOPPING=10

# endregion
# region: gum

# generic
export GUM_BOLD="#F0EE54"
export GUM_NORM="#00FA92"
export GUM_PREFIX="==> "

# choose
export GUM_CHOOSE_TIMEOUT=0
export GUM_CHOOSE_CURSOR_FOREGROUND=$GUM_BOLD
export GUM_CHOOSE_HEADER_FOREGROUND=$GUM_BOLD
export GUM_CHOOSE_ITEM_FOREGROUND=$GUM_NORM
export GUM_CHOOSE_SELECTED_FOREGROUND=$GUM_BOLD
export GUM_CHOOSE_CURSOR=$GUM_PREFIX

# confirm
export GUM_CONFIRM_TIMEOUT=0
export GUM_CONFIRM_PROMPT_FOREGROUND=$GUM_BOLD
export GUM_CONFIRM_SELECTED_FOREGROUND=$GUM_NORM
export GUM_CONFIRM_SELECTED_BACKGROUND=$GUM_BOLD
export GUM_CONFIRM_UNSELECTED_FOREGROUND=$GUM_NORM

# input
export GUM_INPUT_CURSOR_FOREGROUND=$GUM_BOLD
export GUM_INPUT_PROMPT_FOREGROUND=$GUM_BOLD
export GUM_INPUT_PLACEHOLDER="your input goes here..."
export GUM_INPUT_PROMPT=$GUM_PREFIX
export GUM_INPUT_WIDTH=80

# spin
export GUM_SPIN_SPINNER=points
export GUM_SPIN_SHOW_OUTPUT=true
export GUM_SPIN_ALIGN=left
export GUM_SPIN_SPINNER_WIDTH=$((${#GUM_PREFIX} -1 ))
export GUM_SPIN_TIMEOUT=0
export GUM_SPIN_SPINNER_FOREGROUND=$GUM_BOLD
export GUM_SPIN_TITLE_FOREGROUND=$GUM_NORM
export GUM_SPIN_SPINNER_MARGIN="0 0"
export GUM_SPIN_SPINNER_PADDING="0 0"
export GUM_SPIN_TITLE_MARGIN="0 0"
export GUM_SPIN_TITLE_PADDING="0 0"

# style
export ALIGN=center
export BOLD=true
export BORDER=rounded
export BORDER_FOREGROUND=$GUM_BOLD
export FOREGROUND=$GUM_BOLD
export MARGIN="1 2"
export PADDING="2 4"
export UNDERLINE=true
export WIDTH=80

# endregion: gum

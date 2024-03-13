.DEFAULT_GOAL := build
REQUIRED_VARIABLES := PATH_PYTHON PATH_VENV PATH_WORKBENCH

all: train
clean: dep_external
	@gum style 'THIS TARGET CAN BE DESTRUCTIVE' 'IT SHOULD BE RUN WITH SPECIAL CARE'
	@gum confirm "do you want to proceed?" || exit 1
	@gum confirm "is PATH_WORKBENCH == ${PATH_WORKBENCH} correct?" || exit 1
	@if [ ! -d ${PATH_WORKBENCH} ]; then \
		echo "${GUM_PREFIX}${PATH_WORKBENCH} does not exist"; \
	else \
		gum spin --title "removing ${PATH_WORKBENCH}/*" -- find "${PATH_WORKBENCH}" -mindepth 1 -delete; \
	fi
	@echo "${GUM_PREFIX}${PATH_WORKBENCH} is clean"
dep:
	@echo "${GUM_PREFIX}checkig for env variables"
	$(foreach var,$(REQUIRED_VARIABLES),$(if $(value $(var)),,$(error $(GUM_PREFIX) $(var) is not set, load $(ENV) before running make)))
	@$(MAKE) dep_external
	@$(MAKE) dep_venv
	@echo "${GUM_PREFIX}all dependencies are inplace"
dep_external:
	@echo "${GUM_PREFIX}checkig for expternal dependencies"
	@printf `which gum`": "
	@gum --version
	@printf "${PATH_PYTHON}: "
	@${PATH_PYTHON} --version 
dep_venv:
	@echo "${GUM_PREFIX}checkig for python venv"
	@${PATH_VENV}/bin/pip3 --version
init: dep_external
	@echo "${GUM_PREFIX}setting python3 venv"
	@gum confirm "is PATH_VENV == ${PATH_VENV} correct?" || exit 1
	@${PATH_PYTHON} -m venv ${PATH_VENV}
	@. ${PATH_VENV}/bin/activate && ${PATH_VENV}/bin/pip3 install -U pip
	@. ${PATH_VENV}/bin/activate && ${PATH_VENV}/bin/pip3 install -r requirements.txt
categories: dep
	@${PATH_VENV}/bin/python prepare.py
predict: dep
	@${PATH_VENV}/bin/python predict.py
train: dep
	@${PATH_VENV}/bin/python train.py

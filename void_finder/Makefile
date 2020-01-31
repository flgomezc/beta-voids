SHELL := /bin/bash  # Use bash Syntax

BETA=1   # Beta for the Beta Skeleton. BETA >= 1.0
R=1      # ratio "r" between random_points/catalog_points.
         # Tested working range:  1.0 <= R <= 1.4
SEED=1   # Random seed. Integer.

OC_PATH=./original_catalogs/
RC_PATH=./random_catalogs/
FC_PATH=./full_catalogs/
ML_PATH=./masterlists/
VE_PATH=./volume_and_excentricity/
BS_PATH=./xdl_beta_skeleton/        # To store beta-skeleton of FC



all: folders main_sequence
	@echo Make All

folders:
	@echo  ...
	@echo   Making the working directories.
	@echo   Place the INPUT_CATALOG catalog inside 'original_catalogs/'
	@echo ...  
	mkdir -p $(OC_PATH)
	mkdir -p $(RC_PATH)
	mkdir -p $(FC_PATH)
	mkdir -p $(ML_PATH)
	mkdir -p $(VE_PATH)
	mkdir -p $(BS_PATH)

main_sequence:
	@echo ... Main Sequence
	python calculate_beta_skeleton.py   $(INPUT_CATALOG) $(OUTPUT_NAME) --beta $(BETA) --nrand $(R) --seed $(SEED)
	python void_identifier_recursion.py $(INPUT_CATALOG) $(OUTPUT_NAME) --beta $(BETA) --nrand $(R) --seed $(SEED)
	python ellipsoid_analysis.py        $(INPUT_CATALOG) $(OUTPUT_NAME) --beta $(BETA) --nrand $(R) --seed $(SEED)

test: folders
	@echo ... Running the Test Sequence
	python calculate_beta_skeleton.py   100_Mpch_box test --beta $(BETA) --nrand $(R) --seed $(SEED)
	python void_identifier_recursion.py 100_Mpch_box test --beta $(BETA) --nrand $(R) --seed $(SEED)
	python ellipsoid_analysis.py        100_Mpch_box test --beta $(BETA) --nrand $(R) --seed $(SEED)

clean:
	@echo ... Removing all the directories, but "./original_catalogs/"
	rm -r $(RC_PATH)
	rm -r $(FC_PATH)
	rm -r $(ML_PATH)
	rm -r $(VE_PATH)
	rm -r $(BS_PATH)
	rm progress* # TODO: make a new log folder and store all this stuff there.

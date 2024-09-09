INPUT_FILE_LIST:=$(shell ls inputs/)
INPUT_FILES=$(foreach FILE,$(INPUT_FILE_LIST),inputs/$(FILE))
INTERMEDIATE_STAGE_FILES=$(INPUT_FILES:inputs/%=%)

#RULE 0: this is ok
all: combined_outputs.txt

#RULE 1:
#the wildcard variable should not be needed here
#should use dependencies
combined_outputs.txt: $(INTERMEDIATE_STAGE_FILES)
	cat $(wildcard outputs/*) >> $@
	shuf combined_outputs.txt -o combined_outputs.txt

#RULE 2:
#note that this is not a pattern rule - this is two variables with substitution references
#both pattern rules and substitution references in variables use the % symbol, but are not the same thing
#both commands are run in one rule, when these should be split into two separate stages with different rules since they both generate outputs
#hardcoded filepaths should not be added in the commands being run, since this leads to the Makefile not actually tracking the presence of inputs/outputs
#inputs and outputs should not all be using the target value ($@) - this was used here because the dependency value doesn't change in this current setup
#the dependency value stays the same in all iterations because it's a long list of filenames returned by `wildcard`. The first filename in this list would always used for $< here.
#input and output files should not have the same names - even if the filepaths are different, files with the same names can cause confusion
$(INTERMEDIATE_STAGE_FILES): $(INPUT_FILES)
	python3 scripts/add_words.py inputs/$@ > intermediate_stage/$@
	python3 scripts/add_even_more_words.py intermediate_stage/$@ > outputs/$@


#CLEAN RULE
#clean rules should use variable names, not hardcoded filepaths with wildcards
clean:
	rm intermediate_stage/*
	rm outputs/*
	rm combined_outputs.txt

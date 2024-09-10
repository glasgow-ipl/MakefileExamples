# The following should be:
#   INPUT_FILES = $(wildcard inputs/*)
# although unless there are a large number of files it's better to 
# just explicitly list the filenames in the Makefile.
INPUT_FILE_LIST:=$(shell ls inputs/)
INPUT_FILES=$(foreach FILE,$(INPUT_FILE_LIST),inputs/$(FILE))

INTERMEDIATE_STAGE_FILES=$(INPUT_FILES:inputs/%=%)

# RULE 0: this is ok
all: combined_outputs.txt

# RULE 1:
# 
# This rule states that the target combined_outputs.txt depends on
# $(INTERMEDIATE_STAGE_FILES) as prerequisities, but none of the 
# lines in the recipe uses $(INTERMEDIATE_STAGE_FILES) directly or
# indirectly (via $^ or $<). That's a sign that either the recipe
# or dependencies are incorrect.
#
# Second, reading and writing the same file multiple times in a
# rule is problematic:
# a) If the cat command succeeds but shuf fails without writing
#    any output, the combined_outputs.txt file will still have been
#    modified so make will think this command has succeeded.
# b) While shuf might be safe to run in this manner, many commands
#    fail using the same file as input and output.
# c) The rule uses a mix of combined_outputs.txt and $@ to refer to
#    the same output file, and would be better to consistently use $@.
#
# Overall, this rule would be better written something like:
#   combined_outputs.txt: $(INTERMEDIATE_STAGE_FILES)
#     cat $^ >> $@.tmp
#     shuf $@.tmp -o $@
#     rm $@.tmp
#
# or perhaps:
#   combined_outputs.txt: $(INTERMEDIATE_STAGE_FILES)
#     cat $^ | shuf -o $@
#
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
#
# The dependencies should include the Python scripts, so if the script
# is changed the output files are recreated.
$(INTERMEDIATE_STAGE_FILES): $(INPUT_FILES)
	python3 scripts/add_words.py inputs/$@ > intermediate_stage/$@
	python3 scripts/add_even_more_words.py intermediate_stage/$@ > outputs/$@


#CLEAN RULE
#clean rules should use variable names, not hardcoded filepaths with wildcards
clean:
	rm intermediate_stage/*
	rm outputs/*
	rm combined_outputs.txt

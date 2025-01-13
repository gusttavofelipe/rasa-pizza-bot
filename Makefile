train:
	@cd bot \
	&& rasa train

shell:
	@cd bot \
	&& rasa shell

tests:
	@cd bot \
	&& rasa test

actions:
	@cd bot \
	&& uv run python environ.py \
	&& rasa run actions 

run:
	@cd bot \
	&& uv run python environ.py \
	&& rasa run --enable-api --cors "*"

pycache:
	@echo "Running Clean Pycache..."
	@find . \( -name *.py[co] -o -name __pycache__ \) -delete

train:
	@cd pizzabot && rasa train

shell:
	@cd pizzabot && rasa shell

test:
	@cd pizzabot && rasa test

actions:
	@cd pizzabot && rasa run actions

run:
	@cd pizzabot && rasa run --enable-api --cors "*"

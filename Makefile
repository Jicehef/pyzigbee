# Copyright (C) 2015 Legrand France
# All rights reserved

# Simple makefile for pyzigbee development

test:
	PYTHONPATH=. nosetests -v

doc:
	cd docs && PYTHONPATH=.. make html && cd ..
	@echo "Open docs/_build/html/index.html with your favourite browser"docs/_build/html/index.html
	@echo
	@echo "sensible-browser docs/_build/html/index.html &"
	@echo

clean:
	make -C docs clean
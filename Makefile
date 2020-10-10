PYTHON_PACKAGE_NAME = StudyDjango

VIRTUALENV ?= env
PYTHONVERSION ?= python3
PYTHON = $(VIRTUALENV)/bin/$(PYTHONVERSION)

$(VIRTUALENV): requirements.txt
	$(PYTHONVERSION) -m venv $@
	$(PYTHON) -m pip install -r $<
	. "$@/bin/activate"

.PHONY: clean
clean:
	find . -name "*.py[co]" -delete
	rm -r $(VIRTUALENV)

.PHONY: test
test: $(VIRTUALENV)
	$(TESTRUNNER) $(TESTRUNNERFLAGS)

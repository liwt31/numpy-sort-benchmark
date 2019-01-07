default: run
.PHONY: run

run:
	for dtype in numeric string generic; do \
		for stype in sort argsort; do \
		    fname=$${dtype}_$${stype}; \
			python $$fname.py > $$fname.txt; \
		done \
	done \

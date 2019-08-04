SHELL = /usr/bin/zsh
MAKEFLAGS += -rR

WEBDIR=/mit/sashacf/web_scripts/portfolio

MAGIC=../magic_latex.py

all: emilycf.pdf

%_install: %.html %.pdf
	cp $< $(WEBDIR)/includes/resume.html
	cp $(word 2,$^) $(WEBDIR)/documents/resume.pdf

% : %.html %.pdf;

%.pdf: %.tex
	latexmk -pdf $<

%.html %.tex :: %.yaml
	$(MAGIC) $(basename $<)

.PRECIOUS: %.html %.pdf

.PHONY: clean distclean

clean: distclean
	rm -f $(wildcard *.html) $(wildcard *.pdf)

distclean:
	rm -f $(wildcard *.aux) $(wildcard *.fdb_latexmk) $(wildcard *.fls) $(wildcard *.log) $(wildcard *.tex)

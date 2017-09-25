MAKEFLAGS += -rR

WEBDIR=/mit/sashacf/web_scripts/portfolio

%_install: %.html %.pdf
	cp $< $(WEBDIR)/includes/resume.html
	cp $(word 2,$^) $(WEBDIR)/documents/resume.pdf

% : %.html %.pdf;

%.pdf: %.tex
	latexmk -pdf $<
	rm $(basename $<).{aux,fdb_latexmk,fls,log}

%.html %.tex :: %.json
	./magic_latex.py $(basename $<)

.PRECIOUS: %.html

.PHONY: clean distclean

clean:
	rm *.{aux,fdb_latexmk,fls,html,log,pdf,tex}

distclean:
	rm *.{aux,fdb_latexmk,fls,log,tex}

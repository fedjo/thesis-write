#
# Description: A simple Makefile for xelatex compilation.
#
# File: Makefile
# Author: Bliablias Dimitris <bl.dimitris@gmail.com>
#
# Usage: Set TARGET name.
#

.PHONY : ps all clean view spellcheck

VIEWER := xpdf
TARGET := thesis
LATEX := xelatex

# make pdf by default
all: ${TARGET}.pdf

view: ${TARGET}.pdf
	$(VIEWER) $<

# it doesn't really need the .dvi, but this way all the refs are right
%.pdf : %.dvi
	$(LATEX) -shell-escape $*

${TARGET}.bbl: references.bib
	$(LATEX) -shell-escape ${TARGET}.tex
	# get the citations out of the bibliography
	bibtex ${TARGET}
	# do it again in case there are out-of-order cross-references
	@$(LATEX) -shell-escape ${TARGET}.tex

${TARGET}.dvi: ${TARGET}.bbl ${TARGET}.tex
	@$(LATEX) -shell-escape ${TARGET}.tex

# shortcut, so we can say "make ps"
# ps: ${TARGET}.ps

# ${TARGET}.ps: ${TARGET}.dvi
#	@dvips -t a4 ${TARGET}.dvi

clean:
	$(RM) *.aux *.ps *.dvi *.bbl *.blg *.lol *.lot *.lof *.log *.out *.toc *~

distclean: clean
	$(RM) $(TARGET).pdf

spellcheck:
	for file in *.tex ; do \
		aspell -d el -t check $$file ; \
	done
	aspell -d el -t check abstract.tex

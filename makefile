all: ctd

ctd: ctd.pdf

ctd.pdf: ctd.ps
	ps2pdf ctd.ps

ctd.ps: ctd.dvi
	dvips ctd.dvi -o ctd.ps

ctd.dvi: ctd.tex figures
	latex ctd.tex
	bibtex ctd
	latex ctd.tex
	latex ctd.tex

figures: forbidden_zone.eps

forbidden_zone.eps: forbidden_zone.py
	python forbidden_zone.py
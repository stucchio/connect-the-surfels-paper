all: ctd

ctd: ctd.pdf ctd.dvi

ctd.pdf: ctd.ps
	ps2pdf ctd.ps

ctd.ps: ctd.dvi
	dvips ctd.dvi -o ctd.ps

ctd.dvi: ctd.tex figures
	latex ctd.tex
	bibtex ctd
	latex ctd.tex
	latex ctd.tex

figures: forbidden_zone.eps forbidden_zone_noisy.eps polygonalization_example.eps tangents_good_for.eps assumption_two.eps example1.eps noisy_example.eps more_noisy_example.eps obscured_figure.eps

forbidden_zone.eps: forbidden_zone.py
	python forbidden_zone.py

forbidden_zone_noisy.eps: forbidden_zone.py
	python forbidden_zone.py

polygonalization_example.eps: polygonalization_example.py misc.py
	python polygonalization_example.py

tangents_good_for.eps: tangents_good_for.py
	python tangents_good_for.py

assumption_two.eps: assumption_two.py
	python assumption_two.py

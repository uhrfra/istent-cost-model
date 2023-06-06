#!/usr/bin/gnuplot

set xlabel "total time of treatment [years]"
set ylabel "total costs [EUR]"
set xrange [0:35]
set yrange [0:25000]
set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"

plot 'plot_data/scatterplot_without_stent.data' using 3:2 with points lt rgb "red" lw 3 pt 6 title "conventional treatment",\
'plot_data/scatterplot_with_stent.data' using 3:2 with points lt rgb "#da2e2" lw 3 pt 6 title "iStent treatment"
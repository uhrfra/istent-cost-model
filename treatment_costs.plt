#!/usr/bin/gnuplot

set xlabel "treatment duration [years]"
set ylabel "average treatment costs [EUR]"
set xrange [0:25]
set yrange [0:13000]
set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
set xtics 2

plot 'plot_data/treatment_costs_with_stent_avg.data' with lines lt rgb "#da2e2" title "iStent treatment",\
'plot_data/treatment_costs_without_stent_avg.data' with lines lt rgb "red" title "conventional treatment"
set title 'Results on AT&T Facedatabase'
set ylabel 'Accuracy (%)'
set xlabel 'k -Nearest Neighbors'
set xrange [ 0 : 100 ] noreverse nowriteback

set terminal png
set output 'k10-att.png'

set style line 1 lc rgb "red"
set style line 2 lc rgb "green"
set style line 3 lc rgb "blue"
set style fill solid
set boxwidth 0.1

#f(x) = a*x + b
#f2(x) = c*x + d
#fit f(x) 'plot.csv' using 1:2 via a, b
#fit f2(x) 'plot.csv' using 1:3 via c, d

set datafile separator ','
set key autotitle columnhead
plot 'facerec-k10-att.csv' using 1:2 with lines, \
                        '' using 1:3 with lines, \
                        '' using 1:4 with lines

#plot 'facerec-k10-att.csv' using 1:3, f2(x)

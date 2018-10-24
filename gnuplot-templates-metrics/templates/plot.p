set title 'Testing plot'
set ylabel 'Stats'
set xlabel 'n'
set xrange [ 0 : 20 ] noreverse nowriteback

set terminal png
set output 'plot.png'

set style line 1 lc rgb "red"
set style line 2 lc rgb "green"
set style fill solid
set boxwidth 0.1

f(x) = a*x + b
f2(x) = c*x + d

set datafile separator ','
set key autotitle columnhead
fit f(x) 'plot.csv' using 1:2 via a, b
fit f2(x) 'plot.csv' using 1:3 via c, d
#plot 'plot.csv' using 1:2 with lines, \
#             '' using 1:3 with lines, f(x)
plot 'plot.csv' using 1:3, f2(x)

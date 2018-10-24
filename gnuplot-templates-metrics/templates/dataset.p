set title 'Requests per second'

set ylabel 'RPS (%)'
set xlabel 'Time'
set xtics rotate by 45
set xtics offset 0,-2
set timefmt '%Y-%m-%d %H:%M:%S'
set xdata time

set terminal png
set output 'rps.png'

set style line 1 lc rgb "red"
set style line 2 lc rgb "green"
set style fill solid
set boxwidth 0.1
set datafile separator ','
set key autotitle columnhead
plot 'input.csv' using 2:11 with boxes, \
              '' using 2:12 with boxes, \

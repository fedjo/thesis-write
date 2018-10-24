set title 'Results on MyLucce Facedatabase'
set ylabel 'Accuracy (%)'
set xlabel 'k -Nearest Neighbors'
set logscale x
set xtics 1,5,100
set xtics add ("10" 10)
set xtics add ("100" 100)
set xrange [ 1 : 100 ] noreverse nowriteback
set yrange [ 0 : 100 ] noreverse nowriteback

set terminal pdf color
set output 'k4-lucce.pdf'

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
set key inside right top vertical Right noreverse noenhanced autotitle columnhead box
plot 'facerec_k4_Lucce.csv' using 1:2 smooth bezier, \
                        '' using 1:3 smooth bezier, \
                        '' using 1:4 smooth bezier

#plot 'facerec_k4_Lucce.csv' using 1:3, f2(x)

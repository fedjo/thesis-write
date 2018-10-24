set title "TLB shootdown overhead on threaded applications"

set xlabel "Scratchpad size (bytes)" font ",12"
set ylabel "mprotect latency (cycles)" font ",12"

set term pdf size 15, 9 
set output "tlb_{{ name }}.pdf"

set boxwidth 0.9 absolute
set style fill solid 1.00 border lt -1
set key inside right top vertical Right noreverse noenhanced autotitles nobox
set style histogram errorbars gap 2 lw 2
set datafile missing '-'
set style data histograms
set xtics border in scale 0,0 nomirror rotate by -45  offset character 0, 0, 0 autojustify
set xtics  norangelimit font ",8"
set ytics font ",8"
set xtics   ()
#set yrange [ 0 : 40000 ] noreverse nowriteback
set autoscale
set key left top
set bars fullwidth front
set xzeroaxis
j={{ num_cases }}

plot "plot_{{ name }}.dat" using 2:2+j:xtic(1) title columnheader(2), \
         for[i=3:j+1:1] "" using i:i+j title columnheader(i), \

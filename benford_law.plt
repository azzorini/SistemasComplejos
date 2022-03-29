# Para funcionar necesita el fichero benford.txt que genera el script benford_law.py
set terminal png
set output "benford_fit.png"

set xrange [0:10]
set xtics 1, 1, 9

set xlabel "Primera cifra"
set ylabel "Frecuencia"

unset key
set logscale y

f(x) = m*x + n

set fit quiet
fit f(x) "benford.txt" u (log($1)):(log($2)) via m, n

stats "benford.txt" u (log($1)):(log($2)) nooutput

plot exp(f(log(x))) lc "blue" lw 2, "benford.txt" u 1:2 w p lc "dark-red" ps 2 pt 7

# Mostramos todos los datos de interés
print "ln p(x) = m*ln(x) + n"
print sprintf("\tm = %.3f +/- %.3f", m, m_err)
print sprintf("\tn = %.2f +/- %.2f", n, n_err)
print sprintf("\tr = %.7f", STATS_correlation)

print "\np(x) = A*x^(-a)"
print sprintf("\tA = %.3f +/- %.3f", exp(n), exp(n)*n_err)
print sprintf("\ta = %.3f +/- %.3f", -m, m_err)

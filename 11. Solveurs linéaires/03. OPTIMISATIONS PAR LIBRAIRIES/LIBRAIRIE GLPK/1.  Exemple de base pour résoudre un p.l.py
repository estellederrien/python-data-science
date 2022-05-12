""" 
Résoudre un PL avec GLPK

https://pyglpk.readthedocs.io/en/latest/readme.html#building-and-installing

http://www.tfinley.net/software/pyglpk/discussion.html

maximize 	Z	= 	10 x0	+	6 x1	+	4 x2
subject to 	p	= 	x0	+	x1	+	x2
	q	= 	10x0	+	4x1	+	5x2
	r	= 	2x0	+	2x1	+	6x2
and bounds of variables	
−∞ < p ≤ 100 	  0 ≤ x0 < ∞
−∞ < q ≤ 600 	  0 ≤ x1 < ∞
−∞ < r ≤ 300 	  0 ≤ x2 < ∞ 

"""


import glpk            # Import the GLPK module

lp = glpk.LPX()        # Create empty problem instance
lp.name = 'sample'     # Assign symbolic name to problem
lp.obj.maximize = True # Set this as a maximization problem
lp.rows.add(3)         # Append three rows to this instance

for r in lp.rows:      # Iterate over all rows
	r.name = chr(ord('p')+r.index) # Name them p, q, and r

lp.rows[0].bounds = None, 100.0  # Set bound -inf < p <= 100
lp.rows[1].bounds = None, 600.0  # Set bound -inf < q <= 600
lp.rows[2].bounds = None, 300.0  # Set bound -inf < r <= 300

lp.cols.add(3)         # Append three columns to this instance

for c in lp.cols:      # Iterate over all columns
	c.name = 'x%d' % c.index # Name them x0, x1, and x2
	c.bounds = 0.0, None     # Set bound 0 <= xi < inf

lp.obj[:] = [ 10.0, 6.0, 4.0 ]   # Set objective coefficients
lp.matrix = [ 1.0, 1.0, 1.0,     # Set nonzero entries of the
             10.0, 4.0, 5.0,     #   constraint matrix.  (In this
              2.0, 2.0, 6.0 ]    #   case, all are non-zero.)

lp.simplex()           # Solve this LP with the simplex method

print ('Z = %g;' % lp.obj.value),  # Retrieve and print obj func value
print ('; '.join('%s = %g' % (c.name, c.primal) for c in lp.cols))

# Print struct variable names and primal values


""" This may produce this output.

Z = 733.333; x0 = 33.3333; x1 = 66.6667; x2 = 0 """

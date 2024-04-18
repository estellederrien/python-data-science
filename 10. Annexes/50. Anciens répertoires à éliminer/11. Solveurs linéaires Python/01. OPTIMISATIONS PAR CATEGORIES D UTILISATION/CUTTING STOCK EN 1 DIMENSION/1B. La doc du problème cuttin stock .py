#summary One-sentence summary of this page.
2	
3	=A Cutting Stock Problem=
4	
5	
6	==The Sponge Roll Production Problem==
7	--------------------------
8	===*Problem Description*===
9	-------------------
10	The Better Food Company produces cream-filled sponge rolls with a standard width of 20 cm each. Each 20cm roll costs the company $1.00 to produce. Special customer orders with different widths are produced by cutting (slitting) the standard rolls of sponge into shorter lengths. The fixed daily orders are summarized in the following table. These orders need to be met at least cost.
11	
12	||Order Desired || Width (cm) Desired || Number of Rolls ||
13	||A ||5 ||150 ||
14	||B ||7 ||200 ||
15	||C ||9 ||300 ||
16	
17	
18	
19	An order is filled by setting the cutting knives to the desired widths. Usually, there are a number of ways in which standard rolls can be slit to fill a given order. The figure below shows three possible knife settings for the 20-cm roll. Although there are other feasible settings, we limit the discussion for the moment to considering settings 1, 2 and 3 in the figure. Note that the shaded area in each diagram represents lengths of sponge that are too short to be used in meeting orders, and so these pieces must be thrown away. Such wastage is called trim loss.
20	
21	http://pulp-or.googlecode.com/svn/wiki/cutting_rolls.jpg
22	
23	
24	The Better Food Company wants to know how to cut the 20cm rolls to minimise the cost of meeting their customer orders.
25	
26	
27	===Formulation===
28	----------------------
29	The Sponge Roll Production Problem is an example of a Cutting Stock model. Cutting Stock models are a specialisation of Set Covering models. The generalised set covering model is:
30	 
31	http://pulp-or.googlecode.com/svn/wiki/1770704298-14px.png
32	
33	For cutting stock models, each column of the model represents a possible cutting pattern and each constraint represents a requirement for the patterns (in The Sponge Roll Production Problem the requirements are the customer orders). Much of the complexity in cutting stock models (and indeed set covering models in general) is removed during the generation of the columns. Each column represents a feasible pattern, but the complexity of producing feasible patterns is removed from the mathematical programme.
34	
35	When formulating we will consider two alternatives:
36	
37	    # The usual formulation (by row);
38	    # The [ColumnGeneration2 formulation].
39	
40	
41	 === _1. Identify the Decision Variables_===
42	 ---------------------
43	The decision variables are the number of times to use each sensible cutting pattern.
44	
45	
46	 === _2. Formulate the Objective Function_===
47	 --------------------
48	Each cutting pattern has an associated cost, in this case the cost of the 20cm roll used (i.e., $1.00). The objective function is the cost of the total number of 20cm rolls required to be cut.
49	
50	 
51	 === _3. Formulate the Constraints_===
52	 ----------------------
53	The constraints ensure that the desired number of smaller rolls are produced by cutting the 20cm rolls.
54	
55	
56	==*Solution*==
57	-------------------
58	The introductory commenting and import statement is entered.
59	
60	{{{
61	"""
62	The Sponge Roll Problem for the PuLP Modeller
63	Authors: Antony Phillips, Dr Stuart Mitchell   2007
64	"""
65	# Import PuLP modeller functions
66	from pulp import *
67	}}}
68	
69	A list of the roll lengths is entered and a dictionary linking the roll lengths to their demand.
70	
71	{{{
72	# A list of all the roll lengths is created
73	LenOpts = ["5","7","9"]
74	# A dictionary of the demand for each roll length is created
75	rollDemand = {"5": 150,
76	              "7": 200,
77	              "9": 300}
78	}}}
79	
80	A list of the pattern names we are analysing is entered, and then a list (set out to be viewed as a table) of the number of rolls each pattern can make, for each roll length.
81	
82	{{{
83	# A list of all the patterns is created
84	PatternNames = ["A","B","C"]
85	# Creates a list of the number of rolls in each pattern for each different roll length
86	patterns = [#A B C
87	            [0,2,2],# 5
88	            [1,1,0],# 7
89	            [1,0,1] # 9
90	            ]
91	}}}
92	
93	The cost of each 20cm roll to be cut up at $1 is entered.
94	
95	{{{
96	# The cost of each 20cm long sponge roll used
97	cost = 1
98	}}}
99	
100	The pattern table is made into a dictionary (as has been done in previous examples), so that 'Patterns["7"]["B"]' will return the number of rolls of length 7 when cutting according to pattern B.
101	
102	{{{
103	# The pattern data is made into a dictionary
104	patterns = makeDict([LenOpts,PatternNames],patterns,0)
105	}}}
106	
107	The problem variables are created and will be of the form `Patt_A, Patt_B, Patt_C,` due to the first two parameters. A negative number of rolls cut into the patterns cannot happen, so the lower bound is zero, and there is no upper bound. The number of 20cm rolls cut up into patterns must also be an integer.
108	
109	{{{
110	# The problem variables of the number of each pattern to make are created
111	vars = LpVariable.dicts("Patt",PatternNames,0,None,LpInteger)
112	}}}
113	
114	The variable `prob` is created.
115	
116	{{{
117	# The variable `prob` is created
118	prob = LpProblem("Cutting Stock Problem",LpMinimize)
119	}}}
120	
121	The objective function is added to prob. This is the number of each pattern used multiplied by the the cost of each 20cm roll cut up.
122	
123	{{{
124	# The objective function is entered - the total number of large rolls used * the fixed cost of each
125	prob += lpSum([vars[i]*cost for i in PatternNames]),"Production Cost"
126	}}}
127	
128	The constraints are added to `prob`. In this case, the only constraints are ensuring that the demand for each shorter roll length is met.
129	
130	{{{
131	# The demand minimum constraint is entered
132	for i in rollLengths:
133	    prob += lpSum([vars[j]*patterns[i][j] for j in PatternNames])>=rollDemand[i],"Ensuring enough %s cm rolls"%i
134	}}}
135	
136	After the constraints is the usual end to the Python formulation starting with the `prob.writeLP` line. The full working file is available here.
137	
138	
139	==Post-Optimal Analysis==
140	--------------------------------------------
141	One common extension for cutting stock problems is the sale of any extra products and/or the trim loss at discounted prices. For example, The Better Food Company can sell any excess sponge rolls for: 15c for 5cm rolls, 25c for 7cm rolls and 35c for 9cm rolls. They can also get rid of any trim loss for 4c per cm.
142	
143	To incorporate the selling of excess sponge rolls, the following is added/changed:
144	
145	Since each roll length now has both an associated demand and an associated surplus cost, we put these into a list in a dictionary and then use splitDict. These two sections of code replace the `rollDemand` dictionary from the simple formulation. The `surplusPrice` dictionary can now be used.
146	
147	{{{
148	 # A dictionary of the demand and surplus sale price of each roll length is created
149	rollData = {#Length Demand SalePrice
150	              "5":   [150,   0.25],
151	              "7":   [200,   0.33],
152	              "9":   [300,   0.40]}
153	# The rollData is made into separate dictionaries
154	(rollDemand,surplusPrice) = splitDict(rollData)
155	}}}
156	
157	A new set of problem variables need to be created, and so the `vars` dictionary in the problem above needs to be more specifically renamed `pattVars`. The new additional variable dictionary is `surplusVars`, linking the the keys of the roll lengths ("5","7" and "9") to the variables `Surp_5, Surp_7` and `Surp_9` which are the number of rolls of surplus of each length.
158	The objective function has another lpSum term which is subtracted from the original. This term represents the sum of the money made from selling the surplus of each roll length. Lastly, an additional term is put into the demand constraint equation, because each roll that is counted as surplus cannot be used to fill the roll demand. [Note: the slash `\` is just a line continuation operator and has only been included so the line image could fit onto the screen. Using PyDev or IDLE, this will not be needed since there is a horizontal scroll]
159	
160	{{{
161	# The problem variables of the number of surplus rolls for each length are created
162	surplusVars = LpVariable.dicts("Surp",rollLengths,0,None,LpInteger)
163	}}}
164	
165	{{{
166	# The objective function is entered - the total number of large rolls used * the fixed cost of each minus the surplus sales
167	prob += lpSum([pattVars[i]*cost for i in PatternNames]) - \
168	        lpSum([surplusVars[i]*surplusPrice[i] for i in LenOpts]),"Net Production Cost"
169	
170	# The demand minimum constraint is entered
171	for i in LenOpts:
172	    prob += lpSum([pattVars[j]*patterns[i][j] for j in PatternNames]) - surplusVars[i]\
173	    >= rollDemand[i],"Ensuring enough %s cm rolls"%i
174	}}}
175	
176	Running this successfully (before adding trim loss) will result in a objective function value of 287.5
177	
178	
179	The trim loss is incorporated into the model differently to the surplus since the trim sold in each pattern is exactly known before the model runs, and the value of trim sold is simply based on how rolls were cut into each pattern.
180	Firstly, the sale value for each centremetre of trim is entered and the number of centremetres of trim in each pattern is added to a dictionary. This could actually be calculated using loops, but we have explicitly entered it instead, for this simple model with only 3 pattern choices.
181	
182	
183	{{{
184	# A dictionary of the number of cms of trim in each pattern is created
185	trim = {"A": 4,
186	        "B": 2,
187	        "C": 1}
188	}}}
189	
190	{{{
191	# The sale value of each cm of trim
192	trimValue = 0.04
193	}}}
194	
195	Lastly, a trim term is put into the objective function after the surplus term. It represents the value of the trim sold and has the meaning: the number of each pattern created multiplied by the number of centremetres of trim caused by using that pattern multiplied by the value of each centremetre of trim.
196	
197	
198	{{{
199	# The objective function is entered - the total number of large rolls used * the fixed cost of each minus the surplus sales, and the trim sales
200	prob += lpSum([pattVars[i]*cost for i in PatternNames]) - lpSum([surplusVars[i]*surplusPrice[i] for i in LenOpts]) \
201	- lpSum([pattVars[i]*trim[i]*trimValue for i in PatternNames]),"Net Production Cost"
202	}}}
203	
204	This should give you an objective function value of $251.5
205	
206	The full working file with surplus and trim included is available here.
207	
208	
209	===_Validation_===
210	-------------------
211	We need to make sure the number of each pattern cut is integer. We should check to make sure we have met our demand correctly, i.e., ensure the patterns are correctly defined. We should make sure that the number of rolls cut in a pattern will fit into a 20cm roll, i.e., the pattern is valid.
212	
213	
214	==*Presentation of Solution and Analysis*==
215	-------------
216	Your management summary for The Sponge Roll Production should contain a brief problem description, some discussion on your method for generating cutting patterns and a description of the patterns used. It should then present a summary of the optimal use of the cutting patterns.
217	
218	
219	===_Implementation and Ongoing Monitoring_===
220	--------------------
221	To implement your solution you should ensure that the cutting patterns you are using can be set up of the cutting machines. You could also check for hidden set-up costs, i.e., costs incurred by switching from one cutting pattern to the next. Ongoing monitoring should take the form of consistent checking of the product line. Introducing new products means that you will need to regenerate your cutting patterns. As usual, monitoring the costs and demands for any beneficial opportunities should take place.
222	
223	
224	==*Extra for Experts*==
225	-----------------------
226	In the above problem we only analysed 3 different patterns for cutting the sponge rolls, whereas there are in fact many different cutting patterns that are worth considering, as you will remember from STATS 255. All the patterns should be considered and the rest for this case can be calculated simply by hand. However, supposing the sponge roll was longer, or many different lengths were required instead of just three, it would take too long to solve by hand. The calculation of these other patterns can be done in Python at the start of your code so you do not need to explicitly enter them.
227	
228	This is done by using 2 logical functions:
229	
230	The first is the function that calculates the patterns themselves using a series of for loops. This function will only work for length options lists of size 3. The code works quite simply:
231	`j` represents the number of length 5 rolls to be cut, `k` represents the number of length 7 rolls to be cut and `l` represents the number of length 9 rolls to be cut. The range of each of these loops is the logical range that `j,k` and `l` can take. That is, a minimum value of zero, and a maximum value of how many of that length could be cut if the full length of the roll was cut into pieces that size. e.g. for `j`, the maximum possible value is 4 which is computed with 'int(totalRollLength/lenOpts[1])'. The `int` function rounds the result of the inner calculation down to the nearest integer (i.e. it truncates off the decimal part). The `+1` ensures that the top value is reached when iterating through the for loop.
232	
233	Inside the for loops, the sum of the lengths for that combination is calculated. If this sum is less than or equal to the total roll length then the cutting pattern is possible. In STATS255, the patterns with trim of 5 or more would not have been used, however there is no harm in having such patterns at [0,0,0] whereby there is 20cm trim and no rolls. Therefore they are calculated along with the other patterns. Supposing the trimValue was greater than 0.05, and the cost of each roll was still 1.00, this would actually make the problem have a negative infinity cost, since the [0,0,0] pattern would make money.
234	
235	{{{
236	def calculatePatterns(totalRollLength,lenOpts):
237	    """
238	     The patterns are created using for loops     The inputs are:
239	     totalRollLength - the length of the roll
240	     lenOpts - a list of the sizes of cutting options
241	     It returns the list of patterns
242	     Authors: Antony Phillips, Dr Stuart Mitchell    2007
243	    """
244	    patterns =[]
245	    # All possible combinations of cutting patterns are trialed, and the feasible/sensible patterns are added to the list
246	    for j in range (0,int(totalRollLength/lenOpts[0])+1):
247	        for k in range (0, int(totalRollLength/lenOpts[1])+1):
248	            for l in range (0, int(totalRollLength/lenOpts[2])+1):
249	                lengthSum = j*lenOpts[0]+k*lenOpts[1]+l*lenOpts[2]
250	                if lengthSum <= totalRollLength:
251	                    patterns += [[j,k,l]]
252	    return patterns
253	}}}
254	
255	Since the patterns are now calculated, they need to be assigned names and a trim value automatically too. This is done using another function which calls the calculatePatterns function. Whilst both functions could have been combined into one (or we could have even used no functions), it is much simpler for the reader to interpret it this way.
256	
257	Apart from calling calculatePatterns, the makePatterns function does 3 key things:
258	- Creates a name list to correspond to each of the patterns (P0,P1...)
259	- Calculates the trim for each pattern and puts it in a dictionary, with the pattern name as the reference key
260	- Prints the name of the patterns next to the list of the number of rolls of each length in that pattern
261	
262	
263	{{{
264	def makePatterns(totalRollLength,lenOpts):
265	    """
266	     Makes the different cutting patterns for a cutting stock problem.     The inputs are:
267	     totalRollLength : the length of the roll
268	     lenOpts: a list of the sizes of cutting options as strings
269	     Authors: Antony Phillips, Dr Stuart Mitchell    2007
270	    """
271	    # calculatePatterns is called to create a list of the feasible cutting options in tlist
272	    patterns = calculatePatterns(totalRollLength,lenOpts)
273	    # The list PatternNames is created
274	    PatternNames = []
275	    for i in range(len(patterns)):
276	        PatternNames += ["P"+str(i)]
277	    # The amount of trim (unused material) for each pattern is calculated and added to the dictionary
278	    # trim, with the reference key of the pattern name.
279	    trim = {}
280	    for name,pattern in zip(PatternNames,patterns):
281	        ssum = 0
282	        for rep,l in zip(pattern,lenOpts):
283	            ssum += rep*l
284	        trim[name] = totalRollLength - ssum
285	    # The different cutting lengths are printed, and the number of each roll of that length in each
286	    # pattern is printed below. This is so the user can see what each pattern contains.
287	    print "Lens: %s" %lenOpts
288	    for name,pattern in zip(PatternNames,patterns):
289	        print name + "  = %s"%pattern
290	    return (PatternNames,patterns,trim)
291	}}}
292	
293	The final changes must be made to the main code to use these functions. PatternNames, patterns and trim no longer need to be created explicitly in the main function and instead this line is put in:
294	
295	{{{
296	(PatternNames,patterns,trim) = makePatterns(totalRollLength,[int(l) for l in LenOpts])
297	}}}
298	
299	The second argument is the length options list, but it is altered so that all the values are integers instead of strings.
300	
301	The last alteration that must be made is the argument order in the makeDict function. This is because when our patterns list is created using a function, it is actually transposed from the way we entered it explicitly in the first example. The makeDict line should be:
302	
303	{{{
304	patterns = makeDict([PatternNames,LenOpts],patterns,0)
305	}}}
306	
307	Since the code above has been written using functions, any function can be altered to be more efficient or versatile. In the above formulation, the only factor limiting LenOpts lists to length 3 is the calculatePatterns function. This function can be made recursive so it can calculate the pattern list for an input LenOpts of any size. An example of how this can be done is shown below: (when this is called, pass an empty list '[]' as the starting head variable)
308	
309	The full working code using this recursive function is available here. The objective function value is now $246.5
310	
311	{{{
312	def calculatePatterns(totalRollLength, lenOpts, head):
313	    """
314	     Recursively calculates the list of options lists for a cutting stock problem.
315	     
316	     The inputs are:
317	     totalRollLength - the length of the roll
318	     lenOpts - a list of the sizes of remaining cutting options
319	     head - the current list that has been passed down though the recusion
320	     Returns the list of patterns
321	     
322	     Authors: Bojan Blazevic, Dr Stuart Mitchell    2007
323	    """
324	    if lenOpts:
325	        patterns =[]
326	        #take the first option off lenOpts
327	        opt = lenOpts[0]
328	        for rep in range(int(totalRollLength/opt)+1):
329	            #reduce the length
330	            l = totalRollLength - rep*opt
331	            h = head[:]
332	            h.append(rep)           
333	            patterns.extend(calculatePatterns(l, lenOpts[1:], h))
334	    else:
335	        #end of the recursion
336	        patterns = [head]
337	    return patterns
338	}}}
339	
340	Lastly, for people who prefer using an Object-Oriented approach, it is possible to define a Pattern class. This object-oriented method is used later in the Column Generation sections, and it is a good idea to understand how it works. This code can be found [http://pulp-or.googlecode.com/svn/trunk/pulp-or/examples/CGcolumnwise.py here].
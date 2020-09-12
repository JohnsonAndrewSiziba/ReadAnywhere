import os

#directory = os.fsencode("./automata_theory")
directory = "./discrete_mathematics"
output_directory = "./output"

def addModal(data):
	if("</body>" in data):
		out = ""
		counter = 0
		static_string = """ <div class="container">
		   <!-- Modal -->
		   <div class="modal fade" id="myModal" role="dialog">
			  <div class="modal-dialog">
				 <!-- Modal content-->
				 <div class="modal-content">
				    <div class="modal-header">
				       <button type="button" class="close" data-dismiss="modal">&times;</button>
				       <h4 class="modal-title">Chapters</h4>
				    </div>
				    <div class="modal-body">
				       <ul class="toc chapters">
						<li class="heading">Discrete Mathematics Tutorial</li>
						<li><a href="index.htm">Discrete Mathematics - Home</a></li>
						<li><a href="discrete_mathematics_introduction.htm">Discrete Mathematics - Introduction</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Sets, Relations, &amp; Functions</li>
						<li><a href="discrete_mathematics_sets.htm">Discrete Mathematics - Sets</a></li>
						<li><a href="discrete_mathematics_relations.htm">Discrete Mathematics - Relations</a></li>
						<li><a href="discrete_mathematics_functions.htm">Discrete Mathematics - Functions</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Mathematical Logic</li>
						<li><a href="discrete_mathematics_propositional_logic.htm">Propositional Logic</a></li>
						<li><a href="discrete_mathematics_predicate_logic.htm">Predicate Logic</a></li>
						<li><a href="rules_of_inference.htm">Rules of Inference</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Group Theory</li>
						<li><a href="operators_and_postulates.htm">Operators &amp; Postulates</a></li>
						<li><a href="discrete_mathematics_group_theory.htm">Group Theory</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Counting &amp; Probability</li>
						<li><a href="discrete_mathematics_counting_theory.htm">Counting Theory</a></li>
						<li><a href="discrete_mathematics_probability.htm">Probability</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Mathematical &amp; Recurrence</li>
						<li><a href="discrete_mathematical_induction.htm">Mathematical Induction</a></li>
						<li><a href="discrete_mathematics_recurrence_relation.htm">Recurrence Relation</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Discrete Structures</li>
						<li><a href="graph_and_graph_models.htm">Graph &amp; Graph Models</a></li>
						<li><a href="more_on_graphs.htm">More on Graphs</a></li>
						<li><a href="introduction_to_trees.htm">Introduction to Trees</a></li>
						<li><a href="discrete_mathematics_spanning_trees.htm">Spanning Trees</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Boolean Algebra</li>
						<li><a href="boolean_expressions_functions.htm">Boolean Expressions &amp; Functions</a></li>
						<li><a href="simplification_of_boolean_functions.htm">Simplification of Boolean Functions</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Discrete Mathematics Resources</li>
						<li><a href="discrete_mathematics_quick_guide.htm">Discrete Mathematics - Quick Guide</a></li>
						</ul>
				    </div>
				    <div class="modal-footer">
				       <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
				    </div>
				 </div>

			  </div>
		   </div>

		</div> """

		data = data.split("</body>")
		for s in data:
			if(counter == 0):
				s += static_string + "\n</body>"
			out += s
			counter += 1
		return out
	else:
		return data
	
def modifyCss(data):
	counter = 0
	out = ""
	data = data.split("#")
	for s in data:
		s = s.strip()
		if(s == "016884;"):
			out += "#022A51;"
		else:
			if(counter == 0):
				out += s
			else:
				out += "#" + s
		counter += 1
	return out
	
def staticFiles(data):
	if("</head>" in data):
		out = ""
		counter = 0
		bootstrap_css = '<link rel="stylesheet" href="../bootstrap.min.css">' + "\n"
		jquery = '<script src="../jquery.min.js"></script>' + "\n"
		bootstrap_js = '<script src="../bootstrap.min.js"></script>' + "\n"
		masterstyle = '<link rel="stylesheet" href="../style.css">' + "\n"
		masterscript = '<script src="../js/javascript.js"></script>' + "\n"
		static_string = bootstrap_css + jquery + bootstrap_js + masterstyle + masterscript + "\n</head>"

		data = data.split("</head>")
		for s in data:
			if(counter == 0):
				s += static_string
			out += s
			counter += 1
		return out
	else:
		return data
		
def tutorialsPoint(data):
	data = data.replace("tutorialspoint", "")
	data = data.replace("Tutorialspoint", "")
	data = data.replace("TutorialsPoint", "")
	data = data.replace("TUTORIALSPOINT", "")
	return data
   
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".htm") or filename.endswith(".html"): 
		print(os.path.join(directory, filename))
		file_contents = "";
		with open(os.path.join(directory, filename), "r", encoding="utf8", errors='ignore') as a_file:
			for line in a_file:
				stripped_line = line.strip()
				line = modifyCss(stripped_line)
				line = staticFiles(line)
				line = addModal(line)
				line = tutorialsPoint(line)
				file_contents += line + "\n"
				
		file = open(os.path.join(output_directory, filename), "w", encoding="utf8", errors='ignore') 
		file.write(file_contents) 
		file.close() 
		continue
	else:
		continue
	
	
	

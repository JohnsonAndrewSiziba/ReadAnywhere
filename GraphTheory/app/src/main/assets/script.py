import os

#directory = os.fsencode("./automata_theory")
directory = "./graph_theory"
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
				       <ul class="toc chapters" >
						<li class="heading">Graph Theory Tutorial</li>
						<li><a href="index.htm">Graph Theory - Home</a></li>
						<li><a href="graph_theory_introduction.htm">Graph Theory - Introduction</a></li>
						<li><a href="graph_theory_fundamentals.htm">Graph Theory - Fundamentals</a></li>
						<li><a href="graph_theory_basic_properties.htm">Graph Theory - Basic Properties</a></li>
						<li><a href="graph_theory_types_of_graphs.htm">Graph Theory - Types of Graphs</a></li>
						<li><a href="graph_theory_trees.htm">Graph Theory - Trees</a></li>
						<li><a href="graph_theory_connectivity.htm">Graph Theory - Connectivity</a></li>
						<li><a href="graph_theory_coverings.htm">Graph Theory - Coverings</a></li>
						<li><a href="graph_theory_matchings.htm">Graph Theory - Matchings</a></li>
						<li><a href="graph_theory_independent_sets.htm">Graph Theory - Independent Sets</a></li>
						<li><a href="graph_theory_coloring.htm">Graph Theory - Coloring</a></li>
						<li><a href="graph_theory_isomorphism.htm">Graph Theory - Isomorphism</a></li>
						<li><a href="graph_theory_traversability.htm">Graph Theory - Traversability</a></li>
						<li><a href="graph_theory_examples.htm">Graph Theory - Examples</a></li>
						<li class="heading">Graph Theory Useful Resources</li>
						<li><a href="graph_theory_quick_guide.htm">Graph Theory - Quick Guide</a></li>
						<li><a href="graph_theory_useful_resources.htm">Graph Theory - Useful Resources</a></li>
						<li><a href="graph_theory_discussion.htm">Graph Theory - Discussion</a></li>
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
		if(s == "c0b503;"):
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
	
	
	

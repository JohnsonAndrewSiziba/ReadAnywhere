import os

#directory = os.fsencode("./automata_theory")
directory = "./design_and_analysis_of_algorithms"
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
						<li class="heading">Basics of Algorithms</li>
						<li><a href="design_and_analysis_of_algorithms_introduction.htm">DAA - Introduction</a></li>
						<li><a href="analysis_of_algorithms.htm">DAA - Analysis of Algorithms</a></li>
						<li><a href="design_and_analysis_of_algorithms_methodology.htm">DAA - Methodology of Analysis</a></li>
						<li><a href="design_and_analysis_of_algorithms_asymptotic_notations_apriori.htm">Asymptotic Notations &amp; Apriori Analysis</a></li>
						<li><a href="design_and_analysis_of_algorithms_space_complexities.htm">DAA - Space Complexities</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Design Strategies</li>
						<li><a href="design_and_analysis_of_algorithms_divide_conquer.htm">DAA - Divide &amp; Conquer</a></li>
						<li><a href="design_and_analysis_of_algorithms_max_min_problem.htm">DAA - Max-Min Problem</a></li>
						<li><a href="design_and_analysis_of_algorithms_merge_sort.htm">DAA - Merge Sort</a></li>
						<li><a href="design_and_analysis_of_algorithms_binary_search.htm">DAA - Binary Search</a></li>
						<li><a href="design_and_analysis_of_algorithms_strassens_matrix_multiplication.htm">Strassen’s Matrix Multiplication</a></li>
						<li><a href="design_and_analysis_of_algorithms_greedy_method.htm">DAA - Greedy Method</a></li>
						<li><a href="design_and_analysis_of_algorithms_fractional_knapsack.htm">DAA - Fractional Knapsack</a></li>
						<li><a href="design_and_analysis_of_algorithms_job_sequencing_with_deadline.htm">DAA - Job Sequencing with Deadline</a></li>
						<li><a href="design_and_analysis_of_algorithms_optimal_merge_pattern.htm">DAA - Optimal Merge Pattern</a></li>
						<li><a href="design_and_analysis_of_algorithms_dynamic_programming.htm">DAA - Dynamic Programming</a></li>
						<li><a href="design_and_analysis_of_algorithms_01_knapsack.htm">DAA - 0-1 Knapsack</a></li>
						<li><a href="design_and_analysis_of_algorithms_longest_common_subsequence.htm">Longest Common Subsequence</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Graph Theory</li>
						<li><a href="design_and_analysis_of_algorithms_spanning_tree.htm">DAA - Spanning Tree</a></li>
						<li><a href="design_and_analysis_of_algorithms_shortest_paths.htm">DAA - Shortest Paths</a></li>
						<li><a href="design_and_analysis_of_algorithms_multistage_graph.htm">DAA - Multistage Graph</a></li>
						<li><a href="design_and_analysis_of_algorithms_travelling_salesman_problem.htm">Travelling Salesman Problem</a></li>
						<li><a href="design_and_analysis_of_algorithms_optimal_cost_binary_search_trees.htm">Optimal Cost Binary Search Trees</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Heap Algorithms</li>
						<li><a href="design_and_analysis_of_algorithms_binary_heap.htm">DAA - Binary Heap</a></li>
						<li><a href="design_and_analysis_of_algorithms_insert_method.htm">DAA - Insert Method</a></li>
						<li><a href="design_and_analysis_of_algorithms_heapify_method.htm">DAA - Heapify Method</a></li>
						<li><a href="design_and_analysis_of_algorithms_extract_method.htm">DAA - Extract Method</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Sorting Methods</li>
						<li><a href="design_and_analysis_of_algorithms_bubble_sort.htm">DAA - Bubble Sort</a></li>
						<li><a href="design_and_analysis_of_algorithms_insertion_sort.htm">DAA - Insertion Sort</a></li>
						<li><a href="design_and_analysis_of_algorithms_selection_sort.htm">DAA - Selection Sort</a></li>
						<li><a href="design_and_analysis_of_algorithms_quick_sort.htm">DAA - Quick Sort</a></li>
						<li><a href="design_and_analysis_of_algorithms_radix_sort.htm">DAA - Radix Sort</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Complexity Theory</li>
						<li><a href="design_and_analysis_of_algorithms_deterministic_vs_nondeterministic_computations.htm">Deterministic vs. Nondeterministic Computations</a></li>
						<li><a href="design_and_analysis_of_algorithms_max_cliques.htm">DAA - Max Cliques</a></li>
						<li><a href="design_and_analysis_of_algorithms_vertex_cover.htm">DAA - Vertex Cover</a></li>
						<li><a href="design_and_analysis_of_algorithms_p_np_class.htm">DAA - P and NP Class</a></li>
						<li><a href="design_and_analysis_of_algorithms_cooks_theorem.htm">DAA - Cook’s Theorem</a></li>
						<li><a href="design_and_analysis_of_algorithms_np_hard_complete_classes.htm">NP Hard &amp; NP-Complete Classes</a></li>
						<li><a href="design_and_analysis_of_algorithms_hill_climbing.htm">DAA - Hill Climbing Algorithm</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">DAA Useful Resources</li>
						<li><a href="design_and_analysis_of_algorithms_quick_guide.htm">DAA - Quick Guide</a></li>
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
		if(s == "711e1e;"):
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
	
	
	

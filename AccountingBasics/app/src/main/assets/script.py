import os

#directory = os.fsencode("./automata_theory")
directory = "./accounting_basics"
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
						<li class="heading">Accounting Basics Tutorial</li>
						<li><a href="index.htm">Accounting - Home</a></li>
						<li><a href="accounting_basics_overview.htm">Accounting - Overview</a></li>
						<li><a href="accounting_process.htm">Accounting - Process</a></li>
						<li><a href="accounting_basic_concepts.htm">Accounting - Basic Concepts</a></li>   
						<li><a href="accounting_conventions.htm">Accounting - Conventions</a></li> 
						<li><a href="accounting_classification_of_accounts.htm">Accounting - Accounts' Classification</a></li> 
						<li><a href="accounting_systems.htm">Accounting - Systems</a></li> 
						</ul>
						<ul class="toc chapters">
						<li class="heading">Financial Accounting</li>
						<li><a href="financial_accounting_journal.htm">Financial Accounting - Journal</a></li>
						<li><a href="financial_accounting_ledger.htm">Financial Accounting - Ledger</a></li>
						<li><a href="financial_accounting_subsidiary_books.htm">Financial Accounting - Books</a></li>
						<li><a href="financial_accounting_depreciation.htm">Financial Accounting - Depreciation</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Cost Accounting</li>   
						<li><a href="cost_accounting_introduction.htm">Cost Accounting - Introduction</a></li>
						<li><a href="cost_accounting_advantages.htm">Cost Accounting - Advantages</a></li>
						<li><a href="cost_accounting_vs_financial_accounting.htm">Cost Accounting - vs. Financial A/c</a></li>
						<li><a href="cost_accounting_classification_of_cost.htm">Cost Accounting - Cost Classification</a></li>
						<li><a href="cost_accounting_elements_of_cost.htm">Cost Accounting - Elements of Cost</a></li>
						<li><a href="cost_accounting_cost_sheet.htm">Cost Accounting - Cost Sheet</a></li>
						<li><a href="cost_accounting_cost_control.htm">Cost Accounting - Cost Control</a></li>
						<li><a href="cost_accounting_cost_reduction.htm">Cost Accounting - Cost Reduction</a></li>
						<li><a href="cost_accounting_budgeting_analysis.htm">Cost Accounting - Budgeting</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Cost Accounting Techniques</li> 
						<li><a href="cost_accounting_marginal_costing.htm">Cost Accounting - Marginal Costing</a></li>
						<li><a href="cost_accounting_standard_costing.htm">Cost Accounting - Standard Costing</a></li>
						<li><a href="cost_accounting_variance_analysis.htm">Cost Accounting - Variance Analysis</a></li>
						<li><a href="cost_accounting_cvp_analysis.htm">Cost Accounting - CVP Analysis</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Management Accounting</li>   
						<li><a href="management_accounting_introduction.htm">Management A/c - Introduction</a></li>
						<li><a href="management_versus_cost_accounting.htm">Management A/c - vs. Cost A/c</a></li>
						<li><a href="management_versus_financial_accounting.htm">Management A/c - vs. Financial A/c</a></li>
						<li><a href="management_accounting_cash_flow.htm">Management A/c - Cash Flow</a></li>
						<li><a href="management_accounting_ratio_analysis.htm">Management A/c - Ratio Analysis</a></li>
						<li><a href="management_accounting_useful_ratios.htm">Management A/c - Useful Ratios</a></li>
						<li><a href="management_accounting_working_capital.htm">Management A/c - Working Capital</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Accounting Useful Resources</li>
						<li><a href="accounting_basics_quick_guide.htm">Accounting Basics - Quick Guide</a></li>
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
		if(s == "42c2ca;"):
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
	
	
	

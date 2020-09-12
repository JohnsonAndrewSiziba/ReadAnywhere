import os

#directory = os.fsencode("./automata_theory")
directory = "./bank_management"
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
						<li class="heading">Bank Management Tutorial</li>
						<li><a href="index.htm">Bank Management – Home</a></li>
						<li><a href="bank_management_introduction.htm">Bank Management - Introduction</a></li>
						<li><a href="bank_management_commercial_banking.htm">Bank Mngmt - Commercial Banking</a></li>
						<li><a href="bank_management_commercial_banking_functions.htm">Commercial Banking Functions</a></li>
						<li><a href="bank_management_commercial_banking_reforms.htm">Commercial Banking Reforms</a></li>
						<li><a href="bank_management_liquidity.htm">Bank Management – Liquidity</a></li>
						<li><a href="bank_management_liquidity_theory.htm">Liquidity Management Theory</a></li>
						<li><a href="bank_management_liabilities_theory.htm">Liabilities Management Theory</a></li>
						<li><a href="bank_management_basle_norms.htm">Bank Management – Basle Norms</a></li>
						<li><a href="bank_management_credit.htm">Bank Mngmt – Credit Management</a></li>
						<li><a href="bank_management_formulating_loan_policy.htm">Formulating Loan Policy</a></li>
						<li><a href="bank_management_asset_liability.htm">Bank Mngmt – Asset Liability Mngmt</a></li>
						<li><a href="bank_management_evolution_of_alm.htm">Bank Mngmt – Evolution Of ALM</a></li>
						<li><a href="bank_management_risks_with_assets.htm">Bank Mngmt – Risks With Assets</a></li>
						<li><a href="bank_management_risks_measurement_techniques.htm">Risk Measurement Techniques</a></li>
						<li><a href="bank_management_marketing.htm">Bank Management – Bank Marketing</a></li>
						<li><a href="bank_management_relationship.htm">Bank Mngmt – Relationship Banking</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Bank Management Resources</li>
						<li><a href="bank_management_quick_guide.htm">Bank Management - Quick Guide</a></li>
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
		if(s == "1d6094;"):
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
	
	
	

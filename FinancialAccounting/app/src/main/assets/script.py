import os

#directory = os.fsencode("./automata_theory")
directory = "./financial_accounting"
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
						<li class="heading">Financial Accounting Tutorial</li>
						<li><a href="index.htm">Financial Accounting - Home</a></li>
						<li><a href="financial_accounting_rectification_of_errors.htm">Rectification of Errors</a></li>
						<li><a href="financial_accounting_capital_and_revenue.htm">Capital and Revenue</a></li>
						<li><a href="financial_final_accounts.htm">Final Accounts</a></li>
						<li><a href="financial_accounting_provision_and_reserves.htm">Provision and Reserves</a></li>
						<li><a href="financial_accounting_measurement_of_business_income.htm">Measurement of Business Income</a></li>
						<li><a href="financial_accounting_bills_of_exchange_and_promissory_notes.htm">Bills of Exchange &amp; Promissory Notes</a></li>
						<li><a href="financial_accounting_inventory_valuation.htm">Inventory Valuation</a></li>
						<li><a href="financial_accounting_analysis_of_changes_in_income.htm">Analysis of Changes in Income</a></li>
						<li><a href="financial_accounting_consignment.htm">Accounting for Consignment</a></li>
						<li><a href="financial_accounting_joint_venture.htm">Joint Venture</a></li>
						<li><a href="financial_nontrading_accounts.htm">Non-Trading Accounts</a></li>
						<li><a href="financial_accounting_single_entry.htm">Single Entry</a></li>
						<li><a href="financial_accounting_leasing.htm">Leasing</a></li>
						<li><a href="financial_investment_account.htm">Investment Account</a></li>
						<li><a href="financial_insolvency_accounts.htm">Insolvency Accounts</a></li>
						<li><a href="financial_accounting_stock_exchange_transactions.htm">Stock Exchange Transactions</a></li>
						<li><a href="financial_accounts_of_private_individuals.htm">Accounts of Private Individuals</a></li>
						<li><a href="financial_accounting_cooperative_societies.htm">Co-Operative Societies</a></li>
						<li><a href="financial_accounting_insurance_claims.htm">Insurance Claims</a></li>
						<li><a href="financial_government_accounting.htm">Government Accounting</a></li>
						<li><a href="financial_contract_account.htm">Contract Account</a></li>
						<li><a href="financial_departmental_accounting.htm">Departmental Accounting</a></li>
						<li><a href="financial_voyage_accounting.htm">Voyage Accounting</a></li>
						<li><a href="financial_royalty_accounts.htm">Royalty Accounts</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Financial Accounting Resources</li>
						<li><a href="financial_accounting_quick_guide.htm">Financial Accounting - Quick Guide</a></li>
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
		if(s == "446a74;"):
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
	
	
	

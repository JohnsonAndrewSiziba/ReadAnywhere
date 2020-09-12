import os

#directory = os.fsencode("./automata_theory")
directory = "./strategic_management"
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
						<li class="heading">Strategic Management Tutorial</li>
						<li><a href="index.htm">Strategic Management - Home</a></li>
						<li><a href="strategic_management_introduction.htm">Strategic Management - Introduction</a></li>
						<li><a href="strategic_management_types.htm">Strategic Management - Types</a></li>
						<li><a href="strategic_management_process.htm">Strategic Management - Process</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Strategic Leadership</li>
						<li><a href="strategic_management_organization_specifics.htm">Organization Specifics</a></li>
						<li><a href="strategic_management_performance_issue.htm">Performance Issue</a></li>
						<li><a href="strategic_management_top_leadership.htm">The Top Leadership</a></li>
						<li><a href="strategic_management_entrepreneurial_orientation.htm">Entrepreneurial Orientation</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">The External Environment</li>
						<li><a href="strategic_management_organization_environment.htm">Organization &amp; Environment</a></li>
						<li><a href="analyzing_external_environment.htm">Analyzing the External Environment</a></li>
						<li><a href="strategic_management_judging_industry.htm">Judging the Industry</a></li>
						<li><a href="mapping_strategic_groups.htm">Mapping Strategic Groups</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Organizational Resources</li>
						<li><a href="resource_based_theory.htm">The Resource Based Theory</a></li>
						<li><a href="strategic_management_intellectual_property.htm">Intellectual Property</a></li>
						<li><a href="strategic_management_value_chain.htm">The Value Chain</a></li>
						<li><a href="other_performance_measures.htm">Other Performance Measures</a></li>
						<li><a href="company_assets_swot_analysis.htm">Company Assets: SWOT Analysis</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Business Level Strategies</li>
						<li><a href="strategic_management_different_types.htm">Different Types</a></li>
						<li><a href="strategic_management_cost_leadership.htm">Cost Leadership</a></li>
						<li><a href="strategic_management_niche_differentiation.htm">Niche Differentiation</a></li>
						<li><a href="focus_strategies.htm">Focus Strategies</a></li>
						<li><a href="best_cost_strategy.htm">The Best-Cost Strategy</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Aiding Business Level Strategies</li>
						<li><a href="strategic_management_competitive_moves.htm">Competitive Moves</a></li>
						<li><a href="strategic_management_competitors_moves.htm">Competitor's Moves</a></li>
						<li><a href="strategic_management_cooperative_moves.htm">Cooperative Moves</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">International Marketing Strategies</li>
						<li><a href="strategic_management_pros_cons.htm">Pros &amp; Cons</a></li>
						<li><a href="success_and_failure_drivers.htm">Drivers of Success and Failure</a></li>
						<li><a href="international_strategies_types.htm">International Strategies - Types</a></li>
						<li><a href="international_markets_competition.htm">International Markets - Competition</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Cooperative Level Strategies</li>
						<li><a href="concentration_strategies.htm">Concentration Strategies</a></li>
						<li><a href="vertical_integration_strategies.htm">Vertical Integration Strategies</a></li>
						<li><a href="diversification_strategies.htm">Diversification Strategies</a></li>
						<li><a href="downsizing_strategies.htm">Downsizing Strategies</a></li>
						<li><a href="strategic_management_portfolio_planning.htm">Portfolio Planning</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Strategy and Organizational Design</li>
						<li><a href="strategic_management_organizational_structure.htm">Organizational Structure</a></li>
						<li><a href="creating_organizational_structure.htm">Creating an Organizational Structure</a></li>
						<li><a href="organizational_control_systems.htm">Organizational Control Systems</a></li>
						<li><a href="legal_forms_of_business.htm">Legal Forms of Business</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Strategic HR Management</li>
						<li><a href="growth_and_nature.htm">Growth &amp; Nature</a></li>
						<li><a href="organizational_and_hrm_strategy.htm">Organizational &amp; HRM Strategy</a></li>
						<li><a href="hrm_impact_performance.htm">Impact of HRM on Performance</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Strategic Management Resources</li>
						<li><a href="strategic_management_quick_guide.htm">Strategic Management - Quick Guide</a></li>
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
		if(s == "ed8203;"):
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
	
	
	

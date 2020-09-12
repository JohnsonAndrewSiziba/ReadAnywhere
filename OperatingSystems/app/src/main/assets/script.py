import os

#directory = os.fsencode("./automata_theory")
directory = "./operating_system"
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
						<li class="heading">Operating System Tutorial</li>
						<li><a href="index.htm">OS - Home</a></li>
						<li><a href="os_overview.htm">OS - Overview</a></li>
						<li><a href="os_types.htm">OS - Types</a></li>
						<li><a href="os_services.htm">OS - Services</a></li>
						<li><a href="os_properties.htm">OS - Properties</a></li>
						<li><a href="os_processes.htm">OS - Processes</a></li>
						<li><a href="os_process_scheduling.htm">OS - Process Scheduling</a></li>
						<li><a href="os_process_scheduling_algorithms.htm">OS - Scheduling algorithms</a></li> 
						<li><a href="os_multi_threading.htm">OS -  Multi-threading</a></li>
						<li><a href="os_memory_management.htm">OS - Memory Management</a></li>
						<li><a href="os_virtual_memory.htm">OS -  Virtual Memory</a></li>
						<li><a href="os_io_hardware.htm">OS -  I/O Hardware</a></li>
						<li><a href="os_io_software.htm">OS - I/O Software</a></li>
						<li><a href="os_file_system.htm">OS -  File System</a></li>
						<li><a href="os_security.htm">OS - Security</a></li>
						<li><a href="os_linux.htm">OS - Linux</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">OS - Exams Questions with Answers</li>
						<li><a class="left" href="os_exams_questions_answers.htm">OS - Exams Questions with Answers</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Operating System Useful Resources</li>
						<li><a class="left" href="os_quick_guide.htm">OS - Quick Guide</a></li>
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
		if(s == "3896c2;"):
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
	
	
	

import os

#directory = os.fsencode("./automata_theory")
directory = "./data_communication_computer_network"
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
						<li class="heading">DCN Tutorial</li>
						<li><a target="_top" href="index.htm">Data Comm &amp; Networks Home</a></li>
						<li><a target="_top" href="data_communication_computer_network_overview.htm">DCN -  Overview</a></li>
						<li><a target="_top" href="computer_network_types.htm">DCN - Computer Network Types</a></li>
						<li><a target="_top" href="network_lan_technologies.htm">DCN - Network LAN Technologies</a></li>
						<li><a target="_top" href="computer_network_topologies.htm">DCN - Computer Network Topologies</a></li>
						<li><a target="_top" href="computer_network_models.htm">DCN - Computer Network Models</a></li>
						<li><a target="_top" href="computer_network_security.htm">DCN - Computer Network Security</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Physical Layer</li>
						<li><a target="_top" href="physical_layer_introduction.htm">DCN - Physical Layer Introduction</a></li>
						<li><a target="_top" href="digital_transmission.htm">DCN - Digital Transmission</a></li>
						<li><a target="_top" href="analog_transmission.htm">DCN - Analog Transmission</a></li>
						<li><a target="_top" href="transmission_media.htm">DCN - Transmission media</a></li>
						<li><a target="_top" href="wireless_transmission.htm">DCN - Wireless Transmission</a></li>
						<li><a target="_top" href="physical_layer_multiplexing.htm">DCN - Multiplexing</a></li>
						<li><a target="_top" href="physical_layer_switching.htm">DCN - Network Switching</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Data Link Layer</li>
						<li><a target="_top" href="data_link_layer_introduction.htm">DCN - Data Link Layer Introduction</a></li>
						<li><a target="_top" href="error_detection_and_correction.htm">DCN - Error detection and Correction</a></li>
						<li><a target="_top" href="data_link_control_and_protocols.htm">DCN - Data Link Control &amp; Protocols</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Network Layer</li>
						<li><a target="_top" href="network_layer_introduction.htm">DCN - Network Layer Introduction</a></li>
						<li><a target="_top" href="network_addressing.htm">DCN - Network Addressing</a></li>
						<li><a target="_top" href="network_layer_routing.htm">DCN - Routing</a></li>
						<li><a target="_top" href="internetworking.htm">DCN - Internetworking</a></li>
						<li><a target="_top" href="network_layer_protocols.htm">DCN - Network Layer Protocols</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Transport Layer</li>
						<li><a target="_top" href="transport_layer_introduction.htm">DCN - Transport Layer Introduction</a></li>
						<li><a target="_top" href="transmission_control_protocol.htm">DCN - Transmission Control Protocol</a></li>
						<li><a target="_top" href="user_datagram_protocol.htm">DCN - User Datagram Protocol</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Application Layer</li>
						<li><a target="_top" href="application_layer_introduction.htm">DCN - Application Layer Introduction</a></li>
						<li><a target="_top" href="client_server_model.htm">DCN - Client-Server Model</a></li>
						<li><a target="_top" href="application_protocols.htm">DCN - Application Protocols</a></li>
						<li><a target="_top" href="network_services.htm">DCN - Network Services</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">DCN Useful Resources</li>
						<li><a target="_top" href="dcn_quick_guide.htm">DCN - Quick Guide</a></li>
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
		if(s == "2bb2b0;"):
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
	
	
	

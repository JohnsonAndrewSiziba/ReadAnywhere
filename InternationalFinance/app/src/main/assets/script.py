import os

#directory = os.fsencode("./automata_theory")
directory = "./international_finance"
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
						<li class="heading">International Finance Tutorial</li>
						<li><a href="index.htm">International Finance - Home</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading"><span style="font-size:0.93em;">International Finance &amp; Global Markets</span></li>
						<li><a href="international_finance_introduction.htm">International Finance - Introduction</a></li>
						<li><a href="international_financial_globalization.htm">Financial Globalization</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Foreign Exchange Markets</li>
						<li><a href="balance_of_payments.htm">Balance of Payments</a></li>
						<li><a href="forex_market_players.htm">Forex Market Players</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">International Capital Markets</li>
						<li><a href="interest_rate_parity_model.htm">The Interest Rate Parity Model</a></li>
						<li><a href="international_finance_monetary_assets.htm">Monetary Assets</a></li>
						<li><a href="international_finance_exchange_rates.htm">Exchange Rates</a></li>
						<li><a href="international_finance_interest_rates.htm">Interest Rates</a></li>
						<li><a href="international_finance_forex_intervention.htm">Forex Intervention</a></li>
						<li><a href="international_money_market.htm">International Money Market</a></li>
						<li><a href="international_bond_markets.htm">International Bond Markets</a></li>
						<li><a href="international_equity_markets.htm">International Equity Markets</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Hedging &amp; Risk Management</li>
						<li><a href="exchange_rate_forecasts.htm">Exchange Rate Forecasts</a></li>
						<li><a href="exchange_rate_fluctuations.htm">Exchange Rate Fluctuations</a></li>
						<li><a href="foreign_currency_futures_options.htm">Foreign Currency Futures &amp; Options</a></li>
						<li><a href="international_finance_transaction_exposure.htm">Transaction Exposure</a></li>
						<li><a href="international_finance_translation_exposure.htm">Translation Exposure</a></li>
						<li><a href="international_finance_economic_exposure.htm">Economic Exposure</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">Strategic Decision Making</li>
						<li><a href="foreign_direct_investment.htm">Foreign Direct Investment</a></li>
						<li><a href="long_and_short_term_financing.htm">Long-Term and Short-Term Financing</a></li>
						<li><a href="working_capital_management.htm">Working Capital Management</a></li>
						<li><a href="international_trade_finance.htm">International Trade Finance</a></li>
						</ul>
						<ul class="toc chapters">
						<li class="heading">International Finance Resources</li>
						<li><a href="international_finance_quick_guide.htm">International Finance - Quick Guide</a></li>
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
		if(s == "c82456;"):
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
	
	
	

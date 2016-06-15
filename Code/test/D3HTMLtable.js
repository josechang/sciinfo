d3.xml("/data/GoldenGate2012Results.xml", function(xml) {
	
  var runners = d3.select(xml).selectAll("runner")[0];
  var table = d3.select("#presentation").append("table").attr("class","grid");
	
  var thead = table.append("thead");
  thead.append("th").text("Gender");
  thead.append("th").text("City");
  thead.append("th").text("Time");
  thead.append("th").text("Pace");
	
  var tr = table.selectAll("tr")
    .data(runners)
   .enter().append("tr");
  
  // place 
  var td = tr.selectAll("td")
    .data(function(d) {
      return d3.select(d).attr("gender");
    })
   .enter().append("td")
    .text(function(d) {
      return d;
    });
  
  // city
  tr.selectAll("tr")
    .data(function(d) {
      return d3.select(d).select("city")[0]; 
    })
   .enter().append("td")
    .text(function(d) {
      return d.textContent;
    });
	    
  // time
  tr.selectAll("tr")
    .data(function(d) {
      return d3.select(d).select("time")[0]; 
    })
   .enter().append("td")
    .text(function(d) {
      return d.textContent;
    });
		
  // pace
  tr.selectAll("tr")
    .data(function(d) {
      return d3.select(d).select("pace")[0]; 
    })
   .enter().append("td")
    .text(function(d) {
      return d.textContent;
    });
});
var table = document.getElementById("statistics");
var max_score=0;
var num_row=table.rows.length;
var num_col=table.rows[0].cells.length;

function calculate(){
	if (checkweight() == -1)
		return;
	var lastcell_index=num_col-1;
	var count;
	var weightid;
	var weight;
	for (var r = 1; r < num_row; r++) {
		count=0;
        for (var c = 1; c < num_col-1; c++) {
			weightid="weight"+c;
			weight=document.getElementById(weightid).value;
               count+=parseInt(table.rows[r].cells[c].innerHTML)*weight;
        }
		table.rows[r].cells[lastcell_index].innerHTML=count;
    }
	to100();
}
function to100(){
	var c = num_col-1;
	var score;
	for (var r = 1; r < num_row; r++) {
		score = parseFloat(table.rows[r].cells[c].innerHTML);
        if (score > max_score){
			max_score = score;
		}
    }
	for (var r = 1; r < num_row; r++) {
		table.rows[r].cells[c].innerHTML=(table.rows[r].cells[c].innerHTML/max_score*100).toFixed(2);
    }
}
function checkweight(){
	var totalweight=0;
	var weightid;
	var weight;
	for (var c=1;c < num_col-1;c++){
		weightid="weight"+c;
		weight=parseFloat(document.getElementById(weightid).value);
		totalweight+=weight;
	}
	if (totalweight != 1){
		alert("Notice!! The sum of weight is not 1.")
		return -1;
	}
}

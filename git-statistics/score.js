var tableTotal = document.getElementById("total");
var num_row_total=tableTotal.rows.length;
var num_col_total=tableTotal.rows[0].cells.length;

function calculate(){
	for (var r =1; r < num_row_total ; r++){
		a=parseInt(tableTotal.rows[r].cells[num_col_total-1].innerHTML);
		b=parseInt(tableTotal.rows[r].cells[num_col_total-2].children[0].value);
		tableTotal.rows[r].cells[num_col_total-1].innerHTML=Math.round(a+0.2*b);
	}
}

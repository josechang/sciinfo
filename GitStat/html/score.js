function isNumberKey(evt){
    var charCode = (evt.which) ? evt.which : event.keyCode
    if (charCode > 31 && (charCode != 46 &&(charCode < 48 || charCode > 57)))
        return false;
    return true;
}

function calculate(){	
	var score = document.getElementById("score");
	var num_row = score.rows.length;
	var num_col = score.rows[0].cells.length;
	var weight = [0, 0.18, 0.06, 0.36, 0.1, 0.1, 0.2]
	var temp = 0;
	for (var r = 1; r < num_row; r++) {
		var sum = 0;
		for (var c = 1; c < num_col-2; c++) {
			temp = Number(score.rows[r].cells[c].innerHTML);
			sum += temp*weight[c];
		}
		temp = Number(score.rows[r].cells[num_col-2].children[0].value);
		sum += temp*weight[num_col-2];		
		score.rows[r].cells[num_col-1].innerHTML = Math.round(sum);
    }
}

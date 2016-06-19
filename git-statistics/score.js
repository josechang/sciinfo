var table = document.getElementById("statistics");
var max_score=0;
var num_row=table.rows.length;
var num_col=table.rows[0].cells.length;
var profData=new Array(num_col-1);
var tempData;
var t=[12,13,14,15]
function calculate(){
	getProfData();
	createMatrixforTemp();
	firstTransform();
	secondTransform();
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
               count+=tempData[r][c]*weight;
        }
		table.rows[r].cells[lastcell_index].innerHTML=Math.round(count);
    }
}
function getScore(){
	getProfData();
	createMatrixforTemp();
	firstTransform();
	secondTransform();
}
function secondTransform(){
	var max;
	for (var c=1; c< num_col-1; c++){
		max = getMaxOfCol(c);
		for (var r=1; r < num_row ;r++){
			tempData[r][c]=70+30*(tempData[r][c]/max);
		}
	}
}
function firstTransform(){
	for (var r = 1;r < num_row ;r++){
		for (var c = 1; c < num_col-1 ; c++){
			data=parseInt(table.rows[r].cells[c].innerHTML);
			if (data > 0){
				tempData[r][c]=Math.log10(data/profData[c]);
			}else{
				tempData[r][c]=-10;
			}
		}
	}
}
function createMatrixforTemp(){ // a num_row*num_col-1 matrix
	tempData=new Array(num_row); //create a useless col and row to access easily
	for (var c = 0;c < num_row;c++){
		tempData[c] = new Array(num_col-1);
	}
}
function getProfData(){
	for (var r=1;r < num_row; r++){
		if (table.rows[r].cells[0].innerHTML=="Torbjörn Nordling"){
			for (var c=1;c < num_col-1;c++){
				profData[c]=parseInt(table.rows[r].cells[c].innerHTML);
			}
			break;
		}
	}
}
function getMaxOfCol(index) {
	var max=0;
	for (var r = 1;r < num_row; r++){
		if (tempData[r][index] > max){
			max = tempData[r][index];
		}
	}
	return max;
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

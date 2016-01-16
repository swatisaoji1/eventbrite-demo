/**
 * Checks the number of checked checkboxes.
 * gives alert when > 3 check boxes are cheked and clears the last check
 * @param {Number} j: index of the checkbox
 */
function chkcontrol(j) {
	var total=0;
	for(var i=0; i < document.category_list.categories.length; i++){
		if(document.category_list.categories[i].checked){
			total =total +1;}
		if(total > 3){
			alert("Please Select only three") 
			document.category_list.categories[j].checked = false ;
			return false;
		}
	}
}


/**
 * Gets the total count of the selected checkboxes 
 * gives alert when < 3 check boxes are cheked
 */
function getcount(){
	var form = document.forms[0]; // your form element (whatever)
	var checkedElms = form.querySelectorAll(':checked').length;
	if(checkedElms< 3){
		alert('Please select three elements')
		return false;
		
	}else{
		form.submit();
		return true;
	}
	
}

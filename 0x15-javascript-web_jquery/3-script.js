// JavaScript script that adds the class red to the <header>
// element when the user clicks on the tag DIV#red_header
$(document).ready(function(){
	$("DIV#red_header").click(function() {
		$("header").addClass("red");
	});
});

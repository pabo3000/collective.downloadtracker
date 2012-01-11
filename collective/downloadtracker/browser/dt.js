jq(document).ready(function(){
	jq('.documentByLine td a').click(function() {
		var td = jq(this).parent()
		var name = td.prev().prev().text();
		var date = td.prev().text();
		var url = window.location.href.replace(/view/, "delete");
		// alert('Handler for .click() called.');
		jq.getJSON(
			url,
			{
				name: name,
				date: date
			},
			function(data) {
				// lösche Zeile aus dom im Erfolgsfall
				console.log(data);
				if (data==true) {
					location.reload();
				}
			}
		);
		return false;
	});
 });


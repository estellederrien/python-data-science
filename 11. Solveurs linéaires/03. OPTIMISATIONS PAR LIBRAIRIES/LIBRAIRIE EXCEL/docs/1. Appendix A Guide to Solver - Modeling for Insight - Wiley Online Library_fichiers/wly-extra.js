(function(App, w) {
	'use strict';
    var d = w.document,
        en = encodeURIComponent;
    
    var cookies = document.cookie.split(";");
    
	try {
		var payload = {
				cookies : cookies
		};
		
		App.onecount.custom_data("test.wly.cookie", JSON.stringify(payload), function(data) {
			console.log(data);
		});
		
	}catch(e) {
		console.log(e);
	}
	
})(GCN, window);
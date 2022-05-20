
GCN.onecount.IdentityResponse = function(response) {
	try {
		if(response.status && response.status == 300) {
			document.location = response.data;
        } else {
            console.log(response);
            if(response.msg)
                console.log(response.msg);
        }
	}catch(e) {
		console.log(e);
	}
};

isObject = function(a) {
    return (!!a) && (a.constructor === Object);
};

(function(App, w) {
	'use strict';
    var d = w.document,
        en = encodeURIComponent;
    
    var sync = "https://validate.onecount.net/onecount/api/3rdparty/identifyByDemo.php";
    // var sync = "https://kush.onecount.net/oc/onecount/api/3rdparty/identifyByDemo.php";
    
	App.onecount.identify = 
		function(demos, upsert) {
			
			var ocid_cookie = App.cookie.read("__ocid") || "";
            try {
                if (ocid_cookie !== "") {
                    console.log({status: 200, data: "User already logged in!"});
                    return;
                }
                if (!isObject(demos)) {
					console.log({status: 500, data: "Invalid argument! The first parameter should be an object!"});
                    return; 
                }
                if (typeof upsert !== "boolean"){
					console.log({status: 500, data: "Invalid argument! The second parameter should be a boolean!"});
                    return; 
                }
                
                //Return url
                var _return = document.location.href;
                var _sid = App.cookie.read("oc-js-session") || "";
                var _params = {
                        "__cuuid" 	: App.onecount.getClientId(),
                        "ocid_hash" : ocid_cookie,
                        "sid" 		: _sid,
                        "lookup_demos" : JSON.stringify(demos), 
                        "return" 	: en(_return),
                        "callback"  : "GCN.onecount.IdentityResponse",
                        "upsert"	: upsert,
                };
                var url = App.url.build(sync, _params);
                //Do the redirect now in order to try to log the user in ONEcount.
                App.script.addAsync(url);
                return;
            }catch(e) {
                console.log(e);
            }
        };
})(GCN, window);
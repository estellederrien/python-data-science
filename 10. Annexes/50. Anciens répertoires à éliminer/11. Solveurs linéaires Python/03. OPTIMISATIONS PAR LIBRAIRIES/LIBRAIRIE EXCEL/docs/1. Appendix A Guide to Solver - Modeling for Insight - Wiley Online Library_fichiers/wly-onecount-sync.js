
GCN.onecount.ThirdPartySyncResponse = function(response) {
	console.log("In 3rd Party response");
	console.log(response);
	
	try {
		if(response.status && response.status == 300)
			document.location = response.data;
		
	}catch(e) {
		console.log(e);
	}
	
};

refreshIntervalId = null;


function getUserId() {
	
	var userId = "";
	
	if(digitalData && digitalData.identities) {
		
		for(var i = 0; i < digitalData.identities.length; i++) {
			var identity = digitalData.identities[i];
			
			if(identity && identity.type && identity.type == "PersonUser") {
				userId = identity.uuid || "";
				break;
			}
		}
		
	}
	
	return userId;
}

(function(App, w) {
	'use strict';
    var d = w.document,
        en = encodeURIComponent;
    
    var protocol = document.location.protocol;
    
    var sync = protocol + "//wly-validate.onecount.net/onecount/api/3rdparty/index.php";
    
	var ocid_cookie = App.cookie.read("__ocid") || "";
	var sync_cookie_name = "__oc_third_party_sync";
	
	//Read the cookie that contains the flag.
	var sync_cookie_value = App.cookie.read(sync_cookie_name);
	
	//Aborrt we have already checked this
	if(sync_cookie_value != null && parseInt(sync_cookie_value) > 0)
		return;
	
	//Abort user is logged in
	if(ocid_cookie != null && ocid_cookie.length == 64)
		return;
	
	try {
		
		var userId = getUserId();
		
		if(userId && userId.length > 0) {
						
			App.cookie.set(sync_cookie_name, "1", {expires : App.timer.nD(1)}); // production
			
			//Return url
			var _return = document.location.href;
			var _sid = App.cookie.read("oc-js-session") || "";
			var lookupId = 237;
			
			var _params = {
					"__cuuid" 	: App.onecount.getClientId(),
					"ocid_hash" : ocid_cookie,
					"sid" 		: _sid,
					"return" 	: en(_return),
					"lookupField" : lookupId,
					"callback"  : "GCN.onecount.ThirdPartySyncResponse",
			};
			
			_params['mapping[' + lookupId + ']'] = "userId";
			
			_params['field[userId]'] = userId;
			
			var url = App.url.build(sync, _params);
			
			//Do the redirect now in order to try to log the user in ONEcount.
			App.script.addAsync(url);
			
		}
		
	}catch(e) {
		console.log(e);
	}
	
})(GCN, window);
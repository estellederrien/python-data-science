function ocUrlParam(name){
   var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
   if (results==null) {
      return null;
   }
   return decodeURI(results[1]) || 0;
}
var __contact_id = ocUrlParam('elq_cid');
if(__contact_id !== undefined && __contact_id !== null) {
    var identifyDemoObj = {};
    var oc_demo_contact_id = 267;
    identifyDemoObj[oc_demo_contact_id] = __contact_id;
    GCN.onecount.identify(identifyDemoObj, false);
}
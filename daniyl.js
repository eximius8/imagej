var w = new Array();
var resolut=30;
function main () {
   var l = vector_text(-100,0,"Danyil Huraskin, PhD");
   l.forEach(function(pl) {                   // pl = polyline (not closed)
   w.push(rectangular_extrude(pl, {w: 3, h: 5}));   // extrude it to 3D
}); 
   
  // w.push(cyl);
   return w;
}

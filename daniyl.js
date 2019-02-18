var w = new Array();
var resolut=30;
function main () {
   var l = vector_text(-100,10,"Danyil Huraskin, PhD");
   l.forEach(function(pl) {                   // pl = polyline (not closed)
     w.push(rectangular_extrude(pl, {w: 3, h: 60}));   // extrude it to 3D 
   });
   var charpcube=CSG.cube({ 
            corner1: [-110,-30,0],
            corner2: [235,37,50]
        });
         w.push(charpcube);
   
  // w.push(cyl);
  var l = vector_text(-130,-30,"FAU");
   l.forEach(function(pl) {         // pl = polyline (not closed)
         var letter=
         difference(rectangular_extrude(pl, {w: 4, h: 70}),
        CSG.cube({ 
            corner1: [-200,-9,0],
            corner2: [0,-10,200]
        }),
         CSG.cube({ 
            corner1: [-200,-11,0],
            corner2: [0,-12,200]
        }),
         CSG.cube({ 
            corner1: [-200,-13,0],
            corner2: [0,-14,200]
        }),
         CSG.cube({ 
            corner1: [-200,-15,0],
            corner2: [0,-16,200]
        }),
         CSG.cube({ 
            corner1: [-200,-17,0],
            corner2: [0,-18,200]
        }),
         CSG.cube({ 
            corner1: [-200,-19,0],
            corner2: [0,-20,200]
        }),
         CSG.cube({ 
            corner1: [-200,-21,0],
            corner2: [0,-22,200]
        }),
         CSG.cube({ 
            corner1: [-200,-23,0],
            corner2: [0,-24,200]
        }),
         CSG.cube({ 
            corner1: [-200,-25,0],
            corner2: [0,-26,200]
        }),
         CSG.cube({ 
            corner1: [-200,-27,0],
            corner2: [0,-28,200]
        }),
         CSG.cube({ 
            corner1: [-200,-29,0],
            corner2: [0,-30,200]
        })
        )
      w.push(letter.scale(0.8));   // extrude it to 3D 
      });
   return w;
}

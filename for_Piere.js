var w = new Array();
var resolut=30;
function main () {
    var tryag =linear_extrude({ height: 55 }, 
        polygon({ points: [ [7,2],[7,-2],[12,0]] }));
    var tryag2=linear_extrude({ height: 50 }, 
        polygon({ points: [ [28,6.5],[28,-6.5],[-30,-3],[-30,3]] }));
        
    var rad_val=[0.5,1,1.5,2,2.5,3,3.5];
    var cyl_x=[-26.5,-22,-16,-9,0,10,22];
    var cyl = union(
    difference(
       tryag2,
        cylinder({
            start: [cyl_x[0],0,0],
            end: [cyl_x[0],0,50],
            r: rad_val[0],
            resolution: resolut
        }),
         cylinder({
            start: [cyl_x[1],0,0],
            end: [cyl_x[1],0,50],
            r: rad_val[1],
            resolution: resolut
        }),
         cylinder({
            start: [cyl_x[2],0,0],
            end: [cyl_x[2],0,50],
            r: rad_val[2],
            resolution: resolut
        }),
         cylinder({
            start: [cyl_x[3],0,0],
            end: [cyl_x[3],0,50],
            r: rad_val[3],
            resolution: resolut
        }),
         cylinder({
            start: [cyl_x[4],0,0],
            end: [cyl_x[4],0,50],
            r: rad_val[4],
            resolution: resolut
        }),
         cylinder({
            start: [cyl_x[5],0,0],
            end: [cyl_x[5],0,50],
            r: rad_val[5],
            resolution: resolut
        }),
        cylinder({
            start: [cyl_x[6],0,0],
            end: [cyl_x[6],0,50],
            r: rad_val[6],
            resolution: resolut
        })
    )
    );
  var cyl2 = union(
    difference(
       CSG.cube({ 
            corner1: [-30,-10, 0],
            corner2: [30, 10, 50]
        }),
        cylinder({r: 2, h: 50}),
        CSG.cube({
            corner1: [-25,-1,0],
            corner2: [-23,1,50]
        }),
        CSG.cube({
            corner1: [-18,-2,0],
            corner2: [-14,2,50]
        }),
        CSG.cube({
            corner1: [-10,-2,0],
            corner2: [-8,2,50]
        }),
        tryag
    )
    
  );
   w.push(cyl);
   return w;
}

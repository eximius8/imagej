var w = new Array();
function main() {
// Vertical Tensile cylinders
    var radcyl = 4;
    var hcyl = 70;
    var resolut = 5;
    var cyl1coord = [
        [-90, 10],
        [-90, -10],
        [-90, -30],
        [-90, -50],
        [-90,-70]];
// Horizontal Tensile cylinders
    var cyl2uber = 6;
    var angle=1.05*Math.PI;
    var cyl2coord = [
        [25,100,angle],
        [10,100,angle],
        [70,100,angle],
        [55,100,angle],
        [40,100,angle]];
// LECO cylinders
    var lecorad=1.75;
    var lecoh =8;
    var lecocon=100;
    var lecocoord = [
        [Math.sqrt(20),0],
        [-2,4],
        [-2,-4],
        [lecocon+Math.sqrt(20),lecocon+0],
        [lecocon-2,lecocon+4],
        [lecocon-2,lecocon-4],
        [Math.sqrt(20)-lecocon,lecocon+0],
        [-lecocon-2,lecocon+4],
        [-lecocon-2,lecocon-4],
        [Math.sqrt(20)+lecocon,0-lecocon],
        [-2+lecocon,4-lecocon],
        [-2+lecocon,-4-lecocon],
        [Math.sqrt(20)-lecocon,0-lecocon],
        [-2-lecocon,4-lecocon],
        [-2-lecocon,-4-lecocon]
        ];
// Charpy specimens
    var charpcoord1 =[
        [80,-60,0],
        [80,20,0],
        [80,0,0],
        [80,-20,0],
        [80,-40,0]
        ];
// Charpy specimens flat
    var dist_from_surface=cyl2uber;
    var charpcoord2 =[
        [-40,-80,dist_from_surface],
        [40,-80,dist_from_surface],
        [20,-80,dist_from_surface],
        [0,-80,dist_from_surface],
        [-20,-80,dist_from_surface]
        ];
// cubes 8x8x13
    var cubecoord =[
        [60,-60,0],
        [60,-80,0],
        [60,0,0],
        [60,-20,0],
        [60,-40,0],
        [-70,-60,0],
        [-70,-80,0],
        [-70,0,0],
        [-70,-20,0],
        [-70,-40,0]
        ];
// Fatique samples
    var fatrad=6;
    var fath=84;
    var fatique1 =[
        [-95,80],
        [-75,90],
        [-55,90],
        [-35,90],
        [-15,90]
        ];
// Fatique stand
    for (var i = 0; i < fatique1.length; i++)
    {
        var fatcyl1=CSG.cylinder({
        start: fatique1[i].concat([0]),
        end: fatique1[i].concat([fath]),
        radius: fatrad,
        resolution: resolut
        });
         w.push(fatcyl1);
    }
    for (var i = 0; i < cyl1coord.length; i++)
    {
        var cyl1=CSG.cylinder({
        start: cyl1coord[i].concat([0]),
        end: cyl1coord[i].concat([hcyl]),
        radius: radcyl,
        resolution: resolut
        });
         w.push(cyl1);
    }
    
    for (var j = 0; j < cyl2coord.length; j++)
    {
        var cyl2=CSG.cylinder({
        start: [cyl2coord[j][0],cyl2coord[j][1], cyl2uber],
        end: [cyl2coord[j][0]+hcyl*Math.sin(cyl2coord[j][2]),
              cyl2coord[j][1]+hcyl*Math.cos(cyl2coord[j][2]),
              cyl2uber
        ],
        radius: radcyl,
        resolution: resolut
        });
         w.push(cyl2);
    }
    for (var k = 0; k < lecocoord.length; k++)
    {
        var lecocyl=CSG.cylinder({
        start: lecocoord[k].concat([0]),

        end: lecocoord[k].concat([lecoh]),
        radius: lecorad,
        resolution: resolut
        });
         w.push(lecocyl);
    }
    for (var m = 0; m < charpcoord1.length; m++)
    {
        var charpcube=CSG.cube({ 
            corner1: charpcoord1[m],
            corner2: [charpcoord1[m][0]+10,
            charpcoord1[m][1]+10,
            charpcoord1[m][2]+55 // Standard 55
            ]
        });
         w.push(charpcube);
    }
    // Charpy horizontal
    for (var l = 0; l < charpcoord2.length; l++)
    {
        var charpcube2=CSG.cube({ 
            corner1: charpcoord2[l],
            corner2: [charpcoord2[l][0]+10,
            charpcoord2[l][1]+55,
            charpcoord2[l][2]+10 // Standard 55
            ]
        });
         w.push(charpcube2);
    }
     for (var n = 0; n < cubecoord.length; n++)
    {
        var cube88=CSG.cube({ 
            corner1: cubecoord[n],
            corner2: [cubecoord[n][0]+8,
            cubecoord[n][1]+8,
            cubecoord[n][2]+13 // Standard 13
            ]
        });
         w.push(cube88);
    }
    return w;
}

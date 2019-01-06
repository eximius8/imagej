var w = new Array();
function main() {
    // Vertical Tensile cylinders
    var radcyl = 4;
    var hcyl = 70;
    var resolut = 5;
    var cyl1coord = [
        [15, 15],
        [15, -15],
        [-15, 15],
        [-15, -15],
        [0,-28]];
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
// cubes 8x8x13
    var cubecoord =[
        [60,-60,0],
        [60,-80,0],
        [60,0,0],
        [60,-20,0],
        [60,-40,0]
        ];
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

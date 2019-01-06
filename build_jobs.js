var w = new Array();
function main() {
    // Vertical Tensile cylinders
    var radcyl = 4;
    var hcyl = 70;
    var resolut = 3;
    var cyl1coord = [
        [10, 10],
        [20, -20],
        [-20, 20],
        [-20, -20]];
// Horizontal Tensile cylinders
    var cyl2uber = 6;
    var angle=1.05*Math.PI;
    var cyl2coord = [
        [100,100,angle],
        [85,100,angle],
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
    return w;
}

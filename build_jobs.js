var w = new Array();
function main() {
    var radcyl = 4;
    var hcyl = 70;
    var resolut = 7;
    var cyl1coord = [[10, 10], [20, -20], [-20, 20], [-20, -20]];
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
    var cyl2uber = 50;
    var angle=Math.PI/3;
    var cyl2coord = [[30,0,angle],[-30,0,angle],[0,30,angle],
    [0,-30,angle]];
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
    return w;
}

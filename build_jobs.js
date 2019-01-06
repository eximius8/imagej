var w = new Array();
function main() {
    var radcyl = 4;
    var hcyl = 70;
    var resolut = 30;
    var coord = [[40, 20], [40, -20], [-40, 20], [-40, -20]];
    var corlength = coord.length;
    for (var i = 0; i < corlength; i++)
    {
        var cyl=CSG.cylinder({
        start: coord[i].concat([0]),
        end: coord[i].concat([hcyl]),
        radius: radcyl,
        resolution: resolut
        });
         w.push(cyl);
    }
    return w;
}

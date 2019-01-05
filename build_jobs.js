var w = new Array();
function main() {
    var radcyl = 4;
    var hcyl = 70;
    var resolut = 30;
    cyl1=CSG.cylinder({
        start: [40, 20, 0],
        end: [40, 20, hcyl],
        radius: radcyl,
        resolution: resolut
    });
    w.push(cyl1);
    return w;
}

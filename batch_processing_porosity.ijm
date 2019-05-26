run("8-bit");
run("Set Scale...", "distance=970.5 known=1000 unit=um global");
setTool(2); 
makePolygon(350,650,6900,650,6900,10200,5300,10200,5300,10600,350,10600); 
setThreshold(0, 161);
setBatchMode(false);
//Table.deleteRows(0, 5);
waitForUser("Draw ROI, then hit OK"); 
run("Measure");
setBatchMode(true);

// latest version
setBatchMode(true);
run("8-bit");
run("Set Scale...", "distance=970.5 known=1000 unit=um global");
setTool(2); 
makePolygon(470,1500,6800,1500,6800,8900,470,8900); 
setAutoThreshold("Default");
//setBatchMode(false);
//Table.deleteRows(0, 5);
//waitForUser("Draw ROI, then hit OK"); 
run("Measure");
run("Analyze Particles...", "size=5-4000 display include summarize record");
//print(getDirectory("image")+substring(File.name,0,2)+".csv");
selectWindow("Results");
saveAs("Results",getDirectory("image")+substring(File.name,0,2)+".csv");
run("Clear Results");
selectWindow("Summary");
saveAs("Text",getDirectory("image")+substring(File.name,0,2)+"S.csv");
close();

// create ROIs for subsequent measurements
setTool(2); 
setBatchMode(false);
waitForUser("Draw ROI, then hit OK"); 
setBatchMode(true);
roiManager("Add");
roiManager("Select", 0);
roiManager("Save", getDirectory("image")+"RoiCsv/"+substring(File.name,0,2)+".roi");
roiManager("Deselect");
roiManager("Delete");

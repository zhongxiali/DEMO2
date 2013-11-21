#Zhongxia Li 321008250 

import arcpy

#setting the workspace
works = arcpy.GetParameterAsText(0)
arcpy.env.workspace = works

arcpy.env.overwriteOutput = True
Output = arcpy.GetParameterAsText(1)
raster_list = arcpy.ListRasters()
feature_list = arcpy.ListFeatureClasses()
file_handle = open(Output, 'w')
file_handle.write('file,type,geometry,projected,coordinate system\n')
for fileN in feature_list:
	desc = arcpy.Describe(fileN)
	name = desc.file
	filetype = desc.datasetType
	geometry = desc.shapeType
	projection = desc.spatialReference.type
	coordSys = desc.spatialReference.name
	finalString = name + ',' + filetype + ',' + geometry + ',' + projection + ',' + coordSys
	file_handle.write(finalString)
	file_handle.write('\n')
	
#adds the raster info to csv
for raster in raster_list:
	desc2 = arcpy.Describe(raster)
	name = desc2.file
	filetype = desc2.datasetType
	geometry = desc2.tableType
	projection = desc2.spatialReference.type
	coordSys = desc2.spatialReference.name
	finalString = name + ',' + filetype + ',' + geometry + ',' + projection + ',' + coordSys
	file_handle.write(finalString)
	file_handle.write('\n')         

#closes the file
file_handle.close()

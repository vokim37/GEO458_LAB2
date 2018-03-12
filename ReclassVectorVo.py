import arcpy

# Take in inputs from users
infile = arcpy.GetParameterAsText(0)
infield = arcpy.GetParameterAsText(1)
outfield = arcpy.GetParameterAsText(2)
reclassTable = arcpy.GetParameterAsText(3)
notFoundValue = arcpy.GetParameterAsText(4)
output = arcpy.GetParameterAsText(5)

# Create a copy of original shp
arcpy.CopyFeatures_management(infile,output)
# Add new field to the copied shp
arcpy.AddField_management(output, outfield, "DOUBLE")

# Loop through given table and update output shp
curU = arcpy.da.UpdateCursor(output, [infield, outfield])
for row in curU:
    curS = arcpy.da.SearchCursor(reclassTable,["lowerbound", "upperbound", "value"]) 
    found = False
    for line in curS:
        if (row[0] >= line[0] and row[0] <= line[1]):
            row[1] = line[2]
            curU.updateRow(row)
            found = True    # flag for notFoundValue
            break           # if value found, exit the loop
    if not found:
        row[1] = notFoundValue
        curU.updateRow(row)

del curS
del curU

# I worked with Marvin to brainstorm step-by-step proccess.
# Then I developed these codes after we talked.

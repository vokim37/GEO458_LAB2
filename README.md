# Kim Vo

---

A python script of Reclassification tool. This tool can be generate in ArcMap to reclassify vector data. 

Required input features: a feature class, a database table with predefined schema.

To find my tool: <br />
Connect to this Server: <http://geog-gs01.geog.uw.edu:6080/arcgis/services/458_vokim37><br />
Look for folder name: **456_vokim37**<br />
Tool name: **ReclassVectorVo**<br />

**Image 1:** Population Density in Seattle 2012 (matched with sample output)

![alt text](https://github.com/UW-Geog458-Win2018/vokim37/blob/master/Lab2/KingReclass12.png)

**Image 2:** Population Density in Seattle 2017 (tested with another datatset and reclassify table)

New reclassify value:<br />
lowerbound,upperbound,value<br />
0,&nbsp;&nbsp;&nbsp;&nbsp;100,&nbsp;&nbsp;&nbsp;&nbsp;1<br />
100,&nbsp;&nbsp;&nbsp;&nbsp;4000,&nbsp;&nbsp;&nbsp;&nbsp;2<br />
4000,&nbsp;&nbsp;&nbsp;&nbsp;100000,&nbsp;&nbsp;&nbsp;&nbsp;3<br />
100000,&nbsp;&nbsp;&nbsp;&nbsp;130000,&nbsp;&nbsp;&nbsp;&nbsp;4<br />
Not found value set to be -1

![alt text](https://github.com/UW-Geog458-Win2018/vokim37/blob/master/Lab2/KingReclass2017.png)



# Solar-Deployment-in-California

The Solar Deployment Visualization Project provides an interactive choropleth for all residential solar installations recorded as part of the Go Solar California initiative. 

Statistics from Go Solar California are updated periodically but fall off dramatically in 2014 and 2015. 

The GSC CSV file can be downloaded from the Go Solar California site here: 
https://www.californiasolarstatistics.ca.gov/current_data_files/


New York State (NY-Sun) maintains a similar database which may be included in a future visualization project.
http://ny-sun.ny.gov/For-Installers/Solar-Installation-Data-and-Tools


The choropleth groups installations by zip code. Shapefile data is provided by Geo Commons: http://geocommons.com

Project Details 
Shapefiles are converted to GeoJSON using ogr2ogr and then to TopoJSON using topojson. 
The map rendering is done using D3. 
The map projection is Albers USA.
The solar statistics can either be served through the Django API or through a CSV file. 


Acknowledgements: 

Suffens Map Tutorial: 
https://suffenus.wordpress.com/2014/01/07/making-interactive-maps-with-d3-for-total-beginners/

Bostock’s Let’s Make A Map: 
http://bost.ocks.org/mike/map/

Ben, Andy and the gang at Oceana: 
http://oceanatech.com


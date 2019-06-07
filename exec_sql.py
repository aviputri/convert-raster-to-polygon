from osgeo import gdal

ds = gdal.OpenEx("my_shp.shp", gdal.OF_VECTOR | gdal.OF_UPDATE)
ds.ExecuteSQL("ALTER TABLE my_shp DROP COLUMN my_field")
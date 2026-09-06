from points_decorator import points
import inspect
import os
import pandas as pd
import geopandas as gpd
import pyproj

class TestProblem2:

    @points(1, "Problem 2: Did you import the grid data and check if the CRS is correct?")
    def test_problem_2_import_grid(self, problem2):
        section_data, namespace = problem2
        grid = namespace['grid']

        assert isinstance(grid, gpd.GeoDataFrame)
        assert grid.crs == pyproj.CRS.from_epsg(3067)
        

    @points(3, "Problem 2: Did you join the travel time data into the grid cells, using the correct column names?")
    def test_problem_2_centres(self, problem2):
        section_data, namespace = problem2
        grid = namespace['grid']

        expected_shopping_centres = [
            "Itis", "Myyrmanni", "Forum", "Iso_Omena", "Ruoholahti", "Dixi", "Jumbo"
            ]
        

        for shopping_centre in expected_shopping_centres:
            assert f"pt_r_t_{shopping_centre}" in grid.columns  

   
    @points(3, "Problem 2: Some of the values for the nearest shopping centre seem to be incorrect.")    
    def test_problem_2_closest_shopping_centre_value(self, problem2):
        section_data, namespace = problem2
        grid = namespace['grid']

        row1 = grid.loc[5785641]
        assert row1['dominant_shopping_centre'] == "Myyrmanni"

        row2 = grid.loc[5876274]
        assert row2['dominant_shopping_centre'] == "Itis"

        row3 = grid.loc[5785641]
        assert row3['dominant_shopping_centre'] == "Myyrmanni"
    
    @points(1.5, "Problem 2: Did you save the plot as a PNG file?")
    def test_problem_2_plot_file_exists(self,problem2):
        section_data, namespace = problem2

        png_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'dominance_areas.png')
        assert os.path.exists(png_file)

    @points(1.5, "Problem 2: Did you check that the PNG file is not empty?")
    def test_problem_2_plot_file_not_empty(self,problem2):

        section_data, namespace = problem2
        png_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'dominance_areas.png')
        assert os.path.getsize(png_file) > 0

        
    

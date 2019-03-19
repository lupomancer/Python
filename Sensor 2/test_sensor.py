from unittest import TestCase
from sensor import Sensor
import inspect
import csv
from unittest.mock import MagicMock
from unittest.mock import patch, mock_open

class TestSensor(TestCase): 
    TEST_READINGS = [ 
        ["2018-09-23 19:56:01.345", "1", "ABC Sensor Temp M301A", "20.152", "21.367", "22.005", "OK"], 
        ["2018-09-23 19:57:02.321", "2", "ABC Sensor Temp M301A", "20.163", "21.435", "22.103", "OK"], 
        ["2018-09-23 19:58:01.324", "3", "ABC Sensor Temp M301A", "20.142" ,"21.528", "21.803", "OK"], 
        ["2018-09-23 19:59:03.873", "4", "ABC Sensor Temp M301A", "20.212", "21.641", "22.017", "OK"], 
        ["2018-09-23 20:00:01.453", "5", "ABC Sensor Temp M301A", "100.000", "100.000", "100.000", "HIGH_TEMP"], 
        ["2018-09-23 20:01:01.111", "6", "ABC Sensor Temp M301A", "21.244", "21.355", "22.103", "OK"], 
        ["2018-09-23 20:02:02.324", "7", "ABC Sensor Temp M301A", "21.112", "22.345", "22.703", "OK"], 
        ["2018-09-23 20:03:02.744", "8", "ABC Sensor Temp M301A", "20.513", "21.745", "22.105", "OK"], 
        ["2018-09-23 20:04:01.123", "9", "ABC Sensor Temp M301A", "20.333", "21.348", "21.943", "OK"], 
        ["2018-09-23 20:04:01.999", "10", "ABC Sensor Temp M301A", "20.332", "21.445", "22.013", "OK"], 
        ["2018-09-23 20:04:02.001", "11", "ABC Sensor Temp M301A", "-50.000", "-50.000", "-50.000","LOW_TEMP"] ]
        
        # This mocks the builtin file open method in python always return '1' for the file data 
        #  We don’t care about the returned file data since we are mocking the csv reader as well. 





    @patch('builtins.open', mock_open(read_data='1')) 
    def setUp(self):
        
        # This mocks the csv reader to return our test readings 
        csv.reader = MagicMock(return_value=TestSensor.TEST_READINGS) 
        self.sensor1 = Sensor("testresults.csv") 

        self.logPoint()
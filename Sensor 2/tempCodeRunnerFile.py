@patch('builtins.open', mock_open(read_data='1')) 
def setUp(self):
    
    # This mocks the csv reader to return our test readings 
    csv.reader = MagicMock(return_value=TestSensor.TEST_READINGS) 
    self.sensor1 = Sensor("testresults.csv") 

    self.logPoint()
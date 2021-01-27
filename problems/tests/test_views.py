from django.test import TestCase

class ViewsTestCase(TestCase):
    
    # correct
    def test_problema1_view(self):
        _data = """Junior
Buenisimos 3 Malisimos 0
Buenillos 2 Malillos 1
Buenillos 3 Malisimos 0
Buenisimos 3 Malillos 0
Buenisimos 2 Buenillos 1
Malisimos 0 Buenisimos 3
Malillos 1 Buenillos 2
Malisimos 0 Buenillos 3
Malillos 0 Buenisimos 3
Buenillos 1 Buenisimos 2
FIN
Senior
Abuelos 3 Abueletes 0
Abueletes 2 Abuelos 1
FIN
"""
        response = self.client.post('/api/problem-1/',{'input_data':_data})
        self.assertEqual(response.status_code, 200)

    def test_problema2_view(self):
        _data = "5 3\n4 3\n5 5\n4 2\n2 3"
        response = self.client.post('/api/problem-2/',{'input_data':_data})
        self.assertEqual(response.status_code, 200)
    
    def test_problema3_view(self):
        _data = 'aaadfg'
        response = self.client.post('/api/problem-3/',{'input_data':_data})
        self.assertEqual(response.status_code, 200)

    # incorrect
    def test_problem1_viewerror(self):
        response = self.client.post('/api/problem-1/',{'input_data':'**-'})
        self.assertEqual(response.status_code, 200)
    
    def test_problem2_viewerror(self):
        response = self.client.post('/api/problem-2/',{'input_data':'sdfghj'})
        self.assertEqual(response.status_code, 500)
    
    def test_problem3_viewerror(self):
        response = self.client.post('/api/problem-3/',{'input_data':'aksdkanssdasda\nasdasd\n'})
        self.assertEqual(response.status_code, 400)

    # empty
    def test_problem1_viewerror_emtpy(self):
        response = self.client.post('/api/problem-1/')
        self.assertEqual(response.status_code, 400)
    
    def test_problem2_viewerror(self):
        response = self.client.post('/api/problem-2/')
        self.assertEqual(response.status_code, 400)
    
    def test_problem3_viewerror(self):
        response = self.client.post('/api/problem-3/')
        self.assertEqual(response.status_code, 400)
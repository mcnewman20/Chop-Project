from django.test import TestCase
from dashboard.sample_controller import SampleController
from dashboard.models import Sample_Information

# Create your tests here.

class SampleControllerTestCase(TestCase):
    sampleControllerTest = SampleController()

    def setUp(self):
        Sample_Information.objects.create(aliquot_pk_serial=101, volume_remaining=59, received_on='2011-11-11',
                                          collected_on='2011-11-11', volume_received=100, available_flag=True)
        Sample_Information.objects.create(aliquot_pk_serial=102, volume_remaining=123, received_on='2011-11-11',
                                          collected_on='2011-11-11', volume_received=100, available_flag=True)
        Sample_Information.objects.create(aliquot_pk_serial=103, volume_remaining=132, received_on='2011-11-11',
                                          collected_on='2011-11-11', volume_received=100, available_flag=True)

    def test_set_current(self):
        test_code = 102
        self.sampleControllerTest.set_current(test_code)
        self.assertEqual(self.sampleControllerTest.cur_sample_num, test_code)
        self.assertEqual(self.sampleControllerTest.cur_sample.aliquot_pk_serial, test_code)

    def test_use_sample(self):
        test_code = 103
        amount_to_use = 43
        self.sampleControllerTest.set_current(test_code)
        before_amount = self.sampleControllerTest.cur_sample.volume_remaining
        self.sampleControllerTest.use_sample(amount_to_use)
        self.assertEqual(self.sampleControllerTest.cur_sample.volume_remaining, (before_amount-amount_to_use))
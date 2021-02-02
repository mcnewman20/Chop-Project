from dashboard.models import Sample_Information


class SampleController:
    def __init__(self):
        self.cur_sample = None
        self.cur_sample_num = None

    def set_current(self, code):
        self.cur_sample_num = code
        self.cur_sample = Sample_Information.objects.get(aliquot_pk_serial=code)

    def get_current(self):
        return self.cur_sample_num

    def use_sample(self, amount_to_use):
        amount_available = self.cur_sample.volume_remaining
        print(amount_to_use)
        if amount_available > amount_to_use:
            amount_available = amount_available - amount_to_use
            self.cur_sample.volume_remaining = amount_available
            self.cur_sample.save()

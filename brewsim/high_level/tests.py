from django.test import TestCase

# Create your tests here.
# test1:测试Machine模型的创建
from .models import Machine

class MachineModelTests(TestCase):
  def test_usine_creation(self):
    self.assertEqual(Machine.objects.count(), 0)
    Machine.objects.create(nom="four",prix=1_000)
    self.assertEqual(Machine.objects.count(), 1)

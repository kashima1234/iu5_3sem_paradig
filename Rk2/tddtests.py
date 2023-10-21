import unittest
from main import *
class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.deps = [
            Dep(1, 'First'),
            Dep(2, 'Second'),
            # ... остальные данные ...
        ]

        self.emps = [
            Emp(1, 'IU7-12B', 2, 11),
            Emp(2, 'IU5-11B',  1, 11),
            # ... остальные данные ...
        ]

        self.emps_deps = [
            EmpDep(1, 1),
            EmpDep(1, 2),
            # ... остальные данные ...
        ]

    def test_one_to_many(self):
        result = one_to_many(self.deps, self.emps)
        self.assertEqual(result, [('IU7-12B', 2, 'First'), ('IU5-11B', 1, 'Second')])

    def test_many_to_many(self):
        result = many_to_many(self.deps, self.emps_deps, self.emps)
        self.assertEqual(result, [('IU7-12B', 2, 'First'), ('IU5-11B', 1, 'First')])

    def test_sum_subjects_by_course(self):
        one_to_many_data = one_to_many(self.deps, self.emps)
        result = sum_subjects_by_course(self.deps, one_to_many_data)
        self.assertEqual(result, [('First', 2), ('Second', 1)])

    def test_find_subjects_by_course(self):
        many_to_many_data = many_to_many(self.deps, self.emps_deps, self.emps)
        result = find_subjects_by_course(self.deps, many_to_many_data)
        self.assertEqual(result, {'First': ['IU7-12B', 'IU5-11B']})

if __name__ == '__main__':
    unittest.main()

#Результаты выполнения:


# ----------------------------------------------------------------------
# Ran 4 tests in 0.000s

# OK

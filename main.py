import os.path as osp
from ExerciseDb import ExerciseDb

exercises_path = osp.join(
    osp.abspath(
        osp.dirname(__file__)), 
        "exercises.csv"
        )
# execiseDb = ExerciseDb(exercises_path)
# print(os.path.abspath(os.path.dirname(__file__)))
# print(os.path.expanduser(os.path.abspath(os.path.dirname(__file__))))

print(exercises_path)

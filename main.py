import json
from deepface import DeepFace
result = DeepFace.verify(img1_path=r"persons\notjay1.jpg",img2_path=r"persons\JAY2.jpg")
result["verified"] = bool(result["verified"])
print(json.dumps(result, indent=2))

result2 = DeepFace.find(img_path=r"JAY3.jpg", db_path=r"persons")
print(result2)

result_analysis = DeepFace.analyze(img_path = r"persons\notjay3.jpg")
print(json.dumps(result_analysis))
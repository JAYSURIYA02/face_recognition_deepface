import json
from deepface import DeepFace



result = DeepFace.verify(img1_path=r"persons\JAY2.JPG",img2_path=r"persons\JAY3.JPG")
result["verified"] = bool(result["verified"])
print(json.dumps(result, indent=2))




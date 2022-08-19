
# Face++

import http.client
import json


import os

os.chdir('face')


# conn = http.client.HTTPSConnection("face-detection6.p.rapidapi.com")

# payload = "{\n    \"url\": \"https://inferdo.com/img/face-3.jpg\",\n    \"accuracy_boost\": 3\n}"

# headers = {
#     'content-type': "application/json",
#     'X-RapidAPI-Host': "face-detection6.p.rapidapi.com",
#     'X-RapidAPI-Key': "fe323033e9msh38cf69ae65ed85ap12fe29jsn45f450231eae"
#     }

# conn.request("POST", "/img/face-age-gender", payload, headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))




# curl -X POST "https://api-us.faceplusplus.com/facepp/v3/detect" -F "api_key=n8bNeZbWOTwn9FAMRl2rwfpxwbH44a7Q" \
# -F "api_secret=dKI8bmEl_bMY00oE1VLySzZLxK32v6Xq" \
# -F "image_file=@image_file.jpg" \
# -F "return_landmark=1" \
# -F "return_attributes=gender,age"


files = os.listdir('.')
# print(files)
total = 0
total_files = 0

images_with_faces = []

for f in files:
	if not f.endswith('.jpeg'): continue
	total_files += 1

	msg = """curl -X POST "https://api-us.faceplusplus.com/facepp/v3/detect" -F "api_key=n8bNeZbWOTwn9FAMRl2rwfpxwbH44a7Q" \
	-F "api_secret=dKI8bmEl_bMY00oE1VLySzZLxK32v6Xq" \
	-F "image_file=@"""

	msg = msg + f + "\""

	result = os.popen(msg).read()
	res = json.loads(result)

	print(res)
	if res.get("face_num", 0) > 0:
		images_with_faces.append((f, res))
		total = total + 1
		print("total detections: " + str(total))

	print(f + "   " + str(res.get("face_num", 0)))

print(total/total_files)
# print(len(files)-1)

print(images_with_faces)









# # n8bNeZbWOTwn9FAMRl2rwfpxwbH44a7Q
# # dKI8bmEl_bMY00oE1VLySzZLxK32v6Xq

curl -H "Ocp-Apim-Subscription-Key:6122f16de8e545b1b0fc8c18eafbbf45" "https://borjiface.cognitiveservices.azure.com/face/v1.0/detect?detectionModel=detection_03&returnFaceId=true" -H "Content-Type: application/json" --data-ascii "{\"url\":\"https://upload.wikimedia.org/wikipedia/commons/c/c3/RH_Louise_Lillian_Gish.jpg\"}"




# @ECHO OFF

curl -v -X POST "https://borjiface.cognitiveservices.azure.com/face/v1.0/detect?detectionModel=detection_03&returnFaceId=true" \
-H "Content-Type: application/json" \
-H "Ocp-Apim-Subscription-Key:6122f16de8e545b1b0fc8c18eafbbf45" \
--data-ascii "{\"url\":\"https://drive.google.com/file/d/1gW1Cm-8sbtPc2N6mJlVaic-wJFvvYqEs/view?usp=sharing\"}"

--data-ascii "{body}" 
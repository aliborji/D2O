

# https://api-us.faceplusplus.com/humanbodypp/beta/detect

import http.client
import json


import os

os.chdir('person')



files = os.listdir('.')
# print(files)
total = 0
total_files = 0

images_with_bodies = []

for f in files:
	if not f.endswith('.jpeg'): continue
	total_files += 1

	msg = """curl -X POST "https://api-us.faceplusplus.com/humanbodypp/beta/detect" -F "api_key=n8bNeZbWOTwn9FAMRl2rwfpxwbH44a7Q" \
	-F "api_secret=dKI8bmEl_bMY00oE1VLySzZLxK32v6Xq" \
	-F "image_file=@"""

	msg = msg + f + "\""

	result = os.popen(msg).read()
	res = json.loads(result)

	# print(res)
	if len(res.get("humanbodies", [])) > 0:
		images_with_bodies.append((f, res))
		total = total + 1
		print("total detections: " + str(total))

	# print(f + "   " + str(res.get("face_num", 0)))

print(total/total_files)
# print(len(files)-1)

print(images_with_bodies)









# # n8bNeZbWOTwn9FAMRl2rwfpxwbH44a7Q
# # dKI8bmEl_bMY00oE1VLySzZLxK32v6Xq
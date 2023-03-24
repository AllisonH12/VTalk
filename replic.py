import replicate

model = replicate.models.get("methexis-inc/img2prompt")
version = model.versions.get("50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5")

# https://replicate.com/methexis-inc/img2prompt/versions/50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5#input
inputs = {
    # Input image
    'image': open("/Users/yonghuang/code/VTalk/images/anger.jpeg", "rb"),
}

# https://replicate.com/methexis-inc/img2prompt/versions/50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5#output-schema
output = version.predict(**inputs).split(',')

print(output[0])

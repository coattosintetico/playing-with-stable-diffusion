import base64
import json
import io

from PIL import Image
import requests

PROMPT = "maltese puppy with cowboy hat"
NO_OF_STEPS = 25
SEED = -1

OUTPUT_PATH = "./puppy.jpg"

URL = r"http://127.0.0.1:7861/sdapi/v1/txt2img"

print(f"Generating image...")
payload = {
    "prompt": PROMPT,
    "steps": NO_OF_STEPS,
    "seed": SEED,
}

response = requests.post(URL, data=json.dumps(payload))
r = response.json()

img_with_metadata_string = r['images'][0]
# seems like there's no metadata, but just in case
img_string = img_with_metadata_string.split(",",1)[0]

with io.BytesIO(base64.b64decode(img_string)) as image_stream:
    image = Image.open(image_stream)
    image.save(OUTPUT_PATH)
    print(f"Image generated and saved succesfully.")
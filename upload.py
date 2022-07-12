import base64
import os
import sys
from imagekitio import ImageKit

imagekit = ImageKit(
    public_key='public_MVM6V7+TK3lTsWIqX+/c507lJ00=',
    private_key='private_Emhv3vwONUoNxK9VehKKwrZ2t/8=',
    url_endpoint = 'https://upload.imagekit.io/api/v1/files/upload'
)

upload = imagekit.upload(
    file=open("Screenshot.png", "rb"),
    file_name="Screenshot.png",
    options={
        "response_fields": ["is_private_file", "tags"],
        "tags": ["tag1", "tag2"]
    },
)

# print("Upload binary", upload)





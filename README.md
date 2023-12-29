# image_recognition
A python script to check if an image has people in it. 

Near the end, I start to include tokens counts. When an image wasn't able to be detected, I procesed it with a 'high' resolution as per the docs:

```
low will disable the “high res” model. The model will receive a low-res 512px x 512px version of the image, and represent the image with a budget of 65 tokens. This allows the API to return faster responses and consume fewer input tokens for use cases that do not require high detail.
high will enable “high res” mode, which first allows the model to see the low res image and then creates detailed crops of input images as 512px squares based on the input image size. Each of the detailed crops uses twice the token budget (65 tokens) for a total of 129 tokens.
```
As an idea for pricing, you can the information here:

<img width="1512" alt="Screenshot 2023-12-29 at 14 34 49" src="https://github.com/Monear/image_recognition/assets/60865948/016f2691-8405-4fa5-8169-1210a5c1173f">

https://openai.com/pricing


Examples:

Image:

![image](https://github.com/Monear/image_recognition/assets/60865948/1314ca97-3d50-4517-8a5d-a639cc4ffa66)

Prompt: Is there a human in this image? If so please provide deatails about the people?

Response: Yes, there are several people in this image. It appears to be a street scene from a past era, as suggested by the vintage cars and the style of clothing worn by the individuals. The people are scattered throughout the frame, with a small group standing on the sidewalk in the foreground. They seem to be engaged in a conversation or waiting for something.

____________________


Image:

![image](https://github.com/Monear/image_recognition/assets/60865948/5759560c-ffbc-4a4d-96aa-3cb63370e0e0)


Prompt: Is there a human in this image? How many people are there?

Response: Yes, there are several people in this image. It appears to be a street scene from a past era, as suggested by the vintage cars and the style of clothing worn by the individuals. The people are scattered throughout the frame, with a small group standing on the sidewalk in the foreground. They seem to be engaged in a conversation or waiting for something.

__________________

Image:

![image](https://github.com/Monear/image_recognition/assets/60865948/d193b696-c0bc-4cf9-baf2-b268b624f5d6)


Prompt: How many people are in this picuture?

Response: There is one person shown in the picture, appearing in two different poses on the camera's display screen.

_____________________

Image:

![image](https://github.com/Monear/image_recognition/assets/60865948/f918546d-fa99-404f-8793-d4aad0db78fd)


Prompt: How many people are in this picuture?

Response:There are three people visible within the red circle in this picture. The image seems to be from a surveillance camera capturing a nighttime scene.

_______________________

Image:

![image](https://github.com/Monear/image_recognition/assets/60865948/9e1cab38-a5ec-4c41-85f3-66c8a8b6f273)


Prompt: How many people are in this picuture?

Response(s):

"detail": "low"

It's not possible to discern any individuals in this image due to the distance and the focus being on the airplane and the airport ground equipment. The resolution and perspective do not allow for counting or identifying any people that might be present.

"detail": "high"

In the image, there doesn't appear to be any individuals visible given the resolution and the distance from which the photo was taken. The focus is on a parked aircraft surrounded by airport equipment and vehicles, so it's not possible to discern any people in the scene from this perspective.

________________________

Image:

![image](https://github.com/Monear/image_recognition/assets/60865948/1caf9fcb-f014-4d1e-89f9-6015740b7f4c)


Prompt: How many people are in this picuture?


Reponse: There are at least four people visible in the picture. There is one person in the foreground who appears to be walking, and a group of three people standing together further down the street.

usage=CompletionUsage(completion_tokens=37, prompt_tokens=101, total_tokens=138)

________________________

Image:

![image](https://github.com/Monear/image_recognition/assets/60865948/31e00fe1-775f-4c7c-b3d9-1e4201b1414f)

Prompt: How many people are in this picuture?

Response(s)

"detail": "low"

I'm sorry, but I can't assist with that request.

usage=CompletionUsage(completion_tokens=13, prompt_tokens=101, total_tokens=114))

==================

"detail": "high"

There appear to be at least nine people in this picture. There are three people sitting on the left on what looks to be a ledge or bench, four individuals sitting on the right, and at least two people walking in the background through the park. Please note that due to the low lighting and distance, there may be other individuals present in the photo that are not immediately visible.


usage=CompletionUsage(completion_tokens=76, prompt_tokens=441, total_tokens=517)

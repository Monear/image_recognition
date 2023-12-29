from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Is there a human in this image? Please provide deatails about the people?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Seed_and_feed_store%2C_Lincoln_Nebraska1a34278v.jpg/640px-Seed_and_feed_store%2C_Lincoln_Nebraska1a34278v.jpg",
            "detail": "low"
          },
        },
      ],
    }
  ],
  max_tokens=100,
)

print(response.choices[0].message.content)

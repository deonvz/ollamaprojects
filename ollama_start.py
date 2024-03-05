import ollama

#More example: https://github.com/ollama/ollama-python/tree/main/examples

response = ollama.chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])

#Streaming
for chunk in chat('mistral', messages=messages, stream=True):
  print(chunk['message']['content'], end='', flush=True)

#Multi-modal
with open('image.png', 'rb') as file:
  response = ollama.chat(
    model='llava',
    messages=[
      {
        'role': 'user',
        'content': 'What is strange about this image?',
        'images': [file.read()],
      },
    ],
  )
print(response['message']['content'])
#Text Completion
result = ollama.generate(
  model='stable-code',
  prompt='// A c function to reverse a string\n',
)
print(result['response'])
#Creating custom models
modelfile='''
FROM llama2
SYSTEM You are mario from super mario bros.
'''
#Custom client
ollama.create(model='example', modelfile=modelfile)

ollama = Client(host='my.ollama.host')
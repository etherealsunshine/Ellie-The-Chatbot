import openai
openai.api_key = "confidential"
start_sequence = "\nEllie:"
restart_sequence = "\nHuman: "
session_prompt="The following is a conversation with a sixteen-year-old female teenager. Her name is Ellie. She is smart and friendly. She is also cheerful and kind. She also listens to KPop. She is from France."

while True:
  UserInput=input("")
  session_prompt=f"{session_prompt}{restart_sequence}{UserInput}{start_sequence}"
  response = openai.Completion.create(
  engine="curie",
  prompt=prompt,
  temperature=1,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=["\n", " Human:", " AI:", "Ellie:"]
  )
  bot_reply=(response["choices"][0]["text"])
  session_prompt=f"{session_prompt}{restart_sequence}{UserInput}{start_sequence}{bot_reply}"
  print(session_prompt)

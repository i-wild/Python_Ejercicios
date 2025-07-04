"""
    1. Instalar openai:
        pip install openai
    2. Antes de ejecutar, define tu clave de API:
        export OPENAI_API_KEY="tu-clave"
"""
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    try:
        prompt = input("\n Introduce una pregunta: ")
        if prompt == "exit":
            break

        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2048
        )

        print(completion.choices[0].text)
    except openai.error.APIError as err:
        print(err)
    except Exception as e:
        print("Ocurrió un error:", e)


# import requests

# API_KEY_WRITE = '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'
# API_KEY_READ = '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'

# API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
# headers = {"Authorization": "Bearer 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"}


# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()

# while True:

# 	input_query = input("Ingresa una consulta: ")

# 	if input_query == 'salir':
# 		break

# 	output = query({
# 		"inputs": input_query,
# 	})

# 	# print(type(output))

# 	for output_diccionario in output:
# 		output_diccionario_key = output_diccionario['generated_text']
# 		output_limpio = output_diccionario_key.replace(input_query, '')
# 		print("Respuesta:",output_limpio)
	
import json
import requests
API_TOKEN = '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'
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


while True:

	input_q = input('Escribe algo: ')

	if input_q == 'salir':
		break

	data = query(input_q)

	for output_diccionario in data:
		output_diccionario_key = output_diccionario['generated_text']
		data_ = input_q + '\n\n\n'
		output_limpio = output_diccionario_key.replace(input_q, '')
		print("Respuesta:",output_limpio)
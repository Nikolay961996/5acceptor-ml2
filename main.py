import http.client
import json
import pprint
import sys

import requests


def main():
    # conn = http.client.HTTPConnection("http://84.201.152.196:8020")

    in_file = "Program.cs"
    with open(in_file, 'r', encoding='utf-8') as code_snippet:
        code_snippet_content = code_snippet.read()
        payload = {
            'model': 'mistral-nemo-instruct-2407',
            'messages': [
                {
                'role': 'system',
                'content':
                    'Отвечаешь на русском.'
                    'Тебе присылают файлы для код ревью.'
                    ' Ты проверяешь код на потенциальные ошибки.'
                    ' После этого выдаешь их перечень и по возможности предлагаешь их исправление.'
                    'Не нужно предоставлять итоговый код .'
                },
                {
                    'role': 'system',
                    'content':
                        'При генерации ревью учитывай следующие ошибки:'
                        'Nuget пакеты, по возможности, должны быть обновлены до последних версий и'
                        ' не иметь уязвимостей;'
                        'если транзитивный Nuget пакет имеет уязвимость, значит он должен быть включен в проект'
                        'и обновлен до актуальной версии;'
                        'проект не должен иметь лишних зависимостей или зависимостей, ссылающихся на'
                        'локальные файлы (для таких зависимостей прописан абсолютный путь);'
                        'в коде не должно быть неразрешенных TODO'
                        'не должно быть закомментированного или неиспользуемого кода;'
                        'код с атрибутом Obsolete , по возможности, должен быть удален;'
                        'обязательное наличие комментариев для моделей, сущностей и т.д.;'
                        'стоит обращать внимание на неиспользуемые переменные или'
                        ' неиспользуемый возврат из методов'
                },
                {
                    'role': 'user',
                    'content': 'Отревьюй код.\r\n' + code_snippet_content
                },
            ],
            'max_tokens': 1024,
            'temperature': 0.3
        }

        payload_dumped = json.dumps(payload)

        headers = {
            'Content-type': 'application/json',
            'Authorization': '8ZrRwz0pEI59XMUrPyM82EiHc3HgHPT2'
        }

        # Send a GET request
        # conn.request("POST", "/v1/completions", payload_dumped, headers=headers)
        response = requests.post('http://84.201.152.196:8020/v1/completions', payload_dumped, headers=headers).json()

        if response and response.get('error', None) is not None:
            print(response, file=sys.stderr)
        elif response.get('response_id', None) is not None:
            answer = response.get('choices')[0].get('message').get('content')

            with open("answer.txt", 'w+', encoding='utf-8') as out_file:
                out_file.write(answer)

        # Get the response
        # response = conn.getresponse()
        # data = response.read()
        #
        # # Print the response status and data
        # print("Status:", response.status)
        # print("Response Data:", data.decode())

    # Close the connection
    # conn.close()


if __name__ == '__main__':
    main()
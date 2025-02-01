import ollama


def query_llama(prompt: str) -> str:
    messages = [
        {"role": "system",
         "content": "Ти — корисний чат-бот для підтримки психічного здоров'я."},
        {"role": "user", "content": prompt}
    ]
    response = ollama.chat(model="llama2", messages=messages)
    return response["message"]["content"]


def main():
    print("Чат-бот для підтримки психічного здоров'я")
    print("Введіть 'exit' для виходу.")

    while True:
        user_input = input("Ви: ")
        if user_input.lower() == "exit":
            print("Бот: До побачення! Бережіть себе.")
            break

        response = query_llama(user_input)
        print(f"Бот: {response}")


if __name__ == "__main__":
    main()



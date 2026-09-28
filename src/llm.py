import ollama


def generate_answer(question):
    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": f"""
                    Answer the question directly and concisely.
                    Do not add unnecessary explications, examples, or introductions.
                    Use no more then 1-2 short sentences.
                    Question:{question}
                """
            }
        ]
    )

    return response["message"]["content"]
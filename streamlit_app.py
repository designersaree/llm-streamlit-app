from llm_helper import get_llm_response

def main():
    print("=== LLM Project ===")
    while True:
        prompt = input("Enter your prompt (or 'exit' to quit): ")
        if prompt.lower() == "exit":
            break
        response = get_llm_response(prompt)
        print("LLM Response:\n", response)
        print("-" * 50)

if __name__ == "__main__":
    main()

import re


class SecureChatbot:
    def __init__(self):
        self.security_knowledge = {
            'phishing': 'Never click links in unsolicited emails. Check URLs carefully!',
            'malware': 'Keep systems updated and don\'t execute unknown files.',
            'password': 'Use strong, unique passwords and enable 2FA where possible.',
            'encryption': 'Encrypt sensitive data both in transit and at rest.'
        }

    def sanitize_input(self, user_input):
        """Prevents basic injection attempts"""
        try:
            return re.sub(r'[;\\\'"<>|=]', '', user_input.strip())
        except Exception as e:
            print(f"Input error: {e}")
            return ""

    def get_response(self, query):
        clean_query = self.sanitize_input(query.lower())

        if not clean_query:
            return "Please enter valid text"

        # Check security questions
        for term in self.security_knowledge:
            if term in clean_query:
                return f"🔒 {term.upper()}: {self.security_knowledge[term]}"

        # General responses
        response_map = {
            'hi|hello|hey': 'Hello! Ask me about: ' + ', '.join(self.security_knowledge.keys()),
            'bye|exit|quit': 'Stay secure! Goodbye!',
            'help': 'Ask about: ' + ', '.join(self.security_knowledge.keys())
        }

        for pattern, response in response_map.items():
            if re.search(pattern, clean_query):
                return response

        return "I'm a security bot. Try asking about: " + ', '.join(self.security_knowledge.keys())


def main():
    bot = SecureChatbot()
    print("""Security Chatbot (type 'bye' to exit)
I know about: """ + ', '.join(bot.security_knowledge.keys()))

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ('bye', 'exit', 'quit'):
                print("Bot: Stay secure! Goodbye!")
                break

            response = bot.get_response(user_input)
            print(f"Bot: {response}")

        except KeyboardInterrupt:
            print("\nBot: Security session ended abruptly!")
            break
        except Exception as e:
            print(f"Bot: Error occurred - {e}")


if __name__ == "__main__":
    main()

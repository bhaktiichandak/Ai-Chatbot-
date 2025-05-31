import re
import random
from difflib import SequenceMatcher


class DentalClinicChatbot:
    def __init__(self):
        self.clinic_name = "Bright Smile Dental Clinic"
        self.phone = "+91-9876543210"
        self.location = "ABC Complex, MG Road, Nagpur"
        self.hours = "9:00 AM to 6:00 PM, Monday to Saturday"

        # Enhanced responses with variations
        self.responses = {
            "greeting": [
                f"Hello! 😊 Welcome to {self.clinic_name}. I'm here to help you with any questions you might have.",
                f"Hi there! 👋 Thanks for reaching out to {self.clinic_name}. What can I assist you with today?",
                f"Welcome to {self.clinic_name}! 🦷 How may I help you today?"
            ],

            "hours": [
                f"We're open {self.hours}. We're closed on Sundays to give our team some rest! 😊",
                f"Our clinic hours are {self.hours}. Feel free to visit us during these times!",
                f"You can find us open {self.hours}. Sunday is our day off! 🌻"
            ],

            "location": [
                f"You can find us at {self.location}. We're easy to spot with our bright smile logo! 😄",
                f"We're located at {self.location}. There's convenient parking available too!",
                f"Our clinic is at {self.location}. Look for the blue signboard - you can't miss us! 🏥"
            ],

            "appointment": [
                f"I'd be happy to help you book an appointment! Please call us at {self.phone} and our friendly staff will find the perfect time for you. 📞",
                f"To schedule your visit, just give us a call at {self.phone}. We'll work around your schedule! ⏰",
                f"Booking is easy! Call {self.phone} and we'll set you up with an appointment that works best for you. 😊"
            ],

            "walkins": [
                "We do welcome walk-ins! However, I'd recommend calling ahead if possible - it helps us serve you better and reduces your waiting time. 😊",
                "Yes, walk-ins are welcome! Though booking ahead ensures you won't have to wait long. Your time is valuable to us! ⏰",
                "Absolutely! We accept walk-ins, but appointments get priority. Give us a quick call if you can! 📞"
            ],

            "services": [
                "We offer comprehensive dental care including general dentistry, orthodontics (braces & aligners), cosmetic procedures, and preventive care. What specific treatment are you interested in? 🦷✨",
                "Our services include routine cleanings, fillings, root canals, crowns, braces, teeth whitening, and much more! Is there a particular service you'd like to know about? 😊",
                "We provide everything from basic checkups to advanced treatments like implants and cosmetic dentistry. What brings you in? 🏥"
            ],

            "orthodontics": [
                "Yes! We offer full orthodontic treatment including traditional braces, clear aligners, and retainers. Our orthodontist Dr. Smith has over 10 years of experience creating beautiful smiles! 😁✨",
                "Absolutely! We specialize in braces and clear aligners. We'll help you achieve that perfect smile you've always wanted! 🦷💫",
                "We do! Our orthodontic treatments include metal braces, ceramic braces, and Invisalign. We'll find the best option for your lifestyle! 😊"
            ],

            "pain": [
                "I'm sorry you're experiencing pain! 😟 Dental pain can be really uncomfortable. Please call us immediately at {self.phone} - we always make room for dental emergencies!",
                "Oh no! Tooth pain is never fun. 😣 Please call {self.phone} right away. We can often see emergency cases the same day!",
                "That sounds painful! 😰 Don't suffer - call us at {self.phone} and we'll get you seen as soon as possible. Emergency cases are our priority!"
            ],

            "cost": [
                "Costs vary depending on the treatment needed. We offer competitive pricing and accept most insurance plans! For specific pricing, please call {self.phone} - we're happy to discuss payment options too! 💳",
                "We believe quality dental care should be accessible! Prices depend on your specific needs. Call {self.phone} for a personalized quote and to learn about our payment plans! 😊",
                "Treatment costs vary, but we work with you to make care affordable. We accept insurance and offer flexible payment options. Call {self.phone} to discuss! 💰"
            ],

            "goodbye": [
                "Thank you for contacting Bright Smile Dental Clinic! Take care and remember to keep smiling! 😊🦷✨",
                "It was great chatting with you! Don't forget to brush and floss, and we hope to see you soon! 👋😄",
                "Thanks for reaching out! Have a wonderful day and keep that smile bright! 🌟😊"
            ],

            "default": [
                "I'd love to help you with that! For detailed information, please call us at {self.phone} - our knowledgeable staff can give you the complete answer you need! 😊",
                "That's a great question! While I can help with basic info, our team at {self.phone} can provide you with detailed, personalized assistance! 📞",
                "I want to make sure you get the most accurate information! Please give us a call at {self.phone} and we'll be happy to help! 🏥"
            ]
        }

        # Keywords for intent recognition
        self.intent_keywords = {
            "hours": ["hours", "time", "open", "close", "when", "timing", "schedule"],
            "location": ["where", "address", "location", "directions", "find", "situated"],
            "appointment": ["appointment", "book", "schedule", "reserve", "slot", "booking"],
            "walkins": ["walk-in", "walkin", "walk in", "without appointment", "emergency visit"],
            "services": ["services", "treatment", "what do you do", "procedures", "offer"],
            "orthodontics": ["braces", "orthodontic", "alignment", "straighten", "crooked teeth", "invisalign",
                             "aligner"],
            "pain": ["pain", "hurt", "ache", "emergency", "urgent", "tooth pain", "toothache"],
            "cost": ["cost", "price", "expensive", "cheap", "insurance", "payment", "fee", "charges"],
            "goodbye": ["bye", "goodbye", "thanks", "thank you", "see you", "take care"]
        }

    def similarity(self, a, b):
        """Calculate similarity between two strings"""
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()

    def detect_intent(self, user_input):
        """Detect user intent based on keywords and similarity"""
        user_input = user_input.lower()

        # Check for exact keyword matches first
        for intent, keywords in self.intent_keywords.items():
            for keyword in keywords:
                if keyword in user_input:
                    return intent

        # If no exact match, return default
        return "default"

    def get_response(self, user_input):
        """Generate appropriate response based on user input"""
        if not user_input.strip():
            return "I'm here to help! What would you like to know about our dental services? 😊"

        intent = self.detect_intent(user_input)

        # Format response with clinic details if needed
        response_list = self.responses.get(intent, self.responses["default"])
        response = random.choice(response_list)

        # Replace placeholders in responses
        response = response.format(
            phone=self.phone,
            location=self.location,
            hours=self.hours,
            clinic_name=self.clinic_name
        )

        return response

    def greet_user(self):
        """Display welcome message"""
        greeting = random.choice(self.responses["greeting"])
        print(f"\n🤖 {greeting}")
        print("💡 You can ask me about our hours, location, services, appointments, or anything else!")
        print("(Type 'bye' to exit)\n")

    def run(self):
        """Main chatbot loop"""
        self.greet_user()

        while True:
            try:
                user_input = input("You: ").strip()

                if not user_input:
                    continue

                # Check for goodbye intent
                if self.detect_intent(user_input) == "goodbye" or user_input.lower() in ['exit', 'quit']:
                    goodbye_msg = random.choice(self.responses["goodbye"])
                    print(f"🤖 {goodbye_msg}")
                    break

                # Get and display response
                response = self.get_response(user_input)
                print(f"🤖 {response}\n")

            except KeyboardInterrupt:
                print(f"\n🤖 {random.choice(self.responses['goodbye'])}")
                break
            except Exception as e:
                print("🤖 I'm having a small technical hiccup! Please try again or call us directly. 😊")


def main():
    """Initialize and run the chatbot"""
    print("=" * 60)
    print("🦷 BRIGHT SMILE DENTAL CLINIC CHATBOT 🦷")
    print("=" * 60)

    chatbot = DentalClinicChatbot()
    chatbot.run()


if __name__ == "__main__":
    main()
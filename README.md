# Dental Clinic Chatbot

A simple chatbot for dental clinics to answer common patient questions.

## What it does

This chatbot can answer basic questions about:
- Clinic hours and location
- Booking appointments  
- Services offered
- Walk-in policies
- Emergency cases

## How to run

Just run the Python file:
```bash
python chatbot.py
```

That's it! No installation needed.

## Example chat

```
You: What are your hours?
Bot: We're open 9:00 AM to 6:00 PM, Monday to Saturday.

You: Where are you located?  
Bot: We're located at ABC Complex, MG Road, Nagpur.

You: bye
Bot: Thank you for visiting Bright Smile Dental Clinic!
```

## Customize for your clinic

Edit these lines in the code:
```python
self.clinic_name = "Your Clinic Name"
self.phone = "+91-1234567890" 
self.location = "Your Address"
self.hours = "Your Hours"
```

## Requirements

- Python 3.6 or newer
- That's it

## Note

This is a basic rule-based chatbot. For more complex needs, you might want to look into AI-powered solutions.

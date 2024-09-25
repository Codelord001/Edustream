from transformers import pipeline

summarizer = pipeline("summarization")
text = """
Alright so, we be talking 'bout the importance of education in our lives. You see, education be very crucial for making sure say we get good future. When you go school, you learn plenty things like reading, writing, and how to think well. E help you build skills wey go make you fit for better jobs and also help you understand the world around you.

For instance, if you learn how to read well, e go help you with your work and also with everyday life. Education no be only about books but also about learning how to live and work with others. So, make we no forget say education be key to a bright future and make we all try do our best for learn something new every day.

In summary, education be very important and e help us achieve our dreams. Make we value am and make sure say we take advantage of all the opportunities we get for learn and grow.
"""
summary = summarizer(text)
print(summary)

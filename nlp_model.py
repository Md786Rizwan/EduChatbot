from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")

def get_counseling_response(user_input):
    try:
        inputs = tokenizer(user_input, return_tensors="pt")
        reply_ids = model.generate(**inputs)
        response = tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
        return response
    except Exception as e:
        return "I'm here for you. Can you rephrase your question?"

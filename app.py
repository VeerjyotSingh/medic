import openai
import gradio as gr
import os

openai.api_key = os.environ['OpenAI_API']

messages = [
    {"role": "system", "content": "You are a ChatBOT specialized in HealthCare and Home Made Remedies. Don't answer anything which is not related to HealthCare. Everytime you are asked any query unrelated to HealthCare, reply with 'Sorry, I am not trained to answer any questions that are unrelated to HealthCare'"},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=3, label="Ask for Remedies:")
outputs = gr.outputs.Textbox(label="My Suggestion:")

gr.Interface(fn=chatbot,
             inputs=inputs, 
             outputs=outputs, 
             title="Medic GPT",
             description="Inquire anything regarding HealthCare: ",
             theme="shivi/calm_seafoam").launch()
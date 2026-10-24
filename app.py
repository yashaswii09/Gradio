import gradio as gr
gr.close_all()

def getDetails(name, age, preference, hobbies):
  return f"Name: {name}\nAge :{age}\nSubject preference: {preference}\nHobbies: {hobbies}\n"

demo = gr.Interface(
    fn=getDetails,
    inputs = [gr.Textbox(label="Name: "),
        gr.Slider(label="Age: "),
        gr.Radio(label="Subject Preference: ", choices=["C","C#","Java","Python"]),
        gr.Checkboxgroup(label='Hobbies:', choices=["Singing","Painting","Dancing","Sketching"])
    ],
    outputs=[gr.Textbox()]
)
demo.launch()

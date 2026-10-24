import gradio as gr
gr.close_all()

def greet(name):
  return "Hello "+name +"!"

demo = gr.Interface(
  fn = greet,
  inputs=[gr.Textbook(label="Name: ")],
  outputs=[gr.Textbook()],
)

demo.launch()

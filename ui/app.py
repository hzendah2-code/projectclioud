import gradio as gr

def hello(name):
    return f"أهلًا يا {name} 👋 — واجهة مشروع الكلاود شغالة!"

with gr.Blocks(title="Project Cloud UI") as demo:
    gr.Markdown("# Project Cloud UI")
    name = gr.Textbox(label="اسمك")
    out = gr.Textbox(label="النتيجة")
    btn = gr.Button("جرّب")

    btn.click(fn=hello, inputs=name, outputs=out)

demo.launch(server_name="0.0.0.0", server_port=7860)

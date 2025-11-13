from build_adaptive_ai_tutor import get_ai_tutor_stream
import gradio as gr


ai_tutor_interface = gr.Interface(
    fn=get_ai_tutor_stream,
    inputs=gr.Textbox(
        lines=5, placeholder="Ask the AI Tutor Anything...", label="Your Question"
    ),
    outputs=gr.Textbox(label="AI Tutor's Answer"),
    title="AI Tutor",
    description="Enter your question below and the AI Tutor will provide explanation.",
    allow_flagging="never",
)

print("Launching Gradio Interface...")
ai_tutor_interface.queue().launch()
import os
import sys
import traceback
import subprocess

import gradio as gr

from generator import generate_game

# Generate Button

def generate(game_idea):

    try:

        result = generate_game(game_idea)

        game_review = result.get("game_review", "")
        python_code = result.get("python_code", "")
        requirements = result.get("requirements", "")
        file_path = result.get("file_path")
        full_output = result.get("full_output", "")

        status = "✅ Game Generated Successfully"

        return (
            game_review,
            full_output,
            python_code,
            requirements,
            file_path,
            status
        )

    except Exception as e:

        traceback.print_exc()

        return (
            "",
            "",
            "",
            "",
            None,
            f"❌ {str(e)}"
        )

# Run Button

def run_game(file_path):

    if not file_path:
        return "❌ No generated Python file found."

    if not os.path.exists(file_path):
        return "❌ File does not exist."

    # Use the same Python interpreter running Gradio
    subprocess.Popen([sys.executable, file_path])

    return "✅ Game Started"

# UI

css = """
.gradio-container{
    background:#0f172a !important;
}

footer{
    display:none !important;
}

.main-header{
    background:linear-gradient(135deg,#2563eb,#1d4ed8);
    padding:25px;
    border-radius:15px;
    color:white;
    text-align:center;
    margin-bottom:15px;
}

.section{
    background:#1e293b;
    border-radius:12px;
    padding:12px;
}

button{
    border-radius:10px !important;
    font-weight:bold !important;
}

button:hover{
    transform:translateY(-2px);
    transition:0.2s;
}
"""

with gr.Blocks(
    title="AI Game Generator",
    css=css,
    theme=gr.themes.Soft(primary_hue="blue")
) as demo:

    gr.HTML("""
    <div class="main-header">
        <h1>🎮 AI Game Generator</h1>
        <p>Multi-Agent Game Generation using CrewAI + OpenRouter + Pygame</p>
    </div>
    """)

    with gr.Row():

        with gr.Column(scale=3):

            game_input = gr.Textbox(
                label="📝 Game Idea",
                placeholder="Example: Create a Snake game with powerups and enemies",
                lines=4
            )

            generate_btn = gr.Button(
                "🚀 Generate Game",
                variant="primary"
            )

        with gr.Column(scale=1):

            status_box = gr.Textbox(
                label="⚡ Status",
                interactive=False
            )

            run_btn = gr.Button(
                "▶ Run Game"
            )

            run_status = gr.Textbox(
                label="Run Status",
                interactive=False
            )

    gr.Markdown("---")

    code_box = gr.Code(
        label="📜 Generated Python Code",
        language="python",
        lines=22
    )

    gr.Markdown("---")

    with gr.Row():

        review_box = gr.Textbox(
            label="📋 Game Review",
            lines=8
        )

        requirement_box = gr.Textbox(
            label="📦 Requirements",
            lines=8
        )

    gr.Markdown("---")

    download_file = gr.File(
        label="📥 Download Generated Game",
        interactive=False
    )

    with gr.Accordion(
        "🔍 View Complete Crew Output",
        open=False
    ):

        output_box = gr.Textbox(
            label="",
            lines=18
        )

    generate_btn.click(
        fn=generate,
        inputs=game_input,
        outputs=[
            review_box,
            output_box,
            code_box,
            requirement_box,
            download_file,
            status_box
        ]
    )

    run_btn.click(
        fn=run_game,
        inputs=download_file,
        outputs=run_status
    )

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )

import openai
import gradio as gr

openai.api_key = "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"


def openai_answer1(question):
    prompt = f"  Act as a grader for a medical student's History and Physical assignment based on a rubric. \
    The rubric is as follows:  Data Gathering: 0-30 points \
    Evaluate the medical student's according to Data Gathering \nAssignment: {question}\Evaluate and Grade:"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=1000,
    )
    answer = response.choices[0].text.strip()
    return answer


def openai_answer2(question):
    prompt = f"  Act as a grader for a medical student's History and Physical assignment based on a rubric. \
    The rubric is as follows: Medical Reasoning: 0-60 points \
    Evaluate the medical student's according to Medical Reasoning \nAssignment: {question}\Evaluate and Grade:"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=1000,
    )
    answer = response.choices[0].text.strip()
    return answer


def openai_answer3(question):
    prompt = f"  Act as a grader for a medical student's History and Physical assignment based on a rubric. \
    The rubric is as follows: Diagnostic and Therapeutic Plan: 0-10 points \
    Evaluate the medical student's assignment according to Diagnostic and Therapeutic Plan \nAssignment: {question}\Evaluate and Grade:"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=1000,
    )
    answer = response.choices[0].text.strip()
    return answer


def openai_answer4(question):
    prompt = f"  Act as a grader for a medical student's History and Physical assignment based on a rubric. \
    The rubric is as follows: Overall assessment 0-100 points \
    Evaluate overall the medical student's assignment \nAssignment: {question}\Evaluate and Grade:"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=1000,
    )
    answer = response.choices[0].text.strip()
    return answer


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            gr.HTML(
                """
                <div  </div>
                <h1 style="text-align: center;">Medical Student H&P Assignment Grader Based on a Rubric</h1> 
                <h2 style="text-align: center;">(Experimental)</h2>   
                """
            )
            openaai_api_key = gr.Textbox(
                lines=1,
                label="OpenAI API Key",
                placeholder="Enter your OpenAI API Key here",
                interactive=True,
            )
        gr.Image("ucf_logo.jpg", label="University of Central Florida", height=200)

    radio = gr.Radio(["ChatGPT"], label="LLM model")
    slider = gr.Slider(minimum=0.0, maximum=1.0, step=0.1, label="Temperature")

    with gr.Tab("Copy and Paste"):
        name = gr.Textbox(
            lines=10,
            label="Input",
            placeholder="Copy and paste student's assignment here",
            interactive=True,
        )
        button = gr.Button("Grade")

        output1 = gr.Textbox(lines=3, label="Grade for Data Gathering")
        output2 = gr.Textbox(lines=3, label="Grade for Medical Reasoning")
        output3 = gr.Textbox(lines=3, label="Grade for Diagnostic and Therapeutic Plan")
        output4 = gr.Textbox(lines=3, label="TOTAL GRADE")
        button.click(fn=openai_answer1, inputs=name, outputs=output1)
        button.click(fn=openai_answer2, inputs=name, outputs=output2)
        button.click(fn=openai_answer3, inputs=name, outputs=output3)
        button.click(fn=openai_answer4, inputs=name, outputs=output4)

    with gr.Tab("Upload a File"):
        file_upload = gr.File(label="Upload a file", type="file")
        file_button = gr.Button("Grade")
        file_output1 = gr.Textbox(lines=3, label="Grade for Data Gathering")
        file_output2 = gr.Textbox(lines=3, label="Grade for Medical Reasoning")
        file_output3 = gr.Textbox(
            lines=3, label="Grade for Diagnostic and Therapeutic Plan"
        )
        file_output4 = gr.Textbox(lines=3, label="TOTAL GRADE")
        file_button.click(fn=openai_answer1, inputs=name, outputs=output1)
        file_button.click(fn=openai_answer2, inputs=name, outputs=output2)
        file_button.click(fn=openai_answer3, inputs=name, outputs=output3)
        file_button.click(fn=openai_answer4, inputs=name, outputs=output4)


""" demo = gr.Interface(openai_answer, 
        

    ["textbox"], 
    "textbox",
    title="OpenAI Answers",
    description="Ask a question and get an answer from OpenAI's GPT-3 model. See more at",
    article="https://beta.openai.com/",
    examples=[
        ["How many pounds are in a kilogram?"],
        ["Who was the first president of the United States?"]
    ]) """


if __name__ == "__main__":
    demo.launch(share=True)

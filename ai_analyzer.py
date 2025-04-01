import google.generativeai as genai

genai.configure(api_key="")  # Replace with your Gemini API key
model = genai.GenerativeModel("gemini-1.5-pro")

def analyze_files(repo_data, mode, dir_structure):
    prompt_base = "Analyze this repository structure and code:\nStructure: {}\nFiles: {}"
    
    if mode == "summary":
        prompt = prompt_base.format(dir_structure, repo_data) + (
            "\n\nPlease provide a high-level summary for each file in the repository. "
            "For each file, identify its main purpose, key functionalities, and how it interacts with other parts of the project. "
            "Additionally, suggest a logical reading order or flow that would guide a developer through the repository in an efficient manner."
        )
    else:  # detailed
        prompt = prompt_base.format(dir_structure, repo_data) + (
            "\n\nPlease perform a detailed analysis for each file in the repository. "
            "Break down the code into sections or functions, explain the underlying logic of each major block, and describe how each part contributes to the overall functionality of the project. "
            "Also, provide an explicit flow or sequence that outlines the order of execution and interactions between different parts of the code, to help a reader understand the program's structure step-by-step."
        )

    
    response = model.generate_content(prompt)
    return response.text
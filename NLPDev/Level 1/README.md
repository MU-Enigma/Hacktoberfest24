

# Level 1 - Installing and Running a Chat Interface with an LLM

## Task Overview

In this task, you will install and run a **pre-built chat interface** powered by an **open-source Large Language Model (LLM)**. Open-source models like **LLaMA** provide powerful, flexible options for conversational AI. You will use readily available interfaces such as **Ollama** or **Oogabooga** to interact with these models. Your task is to successfully install, run the interface, interact with the LLM, and capture screenshots of the conversation.

### Objective

- Install a pre-built interface like **Ollama** or **Oogabooga** that enables interaction with open-source LLMs like **LLaMA** or **GPT-Neo**.
- Run the interface, converse with the LLM, and document the installation and execution steps.
- Capture screenshots of the interaction and submit them along with a brief report on the process.


### Steps to Contribute

1. **Fork the Repo**

   - Fork the repository to your own GitHub account.

2. **Clone the Repo**

   - Clone the forked repository to your local environment:

   ```bash
   git clone https://github.com/<your_username>/Hacktoberfest_2024
   ```

3. **Navigate to the Correct Directory**

   - Navigate to the Level 1 directory where you will submit your task:

   ```bash
   cd Hacktoberfest24/NLPDev/Level 1/
   ```

4. **Create a Folder with Your Username**

   - Create a new folder named after your GitHub username:

   ```bash
   mkdir <your_username>
   ```

5. **Install a Pre-Built Chat Interface (e.g., Ollama or Oogabooga)**

   - Choose a pre-built interface that supports open-source models. Some popular options are:
     - **[Ollama](https://ollama.com/)**: A user-friendly interface for running LLaMA and similar models locally on your machine.
     - **[Oogabooga](https://github.com/oobabooga/text-generation-webui)**: An advanced web interface for various open-source models, including LLaMA, GPT-Neo, and BLOOM.


6. **Download and Use an Open-Source Model**

   - You can choose from a variety of **open-source models** :
     - **LLaMA**: [Meta’s LLaMA](https://huggingface.co/Meta) is available via Hugging Face.
     - **GPT-Neo**: Available from [EleutherAI](https://huggingface.co/EleutherAI/gpt-neo-1.3B).
     - **BLOOM**: An open-source multilingual model available from [BigScience](https://huggingface.co/bigscience/bloom).


7. **Run and Interact with the LLM**

   - Interact with the model by asking it questions or giving it prompts.
   - Test different inputs and observe the LLM’s responses.

8. **Capture the Conversation**

   - Take **screenshots** of your conversation with the LLM, showing both the interface and the model’s responses.

9. **Document the Process**

   - In a `README.md` or `.txt` file, document:
     - **Installation Steps**: Detail the steps you followed to install the interface and model.
     - **Running the Interface**: Describe how you launched the chat interface and interacted with the LLM.
     - **Challenges (if any)**: Note any issues you encountered during installation or interaction and how you resolved them.

10. **Submit Screenshots and Documentation**

   - Add the screenshots of the conversation and the documentation to your folder.

   Example:

   ```bash
   cp <your_screenshots>.png <your_username>/
   cp README.md <your_username>/
   ```

11. **Add and Commit Your Changes**

    - Stage your changes:

    ```bash
    git add .
    ```

    - Commit your changes with a descriptive message:

    ```bash
    git commit -m "Added Level 1 task with Ollama/Oogabooga by <your_username>"
    ```

12. **Push Your Changes and Open a Pull Request**

    - Push your changes to your forked repository:

    ```bash
    git push origin main
    ```

    - Open a Pull Request to submit your work for review.

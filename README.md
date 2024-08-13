# AI Assistant Chatbot with Quantum Computing

## Overview

This project integrates a GPT-3.5-based chatbot with quantum computing capabilities. Utilizing OpenAI’s GPT-3.5-turbo for generating responses and IBM's quantum backend for quantum computations, this project combines natural language processing with cutting-edge quantum technology.

## Features

- **GPT-3.5 Chatbot**: Leverages OpenAI's GPT-3.5-turbo to generate intelligent responses.
- **Quantum Computation**: Executes a quantum circuit on IBM's quantum hardware and returns quantum state probabilities.
- **Gradio Interface**: Provides a user-friendly web interface for interacting with the chatbot.

## Prerequisites

- **Python 3.6 or later**
- **IBM Quantum Experience account** with an API token

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/quantum-chatbot.git
   cd quantum-chatbot

2. **Set up a virtual environment (recommended):**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   
3. **Install the required Python packages:**

   Create a `requirements.txt` file with the following content:

   ```plaintext
   gradio
   qiskit
   qiskit_ibm_runtime
   g4f

4. **Configuration**

   **Update IBM Quantum API Token:**

   Replace the placeholder token in `app.py` with your actual IBM Quantum API token:

   ```python
   token="YOUR_IBMQ_TOKEN_HERE"
   
5. **Usage**

   **Run the application:**

   Start the Gradio interface by executing:

   ```bash
   python app.py

**User Input:**

```plaintext
What is the current state of quantum computation?
[GPT-3.5 response to the user query]
Quantum Result: [Quantum computation result]




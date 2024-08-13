from g4f.client import Client
import gradio as gr
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, Session, SamplerV2

# Initialize the GPT-3.5 client
client = Client()

# Initialize Qiskit Runtime Service with the specified backend
service = QiskitRuntimeService(channel="ibm_quantum",
                               token="77d5948bfc0a936528d399ba93caa33f6e722041f90e56354707d62b80adbe887289a4c9fccbe517fda98a506acb987c35ca24ceabbe1bb809d3097a5f8aa9ca")
backend = service.backend(name="ibm_brisbane")

def quantum_computation():
    # Example quantum circuit
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)  # Apply Hadamard gate
    circuit.cx(0, 1)  # Apply CNOT gate
    circuit.measure([0, 1], [0, 1])  # Measure the qubits

    # Transpile the circuit for the selected backend
    transpiled_circuit = transpile(circuit, backend=backend)

    # Use Qiskit Runtime to run the circuit on the specified backend
    with Session(backend=backend) as session:
        sampler = SamplerV2(session=session)
        job = sampler.run(transpiled_circuit)
        result = job.result()
        probabilities = result.quasi_dists[0]

    return probabilities

def chatbot_response(user_input):
    # Generate response using GPT-3.5-turbo
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
    )
    
    # Perform quantum computation
    quantum_result = quantum_computation()
    
    # Combine GPT response with quantum result
    return f"{response.choices[0].message.content}\n\nQuantum Result: {quantum_result}"

# Create Gradio interface
interface = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Type your question here..."),
    outputs="text",
    title="AI Assistant Chatbot with Quantum Computing",
    description="Ask any question and the AI assistant will respond, enhanced by quantum computation."
)

if __name__ == "__main__":
    interface.launch()


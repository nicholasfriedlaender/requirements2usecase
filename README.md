# Welcome to Req2UseCase!

This repository supports the study:  
***Leveraging Large Language Models for Use Case Model Generation from Software Requirements***.

It contains the implementation of the proposed method and the results from the experiment with software engineers.

## Repository Structure

### 📦 Application ([app](app))

-   **Frontend** – User interface for interacting with the system.
-   **[`serverGPU.py`](app/serverGPU.py)** – Python script running on the GPU server.
-   **[`proxyFile.py`](app/proxyFile.py)** – Proxy logic layer that handles communication between the frontend and the GPU server.

### 📊 Models ([models](models))

Contains the models from the study, both the [ground truth](models/ground-truth) and the [models created by the participants](models/results). The ground truth is the reference that the participants' models were compared against. The models created by the participants are each described with an UML use case diagram (plantuml and png) and a markdown detailing each use case. In the manual approach, not all use cases were modeled in detail; thus, only some of the use cases are described. For the details, please read the full study.

### 🧾 Prompts

-   **[`prompts.txt`](Prompts.txt)** – Contains all prompts designed and used in the study.

### 📑 Requirements Texts

-   **[`requirements-a.md`](requirements-a.md)** – Requirements Text A.
-   **[`requirements-b.md`](requirements-b.md)** – Requirements Text B.

## Development

### Prerequisites

Ensure you have the following prerequisites before starting development:

-   Python (Version 3.8 or higher)
-   Access to a GPU server with Ollama and Llama3.1:70b installed

### Installation

1.  Clone the repository:
    
    ```shell
    git clone https://github.com/nicholasfriedlaender/req2usecase.git
    cd req2usecase
    ```
    
2.  Install the required dependencies:
    
    ```shell
    npm install
    ```
    

### Running the Development Server

To start the development server, run the following command:

```shell
npm run dev
```
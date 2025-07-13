# Welcome to Req2UseCase!

This project is part of the study ***Leveraging Large Language Models for Use Case Model Generation from Software Requirements***. The repository contains the application used in the experiments with software engineers. It includes both the frontend and the sequence of steps and the `serverGPU.py` file, which contains the Python script running on the GPU server using Llama3.1:70b through Ollama. The `proxyFile.py` file includes the proxy logic layer used to communicate between the frontend and the GPU server. All the prompts created and utilized for this project can be found in the file `Prompts.txt`. Additionally, the Requirements A and B Text used in the Experiments can be found in `RequirementsTextA.md` and `RequirementsTextB.md`

## Development

### Prerequisites

Ensure you have the following prerequisites before starting development:
- Python (Version 3.8 or higher)
- Access to a GPU server with Ollama and Llama3.1:70b installed

### Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/nicholasfriedlaender/req2usecase.git
    cd req2usecase
    ```

2. Install the required dependencies:

    ```shell
    npm install
    ```

### Running the Development Server

To start the development server, run the following command:

```shell
npm run dev

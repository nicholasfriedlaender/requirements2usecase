# Welcome to Req2UseCase!

This project is part of the study ***Leveraging Large Language Models for Use Case Model Generation from Software Requirements***. The repository contains the proposed method evaluated in experiments with software engineers. It includes both the frontend and the sequence of steps and the [`serverGPU.py`](app/serverGPU.py) file, which contains the Python script running on the GPU server using Llama3.1:70b. The [`proxyFile.py`](app/proxyFile.py) file includes the proxy logic layer used to communicate between the frontend and the GPU server. All the prompts created and utilized for this project can be found in the file [`prompts.txt`](prompts.txt). Additionally, the Requirements Texts A and B used in the experiments can be found in [`requirements-a.md`](requirements-a.md) and [`requirements-b.md`](requirements-b.md). These results from each approch for every particaipant can be found [here](models/results/).

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

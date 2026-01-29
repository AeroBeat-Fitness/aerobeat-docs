# Hybrid Gastown Orchestration Plan

## Primary Goal

Create a hybrid local & cloud solution for running Gastown, the parallel agent orchestration model used in the AeroBeat rhythm workout platform for code generation.

## Local Hardware Overview

*   **Operating System**: Zorin OS 18 Pro

*   **Firmware Version**: 1.20.0

*   **Kernel Version**: Linux 6.14.0-37 Generic

*   **Hardware**: Alienware Aurora R13

*   **Processor**: 12th Gen Intel i7-12700KF x 20

*   **Memory**: 128GB

*   **Disk Capacity**: 3.1TB

*   **Graphics**: NVIDIA GeForce RTX 3080 - 10240MiB (10GB) VRAM

## High End Strategy

• Use Gemini 3 Pro via the Google Studio Api for high-level architectural planning and epic decomposition with the Gastown Mayor working alongside rig expert crew members to validate plans.

• Use the Mayor to sling convoys of beads (git backed json tasks) to Polecats and the Refinery agents, which run on local hardware to save on costs.

*   **Mayors**: gemini-3-pro-preview (Google Studio Api)

*   **Polecats**: Two possible *Local* choices.
*   Deepseek-Coder 6.7B : ~7-10 tps 4-bit GGUF quantization in VRAM
*   Qwen3-Coder-32B: ~12-15 tps 4-bit GGUF quantization with memory pooling
   
*   **Refineries**: One recommended *Local* choice
*   Deepseek-Coder 6.7B : ~7-10 tps 4-bit GGUF quantization in VRAM
*   DeepSeek-R1-Distill-Qwen-32B: ~7-10 tps 4-bit GGUF quantization with memory pooling

## 1. Answer Remaining Questions

- [ ] **Local Runner**: Which Ecosystem? Ollama, vLLM, llama.cpp, etc.

- [ ] **Memory Pooling**: Is it worth it for our local models vs just running a model that fits entirely on our GPU?

## 2. Infrastructure Preparation (Local)

- [x] **OS Configuration**: Optimize Zorin OS 18 Pro and ensure NVIDIA drivers for the RTX 3080 are current.

- [ ] **Backend Setup**: Install Ollama or vLLM to provide OpenAI-compatible local endpoints.

## 3. Worker Deployment (Local)

- [ ] **Install The Tools**: Download the ecosystem tools to run local models 
- [ ] **Install Models**: Download the models

- [ ] **Test Polecats**: Provide models the 'Polecat' and 'Refinery' roles, point them at our AGENTS.MD file in a rig, and give them a task written as if a mayor sent it to them and see how they perform.

- [ ] **Test Refinery**: Provide models the 'Refinery' role, point them at our AGENTS.MD file in the same rig as the Polecats, and give them a code evaluation task written as if a mayor sent it to them and see how they perform.

## 4. Integration & Parallelization

- [ ] **Gastown Config**: Update Gastown agent definitions to point to local API providers.

- [ ] **Automated Handoff**: Verify the pipeline works by creating a convoy with the mayor and slinging it to the polecats and refinery.
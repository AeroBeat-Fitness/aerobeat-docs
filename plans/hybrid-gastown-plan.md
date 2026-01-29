# Hybrid Gastown Orchestration Plan

## Primary Goal

Create a hybrid local & cloud solution for running Gastown, the parallel agent orchestration model used in the AeroBeat rhythm workout platform for code generation.

## Known Limitations And Notes

*   Today, January 29, 2026, running parallel agents on a single GPU with 10GB VRAM is limited if we intend to run our agents solely within VRAM to prevent slowdown due to use of RAM for swaps.

*   Instead of parallel ochestration, this plan utilizes *sequential* agents to perform the work. 

*   We are using the Gastown orchestration method to allow us to test this hybrid strategy vs a pure cloud solution with many parallel agents

*   Part of our planning goal is to create a cost benefit analysis and determine our workflow for 2026 in the AeroBeat project which primarily utilizes .gdscript (Godot Scripting Language).

*   Watching a YouTube video, with a few Brave browser tabs open, and Godot + Visual Studio is about ~1.65GB VRAM with GPU acceleration *On* for Brave, and about ~1.1GB VRAM with GPU acceleration *Off* for Brave.

## AeroBeat Project Agents

AeroBeat has specialized agents with unique roles compared to the standard ones included with Gastown.

*   **Mayor**: Used to break down large feature ideas into plan documents, and then convert those plans into convoys of beads.

*   **Crew**: Specialized with each rigs knowledge, used for communication with the Mayor, Polecat, Refinery, and Librarian about rig specific questions. Specialized in answering questions about a rig without hallucinating.

*   **Refinery**: Writes unit & end to end tests for a convoy of beads before the Polecats start working. Reviews results at the end of the convoy to ensure testing coverage guidelines are met.

*   **Librarian**: Writes code comments for gdscript files and Readme files for rigs.

*   **Polecat**: Worker bees that create the classes, functions, etc to pass the tests written by the refinery.

## Local Hardware Overview

*   **Operating System**: Zorin OS 18 Pro

*   **Firmware Version**: 1.20.0

*   **Kernel Version**: Linux 6.14.0-37 Generic

*   **Hardware**: Alienware Aurora R13

*   **Processor**: 12th Gen Intel i7-12700KF x 12 physical cores (8 Performance & 4 Effeciency Cores) & 20 threads

*   **Memory**: 128GB

*   **Disk Capacity**: 3.1TB

*   **Graphics**: NVIDIA GeForce RTX 3080 - 10240MiB (10GB) VRAM


## High End Strategy

• Use Gemini 3 Pro via the Google Studio Api for high-level architectural planning and epic decomposition with the Gastown Mayor working alongside rig expert crew members to validate plans.

• Use the Mayor to sling convoys of beads (git backed json tasks) to Polecats and the Refinery agents, which run on local hardware to save on costs.

• Make full used of our CPU + RAM + VRAM to run simultaneous agents while leaving enough resources to our Zorin 18 OS Pro for it to be used for work by the human engineer while the agents operate in the background.


## **Strategy**

### Local Model Requirements

*   We would prefer to run multiple polecat workers simultaneously if possible within our limited VRAM.

*   Use 4-bit Quantization for the sweet spot of performance vs resources

*   We estimate VRAM usage of about ~0.11 MiB per token for context

*   Gastown agents require ~2k tokens to recieve their role info

*   Local Rigs (repository) Readme.md file is usually about ~1k tokens


### **Mayor**: 

*Cloud* - Large Context, Deap Reasoning

*   Gemini 3 Pro Preview - Most expensive Gemini model with thinking capabilities.

### **Crew**:

*Cloud* - Small per rig context - Fits in RAM

*   Gemini 3 Flash Preview - Ingests rig documentation and provides answers without deep thinking. Can only answer specific questions about the rig. Tries to answer truthfully and avoids hallucinating anything. One agent per active rig is started alongside when a convory of beads will touch those rigs.

### **Polecats (Workers)**

*Local* - Speed + 1 Agent - Fits in VRAM.

*   Qwen3-Coder-3B: ~100 tps 4-bit (Q4_K_M) GGUF. Use 2 simultaneous agents (up to 6k tokens). ~3-4GB VRAM Usage per agent. ~6-8GB VRAM for two agents.

*   Qwen3-Coder-3B: ~100 tps 4-bit (Q4_K_M) GGUF. Use for very long context lengths (up to 32k tokens). ~6GB VRAM Usage.

*   Qwen3-Coder-7B: ~100 tps 4-bit (Q4_K_M) GGUF. Use for higher intelligence with long context lengths (14k tokens) with 1 agent at a time. ~6.5GB VRAM Usage.

*   Qwen3-Coder-30B-A3B: ~12-20 tps 4-bit (Q4_K_M) GGUF. Mixture-Of-Experts Model (MOE). Requires offloading non-active expert layers and KV cache to RAM.

*   Llama 4 8B : ~82 tps 4-bit (Q4_K_M) GGUF for context lengths under 8k tokens. Can only run one agent at a time. ~6GB VRAM for 4k tokens. ~8GB for 16k tokens.

*   Gemma-3-4B-It: ~40-50 tps 5-bit (Q4_K_M) GGUF. One agent at a time. ~6.5GB VRAM for 12k tokens.

*   DeepSeek-Coder-V3-Lite (8B): ~15-25 tps 4-bit (Q4_K_M) GGUF for context lengths under 6k tokens

### **Refineries (Reviewers)**

*Local* - Intelligence - 2 Agents - Fits In CPU + RAM

*   DeepSeek-R1-Distill-Qwen-32B: ~3-5 tps 4-bit (Q4_K_M) GGUF. Uses chain of thought reasoning for code reviews. Takes roughly 20GB of RAM. Assigned P-Cores 0-5 from CPU.

*   Qwen3-7B-Instruct: ~3.5 tps 4-bit (Q4_K_M) GGUF. Performs documentation tasks. Assigned E-Cores 8-11 from CPU.


*Local* - Intelligence - 1 Agent - Fits In VRAM

*   Qwen3-Coder-7B: ~100 tps 4-bit (Q4_K_M) GGUF. Same as Polecat version. Use for higher intelligence with long context lengths (14k tokens) with 1 agent at a time. ~6.5GB VRAM Usage.

*   Qwen3-Coder-3B: ~100 tps 4-bit (Q4_K_M) GGUF. Use for very long context lengths (up to 32k tokens). ~6GB VRAM Usage.

### **Librarian**:

*Local* - Documentation - 1 Agent - Fits In Local E-Cores + RAM

*   SmolLM2-1.7B-Instruct : 150+ tps on E-Cores only.

## 1. Answer Remaining Questions

- [x] **Decide Mayor Model**: 

*   Gemini 3 Pro Thinking: Extremely high context window, great for breaking down epics into convoys of beads across a large variety of rigs.

- [x] **Decide Crew Model**: 

*   Gemini 3 Flash: High context window without the cost of deep thinking. Perfect for answering questions about rigs.

- [x] **Decide Polecat Model**: 

*   Use a switcher strategy by estimating the token count of each bead.

*   Qwen3-Coder-3B: If next two beads of work are < 6k tokens, create two agents with the Polecat role and tackle both simultaneously.

or if hallucinations are an issue

*   DeepSeek-Coder-V3-Lite (8B): If <= 6k tokens and if Qwen3-Coder-3B proves to hallucinate too much due to Godot 4.x gdscript specifics. Limit to one polecat at a time with best in weight reasoning and minimal hallucinations within a small token window.

or for when token size matters

*   Qwen3-Coder-7B: If >= 6k and <= 14k tokens, limit to one polecat at a time with good reasoning and minimal hallucinations but a larger token window.

- [x] **Decide Refinery Model**: 

*   DeepSeek-R1-Distill-Qwen-32B: 1 refinery agent running locally on CPU & RAM using 6 performance cores for deep thinking. We will leave 2 performance cores for Zorin OS 18 Pro and engineering work.

- [x] **Decide Librarian Model**: 

*   SmolLM2-1.7B-Instruct: 1 library agent running locally on CPU & RAM using 6 effeciency cores for documentation writing. We will use all effeciency cores for this agent.

- [x] **Decide Local Runner**: 

*   llama.cpp server: Low level, high performance. Runs any GGUF model on local hardware. Steep learning curve and CLI operation. Estimated ~70% faster than Ollama as of January 2026 due to better handling of the "FlashAttention-3" and "GQA" (Grouped Query Attention) implementations for the Qwen3 and Llama 4 architectures. We will set the `--ctk q8_0` (Key cache) and `--ctv q4_0` (Value cache) flags for the `Refinery` to prevent crashing.

## 2. Infrastructure Preparation

- [x] **OS Configuration**: Optimize Zorin OS 18 Pro and ensure NVIDIA drivers for the RTX 3080 are current.

- [ ] **Local Runner Setup**: Install local runner to provide OpenAI-compatible local endpoints.

- [ ] **Download LLM Models**: Download the specific models we will be using.

- [ ] **Create Gastown Guide**: Create a setup guide to install Gastown and connect it to our local runner and cloud providers.

- [ ] **Follow Gastown Guide**: Perform all the steps in the Gastown guide to prepare our local work environment. Modify the guide as we discover missing content to help future engineers get setup.

## 3. Testing Workflow

- [ ] **Test Polecats**: Provide models the 'Polecat' and 'Refinery' roles, point them at our AGENTS.MD file in a rig, and give them a task written as if a mayor sent it to them and see how they perform.

- [ ] **Test Refinery**: Provide models the 'Refinery' role, point them at our AGENTS.MD file in the same rig as the Polecats, and give them a code evaluation task written as if a mayor sent it to them and see how they perform.

## 4. Integration & Parallelization

- [ ] **Gastown Config**: Update Gastown agent definitions to point to local API providers.

- [ ] **Automated Handoff**: Verify the pipeline works by creating a convoy with the mayor and slinging it to the polecats and refinery.
# AI Foundations - Alura Course

> A comprehensive collection of notes and practical implementations from the AI Foundations course, covering intelligent agents, search algorithms, logic reasoning, and probabilistic modeling.

[![Course](https://img.shields.io/badge/Course-AI_Foundations-blue)](https://www.alura.com.br)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 📚 About This Repository

This repository documents my learning journey through the AI Foundations course at Alura. It includes comprehensive notes organized by topic, practical Python implementations, and Jupyter notebooks demonstrating key AI concepts and algorithms.

### 🎓 Course Certification

![Certificate](assets/Certificate.pdf)

View my [course certificate](assets/Certificate.pdf) demonstrating completion of all modules.

## 📖 Course Topics

### 1. Fundamentals of AI

- Evolution of computing and artificial intelligence
- Understanding AI systems and their applications
- Classification of intelligent systems (Narrow vs General AI)

### 2. Intelligent Agents

- Agent architecture and design patterns
- Reactive, model-based, goal-oriented, and utility-based agents
- Agent orchestration in complex systems
- Perception-Reasoning-Action cycles

### 3. Search Algorithms

- Uninformed search strategies (BFS, DFS)
- Informed search with heuristics (A\* algorithm)
- State-space representation
- Algorithm implementation and optimization

### 4. Logic and Reasoning

- Propositional and predicate logic
- Formal logic in AI systems
- Automated reasoning and inference engines
- Knowledge-based systems

### 5. Handling Uncertainty

- Probabilistic reasoning with Bayesian networks
- Markov chains and state transitions
- Dynamic Bayesian networks
- Reasoning in uncertain environments

### 6. Knowledge-Based Systems

- Expert systems and knowledge representation
- Problem modeling techniques
- Evaluating AI approaches
- Modeling dynamic processes

## 🗂️ Repository Structure

```
.
├── notes/                          # Course notes organized by topic
│   ├── 01-fundamentals/            # AI basics and evolution
│   ├── 02-agents/                  # Intelligent agents
│   ├── 03-search-algorithms/       # Search strategies
│   ├── 04-logic-reasoning/         # Logic and automated reasoning
│   ├── 05-uncertainty/             # Probabilistic reasoning
│   └── 06-knowledge-systems/       # Knowledge-based systems
│
├── exercises/                      # Practical implementations
│   ├── customer-behavior/          # Bayesian customer behavior model
│   ├── expert-system/              # Rule-based expert system
│   ├── uncertainty-analysis/       # Uncertainty modeling
│   ├── weather-prediction/         # Markov chain weather predictor
│   └── electronic-products/        # A* product recommendations
│
├── assets/                         # Course materials
│   └── certificate.pdf             # Course completion certificate
│
└── archive/                        # Archived materials

```

## 💻 Exercises

### 1. Customer Behavior Analysis

**Technologies**: Bayesian Networks, Python, NumPy, Matplotlib, Seaborn

Implements a probabilistic model for analyzing e-commerce customer behavior using Bayesian networks. Models purchase probability based on purchase history, time on site, and promotion interaction.

- 📁 [Python Script](exercises/customer-behavior/customer_behavior_model.py)
- 📓 [Jupyter Notebook](exercises/customer-behavior/customer_behavior_model.ipynb)

### 2. Expert System with Inference Engine

**Technologies**: Knowledge-Based Systems, Forward Chaining, Python

Rule-based expert system demonstrating automated reasoning. Uses forward chaining to infer conclusions from facts and rules, with a medical diagnosis example.

- 📁 [Python Script](exercises/expert-system/specialist_system.py)
- 📓 [Jupyter Notebook](exercises/expert-system/specialist_system.ipynb)

### 3. Uncertainty Analysis

**Technologies**: Bayesian Networks, pgmpy, scipy, Python

Models uncertainty in customer purchase decisions using discrete Bayesian networks and continuous probability distributions.

- 📁 [Python Script](exercises/uncertainty-analysis/uncertainty.py)
- 📓 [Jupyter Notebook](exercises/uncertainty-analysis/uncertainty.ipynb)

### 4. Weather Prediction with Markov Chains

**Technologies**: Markov Chains, NumPy, Stochastic Modeling

Implements a weather prediction system using Markov chains to model state transitions and calculate steady-state distributions.

- 📁 [Python Script](exercises/weather-prediction/weather_predictor.py)
- 📓 [Jupyter Notebook](exercises/weather-prediction/weather_predictor.ipynb)

### 5. Product Recommendation System

**Technologies**: A\* Algorithm, Search Algorithms, Python

Uses A\* search algorithm with conversion probability as heuristic to find optimal product recommendation paths for e-commerce.

- 📁 [Python Script](exercises/electronic-products/produtos_eletronicos.py)
- 📓 [Jupyter Notebook](exercises/electronic-products/produtos_eletronicos.ipynb)

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/ai-foundations-alura.git
cd ai-foundations-alura
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Run any exercise:

```bash
# Run Python scripts directly
python exercises/customer-behavior/customer_behavior_model.py

# Or open Jupyter notebooks
jupyter notebook exercises/customer-behavior/customer_behavior_model.ipynb
```

## 📦 Dependencies

- **numpy**: Numerical computations and array operations
- **matplotlib**: Data visualization and plotting
- **seaborn**: Statistical data visualization
- **scipy**: Scientific computing and statistics
- **pgmpy**: Probabilistic graphical models (Bayesian networks)

See [requirements.txt](requirements.txt) for complete list with versions.

## 📝 Notes Organization

All course notes are organized in the `notes/` directory, categorized by topic:

- **Fundamentals**: Core AI concepts and evolution
- **Agents**: Intelligent agent design and architecture
- **Search Algorithms**: Problem-solving through search
- **Logic Reasoning**: Formal logic and automated reasoning
- **Uncertainty**: Probabilistic reasoning and Bayesian methods
- **Knowledge Systems**: Expert systems and knowledge representation

Each folder contains markdown files with detailed explanations, examples, and key takeaways from the course.

## 🎯 Key Learning Outcomes

- ✅ Understanding of AI fundamentals and intelligent agent architectures
- ✅ Implementation of search algorithms (BFS, DFS, A\*)
- ✅ Application of formal logic and automated reasoning
- ✅ Probabilistic modeling with Bayesian networks
- ✅ Practical experience with knowledge-based systems
- ✅ Real-world applications in e-commerce, diagnosis, and prediction

## 🤝 Contributing

This is a personal learning repository, but suggestions and improvements are welcome! Feel free to:

- Open an issue for questions or discussion
- Submit a pull request with improvements
- Share your own implementations

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Yuri**

- LinkedIn: [Connect with me](https://linkedin.com/in/yurileonel)
- GitHub: [@yourusername](https://github.com/YuriLeonel)

## 🙏 Acknowledgments

- **Alura** for providing comprehensive AI education
- Course instructors for excellent content and examples
- Open-source community for the amazing tools and libraries

---

⭐ If you found this repository helpful, please consider giving it a star!

📚 Check out the [notes](notes/README.md) and [exercises](exercises/README.md) for detailed content.

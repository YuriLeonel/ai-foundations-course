# Practical Exercises

This directory contains hands-on implementations of key AI concepts covered in the course. Each exercise includes both a standalone Python script and an interactive Jupyter notebook with detailed explanations.

## 🎯 Exercise Overview

### 1. Customer Behavior Analysis

**📁 Directory**: `customer-behavior/`  
**🎓 Topics**: Bayesian Networks, Probabilistic Reasoning, E-commerce Analytics

A sophisticated probabilistic model for analyzing customer behavior in an online store using Bayesian networks.

**Key Features**:

- Three-variable Bayesian network (Purchase History, Time on Site, Promotion Interaction)
- Conditional probability tables (CPTs) modeling dependencies
- Customer segmentation (High/Medium/Low potential)
- Personalized recommendation engine
- Comprehensive visualizations (heatmaps, distributions, bar charts)

**Files**:

- [`customer_behavior_model.py`](customer-behavior/customer_behavior_model.py) - Complete implementation with visualizations
- [`customer_behavior_model.ipynb`](customer-behavior/customer_behavior_model.ipynb) - Interactive notebook

**Run it**:

```bash
python customer-behavior/customer_behavior_model.py
# or
jupyter notebook customer-behavior/customer_behavior_model.ipynb
```

---

### 2. Expert System with Inference Engine

**📁 Directory**: `expert-system/`  
**🎓 Topics**: Knowledge-Based Systems, Forward Chaining, Automated Reasoning

A rule-based expert system demonstrating automated reasoning through forward chaining inference.

**Key Features**:

- Knowledge base storing facts and rules
- Forward chaining inference engine
- Automatic conclusion derivation
- Medical diagnosis example domain
- Extensible architecture for different domains

**Files**:

- [`specialist_system.py`](expert-system/specialist_system.py) - Core implementation
- [`specialist_system.ipynb`](expert-system/specialist_system.ipynb) - Interactive notebook with examples

**Run it**:

```bash
python expert-system/specialist_system.py
```

---

### 3. Uncertainty Analysis

**📁 Directory**: `uncertainty-analysis/`  
**🎓 Topics**: Bayesian Networks, Probabilistic Inference, Continuous Distributions

Models uncertainty in customer purchase decisions using discrete Bayesian networks and continuous probability distributions.

**Key Features**:

- Discrete Bayesian network for purchase prediction
- Variable elimination for inference
- Conditional probability tables
- Normal distribution for continuous variables
- Integration with pgmpy library

**Files**:

- [`uncertainty.py`](uncertainty-analysis/uncertainty.py) - Full implementation
- [`uncertainty.ipynb`](uncertainty-analysis/uncertainty.ipynb) - Interactive analysis

**Dependencies**:

```bash
pip install pgmpy scipy
```

**Run it**:

```bash
python uncertainty-analysis/uncertainty.py
```

---

### 4. Weather Prediction with Markov Chains

**📁 Directory**: `weather-prediction/`  
**🎓 Topics**: Markov Chains, State Transitions, Stochastic Modeling

Implements a weather forecasting system using Markov chains to model state transitions.

**Key Features**:

- Three-state system (Sunny, Cloudy, Rainy)
- Transition probability matrix
- Next-day prediction
- Multi-day sequence generation
- Steady-state distribution calculation
- Statistical analysis over multiple simulations

**Files**:

- [`weather_predictor.py`](weather-prediction/weather_predictor.py) - Complete predictor with examples
- [`weather_predictor.ipynb`](weather-prediction/weather_predictor.ipynb) - Interactive forecasting

**Run it**:

```bash
python weather-prediction/weather_predictor.py
```

---

### 5. Product Recommendation System

**📁 Directory**: `electronic-products/`  
**🎓 Topics**: A\* Algorithm, Informed Search, Heuristic Functions

Uses A\* search algorithm with conversion probability as heuristic to optimize product recommendations.

**Key Features**:

- A\* pathfinding implementation
- Conversion probability as heuristic
- Product graph representation
- Optimal path calculation
- E-commerce optimization

**Files**:

- [`produtos_eletronicos.py`](electronic-products/produtos_eletronicos.py) - A\* recommendation engine
- [`produtos_eletronicos.ipynb`](electronic-products/produtos_eletronicos.ipynb) - Interactive recommendations

**Run it**:

```bash
python electronic-products/produtos_eletronicos.py
```

---

## 🛠️ Technical Requirements

### Python Version

- Python 3.8 or higher

### Core Dependencies

```bash
pip install numpy matplotlib seaborn scipy pgmpy
```

### For Jupyter Notebooks

```bash
pip install jupyter notebook
```

Or install all at once:

```bash
pip install -r ../requirements.txt
```

---

## 📊 Complexity Overview

| Exercise               | Difficulty          | Lines of Code | Key Algorithm        |
| ---------------------- | ------------------- | ------------- | -------------------- |
| Expert System          | ⭐⭐ Beginner       | ~50           | Forward Chaining     |
| Weather Prediction     | ⭐⭐ Beginner       | ~180          | Markov Chain         |
| Product Recommendation | ⭐⭐⭐ Intermediate | ~120          | A\* Search           |
| Uncertainty Analysis   | ⭐⭐⭐ Intermediate | ~60           | Variable Elimination |
| Customer Behavior      | ⭐⭐⭐⭐ Advanced   | ~490          | Bayesian Network     |

---

## 🎓 Learning Approach

### For Beginners

Start with:

1. **Expert System** - Understand rule-based reasoning
2. **Weather Prediction** - Learn probabilistic state transitions

### For Intermediate Learners

Progress to: 3. **Product Recommendation** - Master informed search algorithms 4. **Uncertainty Analysis** - Apply Bayesian inference

### For Advanced Study

Complete with: 5. **Customer Behavior** - Integrate multiple AI techniques

---

## 💡 Extending the Exercises

### Ideas for Enhancement

**Customer Behavior**:

- Add more variables (device type, time of day, referral source)
- Integrate real customer data
- Implement A/B testing framework
- Add deep learning predictions

**Expert System**:

- Expand to other domains (finance, legal, technical support)
- Add backward chaining
- Implement uncertainty handling (fuzzy logic)
- Create GUI interface

**Uncertainty Analysis**:

- Add temporal aspects (Dynamic Bayesian Networks)
- Integrate with real-time data sources
- Implement learning from data
- Compare different inference methods

**Weather Prediction**:

- Add more states and environmental factors
- Implement Hidden Markov Models
- Use real weather data
- Create prediction visualization dashboard

**Product Recommendation**:

- Incorporate user preferences and ratings
- Add collaborative filtering
- Implement multi-objective optimization
- Create recommendation explanations

---

## 🔗 Related Content

- [Course Notes](../notes/README.md) - Theoretical foundations
- [Main README](../README.md) - Repository overview
- [Certificate](../assets/certificate.pdf) - Course completion

---

## 🐛 Troubleshooting

### Common Issues

**ImportError: pgmpy not found**

```bash
pip install pgmpy
```

**Matplotlib display issues**

```bash
# For headless environments
import matplotlib
matplotlib.use('Agg')
```

**Seaborn style warnings**

```python
# Use newer syntax
plt.style.use('seaborn-v0_8')
```

---

## 📝 Code Quality

All exercises follow:

- ✅ PEP 8 style guidelines
- ✅ Comprehensive docstrings
- ✅ Type hints where appropriate
- ✅ Error handling
- ✅ Clear variable names
- ✅ Modular design

---

Happy coding! 🚀

For questions or suggestions, please open an issue in the repository.

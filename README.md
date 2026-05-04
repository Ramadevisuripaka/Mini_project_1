---

## 📐 Mathematical Working of the Model

### 🔹 Multiple Linear Regression Formula

:contentReference[oaicite:0]{index=0}

Where:
- \(y\) → Predicted house price  
- \(x_1, x_2, ..., x_n\) → Input features (bedrooms, sqft, etc.)  
- \(\beta_0\) → Intercept  
- \(\beta_1, \beta_2, ..., \beta_n\) → Feature coefficients  

---

## 🧠 How the Model Learns

The model finds the best coefficients by minimizing error using:

### 🔹 Cost Function (Mean Squared Error)

:contentReference[oaicite:1]{index=1}

👉 The goal is to **minimize this error** so predictions are close to actual values.

---

## ⚙️ Step-by-Step Working

1. Load dataset (`House.csv`)  
2. Split into:
   - Training data (80%)  
   - Testing data (20%)  

3. Model learns:
   - Relationship between inputs & price  
   - Calculates coefficients  

4. Prediction:
   - New input → applied to equation  
   - Output → predicted price  

---

## 📊 Model Evaluation Metrics

### 🔹 R² Score (Accuracy)

:contentReference[oaicite:2]{index=2}

- Value ranges: **0 to 1**
- Closer to **1 → better model**

---

### 🔹 RMSE (Error)

:contentReference[oaicite:3]{index=3}

- Lower value → better predictions  

---

## 📈 Model Performance Interpretation

| Metric | Meaning |
|------|--------|
| Train Accuracy | How well model fits training data |
| Test Accuracy | How well model generalizes |
| RMSE | Average prediction error |

👉 If:
- Train accuracy high & Test low → Overfitting  
- Both low → Underfitting  

---

## 📊 Visualization

### 🔹 Accuracy Graph

![Accuracy Graph](static/accuracy.png)

---

### 🔹 Loss Graph

![Loss Graph](static/loss.png)

---

## 🧪 Example Prediction (Manual Understanding)

Example Input:
- Bedrooms = 3  
- Sqft = 1340  
- City = Seattle  

Model calculates:

\[
Price = \beta_0 + \beta_1(3) + \beta_2(1340) + ...
\]

👉 Output: Predicted House Price  

---

## 🎯 Key Insight

This model transforms:
👉 **Real-world housing features → mathematical equation → predicted price**

---

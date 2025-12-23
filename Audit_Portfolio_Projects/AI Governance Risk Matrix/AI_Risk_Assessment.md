# AI Governance Risk Assessment (NIST AI RMF)
**Project Lead:** Mansi Singh  
**Framework:** NIST AI Risk Management Framework (AI RMF 1.0)  
**System Audited:** "MarketingGen" (Hypothetical Generative AI Tool for Press Releases)

---

## 1. Executive Summary
This assessment evaluates the compliance of the "MarketingGen" tool against NIST AI RMF standards. The primary risks identified are **Data Leakage** (confidential data entering the public model) and **Hallucinations** (inaccurate output).

## 2. Risk Control Matrix

| NIST Category | Risk ID | Risk Description | Proposed Control (Mitigation) | Test Procedure |
| :--- | :--- | :--- | :--- | :--- |
| **Valid & Reliable** | R-01 | AI hallucinates facts, creating fake product features. | **Human-in-the-Loop (HITL):** Senior Editor must sign-off on all AI outputs. | Sample 5 published articles and verify 'Editor Approval' logs. |
| **Safe & Secure** | R-02 | Employees paste PII/Confidential data into prompt. | **DLP Blocking:** Configure API to reject patterns like SSNs or "Confidential". | Attempt to input dummy credit card info; verify system blocks it. |
| **Explainable** | R-03 | AI output shows bias against specific demographics. | **Adversarial Testing:** Run quarterly 'Red Team' prompt attacks. | Review Q3 Red Team Report for bias findings. |
| **Privacy** | R-04 | User data is used to train the public model. | **Opt-Out Switch:** Enterprise 'Zero-Retention' setting enabled. | Inspect OpenAI/Model Admin console settings. |

## 3. Conclusion
The system requires the implementation of **DLP Blocking (R-02)** before full deployment to production.
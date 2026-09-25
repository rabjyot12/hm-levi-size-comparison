# H&M vs Levi's Size Comparison

## Live streamlit deployed link: https://rabjyot12-hm-levi-size-comparison-app-jb7jyz.streamlit.app/

A data analysis project that compares men's clothing size charts from H&M and Levi's using their published body measurement guides.

The project analyzes differences between the two brands and includes a simple size-matching tool based on a user's body measurement.

---

## Project Objective

The objective of this project is to compare the published men's clothing size charts of H&M and Levi's and understand how their size ranges differ.

The project focuses on:

- Comparing chest and waist measurements for tops
- Comparing waist and hip/seat measurements for bottoms
- Measuring the overlap between size ranges
- Comparing the midpoint of published measurement ranges
- Finding a matching or closest published size for a given body measurement

---

## Data Sources

The measurements were collected from the official size guides of:

- H&M: https://www2.hm.com/en_in/customer-service/sizeguide.html
- Levi's: https://www.levi.com/US/en_US/info/sizeguide

The project uses body measurement charts rather than individual garment measurements.

---

How to Run
1. Clone the repository
git clone https://github.com/rabjyot12/hm-levi-size-comparison.git
2. Open the project
cd hm-levi-size-comparison
3. Create a virtual environment

Windows:

python -m venv .venv

Activate it:

.venv\Scripts\activate
4. Install the required packages
pip install -r requirements.txt
5. Run the analysis
python src/data_analysis.py


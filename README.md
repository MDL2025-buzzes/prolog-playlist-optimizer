# Playlist Optimizer via Logic Programming

## Overview

This project is a demonstration of **First Order Logic (FOL)** and **rule-based inference** applied to the optimization of music playlist order for smooth transitions. It features a Python-based GUI (using Streamlit) that interacts with a Prolog knowledge base, allowing users to explore logical reasoning and playlist optimization in an educational context.

**Academic Context:**  
Developed for a college-level Advanced Discrete Mathematics course (Fall 2025), this project illustrates:
- Rule chaining and logical inference
- Integration of Python and SWI-Prolog
- Visualization of logical queries and their results

---

## Features

- **Interactive Web GUI:** Built with Streamlit for intuitive use and visualization.
- **Prolog Knowledge Base:** Encodes facts and rules about songs, genres, energy levels, and transitions.
- **Rule-Based Inference:** Demonstrates multi-step logical reasoning (e.g., identifying outliers, recommending playlist order).
- **Custom Query Support:** Users can run their own Prolog queries and see results instantly.
- **Educational Value:** Clear mapping between FOL rules and real-world playlist optimization.

---

## File Structure

- `Aplikasi Inferensi/app_inferensi_kebijakan.py`  
  Main Python app. Handles the GUI, connects to Prolog, runs queries, and displays results.

- `Aplikasi Inferensi/prolog_kb.pl`  
  Prolog knowledge base. Contains facts about songs and rules for playlist optimization.

- `Aplikasi Inferensi/requirements.txt`  
  Python dependencies for running the app.

---

## Setup & Installation

1. **Clone the Repository**
   ```sh
   git clone <your-repo-url>
   cd eas/Aplikasi\ Inferensi
   ```

2. **Install Python Requirements**
   ```sh
   pip install -r requirements.txt
   ```

3. **Install SWI-Prolog**
   - Download and install from: https://www.swi-prolog.org/Download.html

---

## Usage

1. **Start the Streamlit App**
   ```sh
   streamlit run app_inferensi_kebijakan.py
   ```

2. **Open the Web Interface**
   - The app will open in your browser.
   - Explore built-in inference queries.
   - View and edit the Prolog knowledge base.
   - Run custom Prolog queries and see results in real time.

---

## Example Inference Rules

- **lagu_ekstrem(X):** Song with very high or low energy.
- **pembentuk_outlier(X):** Extreme songs are potential outliers.
- **wajib_kurasi_manual(X):** Outliers require manual curation.
- **transisi_kasar(X, Y):** Rough transitions (energy contrast or high graph distance).
- **rekomendasi_urutan(X, Y):** Ideal song pairs for smooth transitions.

See `prolog_kb.pl` for all facts and rules.

---

## Screenshots

*(Add screenshots of the GUI here for better illustration)*

---

## Credits

- Developed for Advanced Discrete Mathematics, Fall 2025
- Technologies: Python, Streamlit, SWI-Prolog, pyswip, pandas

---

## License

None

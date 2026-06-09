normal_ranges = {
    "Hemoglobin": (12.0, 17.0), "RBC Count": (4.2, 5.9), "WBC Count": (4000.0, 11000.0),
    "Platelets": (150000.0, 450000.0), "Hematocrit": (36.0, 52.0), "MCV": (80.0, 100.0),
    "MCH": (27.0, 33.0), "MCHC": (32.0, 36.0), "RDW": (11.0, 15.0), "Neutrophils": (40.0, 70.0),
    "Lymphocytes": (20.0, 40.0), "Monocytes": (2.0, 8.0), "Eosinophils": (1.0, 4.0), "Basophils": (0.0, 1.0),
    "Fasting Blood Sugar": (70.0, 99.0), "Postprandial Blood Sugar": (0.0, 140.0), "Random Blood Sugar": (70.0, 140.0),
    "HbA1c": (0.0, 5.7), "Total Cholesterol": (0.0, 200.0), "HDL Cholesterol": (40.0, 999.0),
    "LDL Cholesterol": (0.0, 100.0), "VLDL": (5.0, 40.0), "Triglycerides": (0.0, 150.0), "Cholesterol/HDL Ratio": (0.0, 5.0),
    "Bilirubin Total": (0.3, 1.2), "Bilirubin Direct": (0.0, 0.3), "SGOT": (10.0, 40.0), "SGPT": (7.0, 56.0),
    "Alkaline Phosphatase": (44.0, 147.0), "Albumin": (3.5, 5.5), "Total Protein": (6.0, 8.3),
    "Creatinine": (0.6, 1.3), "Blood Urea": (7.0, 20.0), "BUN": (8.0, 23.0), "Uric Acid": (3.5, 7.2),
    "Sodium": (135.0, 145.0), "Potassium": (3.5, 5.0), "Chloride": (96.0, 106.0), "TSH": (0.4, 4.0),
    "T3": (80.0, 200.0), "T4": (5.0, 12.0), "Free T3": (2.3, 4.2), "Free T4": (0.8, 1.8),
    "CK-MB": (0.0, 25.0), "Homocysteine": (5.0, 15.0), "CRP": (0.0, 3.0), "Vitamin D": (30.0, 100.0),
    "Vitamin B12": (200.0, 900.0), "Calcium": (8.5, 10.5), "Magnesium": (1.7, 2.2), "Iron": (60.0, 170.0),
    "Ferritin": (12.0, 300.0), "ESR": (0.0, 20.0), "Procalcitonin": (0.0, 0.1), "D-Dimer": (0.0, 500.0),
    "Urine pH": (4.5, 8.0), "Specific Gravity": (1.005, 1.030), "Urine RBC": (0.0, 2.0), "Urine WBC": (0.0, 5.0)
}

qualitative_parameters = ["Urine Protein", "Urine Glucose", "Urine Ketones"]

def analyze(test, value):
    if test in qualitative_parameters:
        val_clean = str(value).strip().lower()
        if "negative" in val_clean or "nil" in val_clean or "normal" in val_clean:
            return "Normal"
        return "Critical High"

    if test == "Troponin":
        val_clean = str(value).strip().lower()
        if "negative" in val_clean or "normal" in val_clean or "low" in val_clean:
            return "Normal"
        return "Critical High"

    try:
        val_num = float(str(value).replace(",", ""))
    except ValueError:
        return "Unknown"

    if test not in normal_ranges:
        return "Unknown"

    low, high = normal_ranges[test]
    if low <= val_num <= high:
        return "Normal"
    
    if val_num < low:
        return "Critical Low" if val_num <= (low * 0.75) else "Slightly Low"
    else:
        return "Critical High" if val_num >= (high * 1.25) else "Slightly High"
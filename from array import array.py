from array import array

# ------------------------------
# INTEGERS: Vital signs values
# ------------------------------
blood_pressures = [120, 135, 128, 140, 115]  # integer values for patients

total_bp = sum(blood_pressures)
avg_bp = total_bp / len(blood_pressures)
min_bp = min(blood_pressures)
max_bp = max(blood_pressures)

# ------------------------------
# STRINGS: Formatted Report
# ------------------------------
report = (
    f"Clinic Vital Signs Log Report\n"
    f"Total Blood Pressure Readings: {total_bp}\n"
    f"Average Blood Pressure: {avg_bp:.2f}\n"
    f"Minimum BP: {min_bp}, Maximum BP: {max_bp}"
)
print(report)

# ------------------------------
# BOOLEANS: Threshold condition
# ------------------------------
threshold = 130
# compound boolean condition: check average AND also if max > threshold
if avg_bp > threshold and max_bp > threshold:
    print("Status: Above Standard\n")
else:
    print("Status: Below Standard\n")

# ------------------------------
# LISTS: Manage Vital Sign Items
# ------------------------------
vital_signs = ["BP-120", "BP-135", "BP-128", "BP-140", "BP-115"]
print("Original List:", vital_signs)

# Add a new element
vital_signs.append("BP-130")

# Remove one based on a condition (remove any reading under 120)
vital_signs = [item for item in vital_signs if int(item.split("-")[1]) >= 120]

# Sort the list
vital_signs.sort()
print("Modified & Sorted List:", vital_signs, "\n")

# ------------------------------
# ARRAYS: Store fixed-size subset
# ------------------------------
bp_array = array('i', [120, 135, 128, 140, 115])
sum_array = sum(bp_array)
print("Array Sum:", sum_array)
print("List Sum:", total_bp, "\n")

# ------------------------------
# DICTIONARIES: Records Management
# ------------------------------
records = [
    {"id": 1, "name": "Patient A", "value": 120},
    {"id": 2, "name": "Patient B", "value": 135},
    {"id": 3, "name": "Patient C", "value": 128},
]

# Update one record
records[1]["value"] = 138  # Patient B new value

# Delete another record (Patient C)
records = [rec for rec in records if rec["id"] != 3]

# Compute total value field
total_value = sum(rec["value"] for rec in records)

print("Updated Records:")
for rec in records:
    print(rec)

print(f"\nTotal of 'value' field across records: {total_value}")

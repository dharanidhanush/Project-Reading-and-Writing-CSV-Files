import csv

def read_csv_fieldnames(filename):
    """
    Reads the field names from the first row of the CSV file.
    Returns a list of field names.
    """
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return reader.fieldnames

def read_csv_as_list_dict(filename):
    """
    Reads the CSV file and returns a list of dictionaries,
    one per row using field names as keys.
    """
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def read_csv_as_nested_dict(filename, keyfield):
    """
    Reads the CSV file and returns a dictionary of dictionaries.
    Outer dictionary uses keyfield value as key.
    Inner dictionary represents the row.
    """
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return {row[keyfield]: row for row in reader}

def write_csv_from_list_dict(filename, table, fieldnames):
    """
    Writes a list of dictionaries to a CSV file using specified fieldnames.
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in table:
            writer.writerow(row)

# 🧪 Unit Tests
def test_csv_functions():
    test_file = "students.csv"
    fieldnames = ["ID", "Name", "Score"]
    data = [
        {"ID": "101", "Name": "Dharani", "Score": "95"},
        {"ID": "102", "Name": "Arun", "Score": "88"},
        {"ID": "103", "Name": "Priya", "Score": "92"}
    ]

    # Write test data
    write_csv_from_list_dict(test_file, data, fieldnames)

    # Test read_csv_fieldnames
    assert read_csv_fieldnames(test_file) == fieldnames

    # Test read_csv_as_list_dict
    assert read_csv_as_list_dict(test_file) == data

    # Test read_csv_as_nested_dict
    nested = read_csv_as_nested_dict(test_file, "ID")
    assert nested["101"]["Name"] == "Dharani"
    assert nested["102"]["Score"] == "88"

    print("✅ All tests passed successfully!")

# Run tests
if __name__ == "__main__":
    test_csv_functions()

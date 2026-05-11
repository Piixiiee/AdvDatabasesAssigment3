import csv

# Input CSV file
csv_file = "Students.csv"

# Output TTL file
ttl_file = "students.ttl"

# Prefixes
prefixes = """
@prefix ex: <http://example.org/> .
@prefix student: <http://example.org/student/> .

"""

with open(csv_file, newline='', encoding='utf-8') as infile, \
     open(ttl_file, 'w', encoding='utf-8') as outfile:

    # Write prefixes
    outfile.write(prefixes)

    reader = csv.DictReader(infile)
    for row in reader:

        student_id = row["Student id"]
        student_name = row["Student name"]
        programme = row["Programme"]
        year = row["Year"]
        graduated = row["Graduated"]

        ttl_entry = f"""
student:{student_id}
    ex:hasStudentId "{student_id}" ;
    ex:hasStudentName "{student_name}" ;
    ex:hasProgramme "{programme}" ;
    ex:hasGraduated "{graduated}" ;
    ex:hasAdmissionYear "{year}" .


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
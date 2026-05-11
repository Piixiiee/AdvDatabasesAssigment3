import csv

# Input CSV file
csv_file = "Registrations.csv"

# Output TTL file
ttl_file = "registrations.ttl"

# Prefixes
prefixes = """
@prefix ex: <http://example.org/> .
@prefix registrations: <http://example.org/registrations/> .

"""

with open(csv_file, newline='', encoding='utf-8') as infile, \
     open(ttl_file, 'w', encoding='utf-8') as outfile:

    # Write prefixes
    outfile.write(prefixes)

    reader = csv.DictReader(infile)
    for row in reader:

        student_id = row["Student id"]
        course_instance = row["Course Instance"]
        status = row["Status"]
        grade = row["Grade"]

        ttl_entry = f"""
registrations:{student_id}
    ex:hasStudentId "{student_id}" ;
    ex:hasCourseInstance "{course_instance}" ;
    ex:hasStatus "{status}" ;
    ex:hasGrade "{grade}" .


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
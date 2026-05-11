import csv

# Input CSV file
csv_file = "Teaching_Assistants.csv"

# Output TTL file
ttl_file = "teacher_Assistants.ttl"

# Prefixes
prefixes = """
@prefix ex: <http://example.org/> .
@prefix teacher_Assistants: <http://example.org/teacher_Assistants/> .

"""

with open(csv_file, newline='', encoding='utf-8') as infile, \
     open(ttl_file, 'w', encoding='utf-8') as outfile:

    # Write prefixes
    outfile.write(prefixes)

    reader = csv.DictReader(infile)
    for row in reader:

        teacher_id = row["Teacher id"]
        teacher_name = row["Teacher name"]
        department_name = row["Department name"]
        division_name = row["Division name"]

        ttl_entry = f"""
teaching_Assistants:{teacher_id}
    ex:hasTeacherId "{teacher_id}" ;
    ex:hasTeacherName "{teacher_name}" ;
    ex:hasDepartmentName "{department_name}" ;
    ex:hasDivisionName "{division_name}" .


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
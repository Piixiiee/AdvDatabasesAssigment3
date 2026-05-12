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
:registrations_{student_id}
    :Is_reg :student_{student_id} ;
    :Registered_to :course_instance_{course_instance} ;
    :status "{status}" ;
    :grade "{grade}" .


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
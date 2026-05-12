import csv

# Input CSV file
csv_file = "Students.csv"

# Output TTL file
ttl_file = "students.ttl"

# Prefixes
prefixes = """
@prefix : <http://www.semanticweb.org/frida/ontologies/2026/3/untitled-ontology-3/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

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
:student_{student_id}
    rdf:type :Student ;
    :studentId "{student_id}" ;
    :studentName "{student_name}" ;
    :Enrolled_in :Programme_{programme} ;
    :graduated {graduated.lower()} ;
    :admissionYear "{year}" .


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
import csv

# Input CSV file
csv_file = "Teaching_Assistants.csv"

# Output TTL file
ttl_file = "teacher_Assistants.ttl"

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

        teacher_id = row["Teacher id"]
        teacher_name = row["Teacher name"]
        department_name = row["Department name"]
        division_name = row["Division name"]

        ttl_entry = f"""
:teaching_Assistant_{teacher_id}
    rdf:type :Teaching_assistant ;
    :teacherId "{teacher_id}" ;
    :teacherName "{teacher_name}" ;
    :Works_for :department_{department_name} ;
    :Teacher_Belongs_To :division_{division_name};
    :Might_be :student_{teacher_id} .

:teacher_{teacher_id}
    rdf:type :Teacher ;
    :teacherId "{teacher_id}" ;
    :teacherName "{teacher_name}" ;
    :Works_for :department_{department_name} ;
    :Teacher_Belongs_To :division_{division_name} .

:department_{department_name}
    rdf:type :Department .

:division_{division_name}
    rdf:type :Division .
        
"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
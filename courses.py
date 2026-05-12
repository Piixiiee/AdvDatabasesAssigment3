#Assignment 3 - Group 20 Frida Sundelin & Jennifer Hallberg
import csv

# Input CSV file
csv_file = "Courses.csv"

# Output TTL file
ttl_file = "courses.ttl"

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

        course_code = row["Course code"]
        course_name = row["Course name"]
        credits = row["Credits"]
        level = row["Level"]
        department = row["Department"]
        division = row["Division"]
        owned_by = row["Owned By"]

        ttl_entry = f"""
:course_{course_code}
    rdf:type :Course ;
    :courseCode "{course_code}" ;
    :courseName "{course_name}" ;
    :credits "{credits}" ;
    :level "{level}" ;
    :Belongs_To_Department :department_{department} ;
    :Courses_Belongs_to :division_{division} ;
    :Owned_By_Programme :programme_{owned_by} .

:department_{department}
    rdf:type :Department .

:division_{division}
    rdf:type :Division .
"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
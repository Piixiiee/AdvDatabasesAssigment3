import csv

# Input CSV file
csv_file = "Programmes.csv"

# Output TTL file
ttl_file = "programmes.ttl"

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

        programme_code = row["Programme code"]
        programme_name = row["Programme name"]
        department_name = row["Department name"]
        director = row["Director"]

        ttl_entry = f"""
:programme_{programme_code}
    rdf:type :Programme ;
    :programmeCode "{programme_code}" ;
    :programmeName "{programme_name}" ;
    :departmentName "{department_name}" ;
    :hasDirector :senior_teacher_{director} .

:department_{department_name}
    :rdf:type :Department .
"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
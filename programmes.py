import csv

# Input CSV file
csv_file = "Programmes.csv"

# Output TTL file
ttl_file = "programmes.ttl"

# Prefixes
prefixes = """
@prefix ex: <http://example.org/> .
@prefix programmes: <http://example.org/programmes/> .

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
programme:{programme_code}
    ex:hasProgrammeCode "{programme_code}" ;
    ex:hasProgrammeName "{programme_name}" ;
    ex:hasDepartmentName "{department_name}" ;
    ex:hasDirector "{director}" .


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
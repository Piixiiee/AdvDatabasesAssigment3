import csv

# Input CSV file
csv_file = "Reported_Hours.csv"

# Output TTL file
ttl_file = "reported_Hours.ttl"

# Prefixes
prefixes = """
@prefix ex: <http://example.org/> .
@prefix reported_Hours: <http://example.org/reported_Hours/> .

"""

with open(csv_file, newline='', encoding='utf-8') as infile, \
     open(ttl_file, 'w', encoding='utf-8') as outfile:

    # Write prefixes
    outfile.write(prefixes)

    reader = csv.DictReader(infile)
    for row in reader:

        course_code = row["Course code"]
        teacher_id = row["Teacher Id"]
        hours = row["Hours"]

        ttl_entry = f"""
reported_Hours:{course_code}
    ex:hasCourseCode "{course_code}" ;
    ex:hasTeacherId "{teacher_id}" ;
    ex:hasHours "{hours}" .


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
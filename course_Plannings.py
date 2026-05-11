import csv

# Input CSV file
csv_file = "Course_Plannings.csv"

# Output TTL file
ttl_file = "course_Plannings.ttl"

# Prefixes
prefixes = """
@prefix ex: <http://example.org/> .
@prefix course_Plannings: <http://example.org/course_Plannings/> .

"""

with open(csv_file, newline='', encoding='utf-8') as infile, \
     open(ttl_file, 'w', encoding='utf-8') as outfile:

    # Write prefixes
    outfile.write(prefixes)

    reader = csv.DictReader(infile)
    for row in reader:

        course = row["Course"]
        planned_number_of_students = row["Planned number of Students"]
        senior_hours = row["Senior Hours"]
        assistant_hours = row["Assistant Hours"]

        ttl_entry = f"""
course_Planning:{course}
    ex:hasCourse "{course}" ;
    ex:hasPlannedNumberOfStudents "{planned_number_of_students}" ;
    ex:hasSeniorHours "{senior_hours}" ;
    ex:hasAssistantHours "{assistant_hours}" .


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
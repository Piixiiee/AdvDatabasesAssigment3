import csv

# Input CSV file
csv_file = "Assigned_Hours.csv"

# Output TTL file
ttl_file = "assignedHours.ttl"

# Prefixes
prefixes = """
@prefix ex: <http://example.org/> .
@prefix assigned_Hours: <http://example.org/assigned_Hours/> .

"""

with open(csv_file, newline='', encoding='utf-8') as infile, \
     open(ttl_file, 'w', encoding='utf-8') as outfile:

    # Write prefixes
    outfile.write(prefixes)

    reader = csv.DictReader(infile)
    for row in reader:

        course_code = row["Course code"]
        study_period = row["Study Period"]
        academic_year = row["Academic Year"]
        teacher_id = row["Teacher Id"]
        hours = row["Hours"]
        course_instance = row["Course Instance"]

        ttl_entry = f"""
assigned_Hours:{course_code}
    ex:hasCourseCode "{course_code}" ;
    ex:hasStudyPeriod "{study_period}" ;
    ex:hasAcademicYear "{academic_year}" ;
    ex:hasTeacherId "{teacher_id}" ;
    ex:hasHours "{hours}" 
    ex:hasCourseInstance "{course_instance}" .


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
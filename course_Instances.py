import csv

# Input CSV file
csv_file = "Course_Instances.csv"

# Output TTL file
ttl_file = "course_Instances.ttl"

# Prefixes
prefixes = """
@prefix ex: <http://example.org/> .
@prefix course_Instances: <http://example.org/course_Instances/> .

"""

with open(csv_file, newline='', encoding='utf-8') as infile, \
     open(ttl_file, 'w', encoding='utf-8') as outfile:

    # Write prefixes
    outfile.write(prefixes)

    reader = csv.DictReader(infile)
    for row in reader:

        course_code = row["Course code"]
        study_period = row["Study period"]
        academic_year = row["Academic year"]
        instance_id = row["Instance_id"]
        examiner = row["Examiner"]

        ttl_entry = f"""
course_Instances:{course_code}
    ex:hasCourseCode "{course_code}" ;
    ex:hasStudyPeriod "{study_period}" ;
    ex:hasAcademicYear "{academic_year}" ;
    ex:hasInstanceId "{instance_id}" ;
    ex:hasexaminer "{examiner}" .


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
import csv

# Input CSV file
csv_file = "Programme_Courses.csv"

# Output TTL file
ttl_file = "programme_Courses.ttl"

# Prefixes
prefixes = """
@prefix ex: <http://example.org/> .
@prefix programme_Courses: <http://example.org/programme_Courses/> .

"""

with open(csv_file, newline='', encoding='utf-8') as infile, \
     open(ttl_file, 'w', encoding='utf-8') as outfile:

    # Write prefixes
    outfile.write(prefixes)

    reader = csv.DictReader(infile)
    for row in reader:

        programme_code = row["Programme code"]
        study_year = row["Study Year"]
        academic_year = row["Academic Year"]
        course = row["Course"]
        course_type = row["Course Type"]

        ttl_entry = f"""
programme_Courses:{programme_code}
    ex:hasProgrammeCode "{programme_code}" ;
    ex:hasStudyYear "{study_year}" ;
    ex:hasAcademicYear "{academic_year}" ;
    ex:hascourse "{course}" ;
    ex:hasCourseType "{course_type}" .


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
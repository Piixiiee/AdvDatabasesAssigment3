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
:programme_Course_{programme_code}
    rdf:type :Programme_Course ;    
    :programmeCode "{programme_code}" ;
    :studyYear "{study_year}" ;
    :academicYear "{academic_year}" ;
    :Has_Course_Code :course_{course} ;
    :courseType "{course_type}" .


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
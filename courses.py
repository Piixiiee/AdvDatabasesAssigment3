import csv

# Input CSV file
csv_file = "Courses.csv"

# Output TTL file
ttl_file = "courses.ttl"

# Prefixes
prefixes = """
@prefix ex: <http://example.org/> .
@prefix courses: <http://example.org/courses/> .

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
courses:{course_code}
    ex:hasCourseCode "{course_code}" ;
    ex:hasCourseName "{course_name}" ;
    ex:hasCredits "{credits}" ;
    ex:hasLevel "{level}" ;
    ex:hasDepartment "{department}" ;
    ex:hasDivision "{division}" ;
    ex:hasOwnedBy "{owned_by}" .


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
#Assignment 3 - Group 20 Frida Sundelin & Jennifer Hallberg
import pandas as pd


# Input CSV file
csv_file = ["Course_Instances.csv", "Course_planning.csv"]

# Output TTL file
ttl_file = "course_Instances.ttl"

# Prefixes
prefixes = """
@prefix ex: <http://example.org/> .
@prefix course_Instances: <http://example.org/course_Instances/> .

"""

with open(ttl_file, 'w', encoding='utf-8') as outfile:

    # Write prefixes
    outfile.write(prefixes)

    course_instance = pd.read_csv("Course_Instances.csv")
    course_planning = pd.read_csv("Course_plannings.csv")

    joined_df = pd.merge(course_instance, course_planning, on="Instance_id", how="left")

    joined_df.columns = (
    joined_df.columns
      .str.strip()
      .str.replace(" ", "_")
    )

    for row in joined_df.itertuples(index=False):

        course_code = row.Course_code
        study_period = row.Study_period
        academic_year = row.Academic_year
        instance_id = row.Instance_id
        examiner = row.Examiner
        num_stud = row.Planned_number_of_Students
        sen_hour = row.Senior_Hours
        ass_hour = row.Assistant_Hours
        

        ttl_entry = f"""
:course_Instance_{instance_id}
    rdf:type :Course_Instance ;
    :ciCourse :course_{course_code} ;
    :studyPeriod "{study_period}" ;
    :academicYear "{academic_year}" ;
    :instanceId "{instance_id}" ;
    :Examined_By :senior_teacher_{examiner} ;
    :planningNumStudents "{num_stud}" ;
    :seniorHours "{sen_hour}" ;
    :assistantHours "{ass_hour}" . 


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
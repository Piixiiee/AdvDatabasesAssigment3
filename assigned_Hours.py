import csv
import pandas as pd


# Output TTL file
ttl_file = "Hours.ttl"

# Prefixes
prefixes = """
@prefix : <http://www.semanticweb.org/frida/ontologies/2026/3/untitled-ontology-3/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

"""

with open(ttl_file, 'w', encoding='utf-8') as outfile:

    # Write prefixes
    outfile.write(prefixes)

    assigned_hours = pd.read_csv("Assigned_Hours.csv")
    reported_hours = pd.read_csv("Reported_Hours.csv")

    joined_df = pd.merge(assigned_hours, reported_hours, on=["Teacher Id","Course Instance"], how="left")

    joined_df.columns = (
    joined_df.columns
      .str.strip()
      .str.replace(" ", "_")
    )

    for row in joined_df.itertuples(index=False):

        course_code = row.Course_code
        study_period = row.Study_Period
        academic_year = row.Academic_Year
        teacher_id = row.Teacher_Id
        ass_hours = row.Assigned_Hours
        course_instance = row.Course_Instance
        rep_hours = row.Reported_Hours

        ttl_entry = f"""
:hours_{course_instance}
    rdf:type :Hours ;
    :Hours_Has_Course_Code :course_{course_code} ;
    :studyPeriod "{study_period}" ;
    :academicYear "{academic_year}" ;
    :Hours_Has_Teacher :teacher_{teacher_id} ;
    :Hours_Has_Instance :instance_{course_instance} ;
    :assignedHours "{ass_hours}" ;
    :reportedHours "{rep_hours}" .


"""

        outfile.write(ttl_entry)

print("TTL file created successfully!")
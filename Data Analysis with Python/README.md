# How to Run



-Use in a conda environment and activate jupyter lab 
-Go to the directory containing Starter_Code\PyCitySchools
-Start PyCitySchools_starter.ipynb



# Analysis:
* Full notebook is located in Starter_Code\PyCitySchools

## PyCity Schools Analysis

1. Schools with higher budgets did not yield better test results. However, Schools that had lower student budgets (<585) actually perfomed a lot better in overall test results compared to students who received the highest budgets($645-680). Test scores increase when looking at lower student budget bins.

2. Small and Medium Sized Schools seem to have a higher passing rate than larger populated schools. Could be linked to students per classroom. (89-91% passing vs 67%).

3. As a whole, charter schools out-performed the public district schools in both reading and math scores while having a high passing rate. Charter schools seem to have a lower populated class size which can point to the fact that there are less students per classroom which could be a correlation to high test scores. Or that students in charters have access to better curriculums. More data will be needed, maybe regarding teachers and teacher salaries.


# Background
You are the new Chief Data Scientist for your city's school district. In this capacity, you'll be helping the school board and mayor make strategic decisions regarding future school budgets and priorities.

As a first task, you've been asked to analyze the district-wide standardized test results. You'll be given access to every student's math and reading scores, as well as various information on the schools they attend. Your task is to aggregate the data to showcase obvious trends in school performance.


# Instructions


Using Pandas and Jupyter Notebook, create a report that includes the following data. Your report must include a written description of at least two observable trends based on the data.

Hint: Check out the sample solution called `PyCitySchools_starter.ipynb` located in the .zip file to review the desired format for this assignment.

## District Summary

Perform the necessary calculations and then create a high-level snapshot of the district's key metrics in a DataFrame.

Include the following:

- Total number of unique schools

- Total students

- Total budget

- Average math score

- Average reading score

- % passing math (the percentage of students who passed math)
  
- % passing reading (the percentage of students who passed reading)

- % overall passing (the percentage of students who passed math AND reading)

## School Summary

Perform the necessary calculations and then create a DataFrame that summarizes key metrics about each school.

Include the following:

- School name

- School type

- Total students

- Total school budget

- Per student budget

- Average math score

- Average reading score

- % passing math (the percentage of students who passed math)

- % passing reading (the percentage of students who passed reading)

- % overall passing (the percentage of students who passed math AND reading)

## Highest-Performing Schools (by % Overall Passing)

Sort the schools by % Overall Passing in descending order and display the top 5 rows.

Save the results in a DataFrame called "top_schools".

## Lowest-Performing Schools (by % Overall Passing)

Sort the schools by % Overall Passing in ascending order and display the top 5 rows.

Save the results in a DataFrame called "bottom_schools".

## Math Scores by Grade

Perform the necessary calculations to create a DataFrame that lists the average math score for students of each grade level (9th, 10th, 11th, 12th) at each school.
Reading Scores by Grade

Create a DataFrame that lists the average reading score for students of each grade level (9th, 10th, 11th, 12th) at each school.

## Scores by School Spending

Create a table that breaks down school performance based on average spending ranges (per student).

Use the code provided below to create four bins with reasonable cutoff values to group school spending.
```
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]
```
Use `pd.cut` to categorize spending based on the bins.

Use the following code to then calculate mean scores per spending range.
```
spending_math_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"])["Average Math Score"].mean()
spending_reading_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"])["Average Reading Score"].mean()
spending_passing_math = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Passing Math"].mean()
spending_passing_reading = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Passing Reading"].mean()
overall_passing_spending = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Overall Passing"].mean()
```
Use the scores above to create a DataFrame called `spending_summary`.

Include the following metrics in the table:

- Average math score

- Average reading score

- % passing math (the percentage of students who passed math)

- % passing reading (the percentage of students who passed reading)

- % overall passing (the percentage of students who passed math AND reading)

## Scores by School Size

Use the following code to bin the `per_school_summary`.
```
size_bins = [0, 1000, 2000, 5000]
labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]
```
Use `pd.cut` on the "Total Students" column of the `per_school_summary` DataFrame.

Create a DataFrame called size_summary that breaks down school performance based on school size (small, medium, or large).

## Scores by School Type

Use the `per_school_summary` DataFrame from the previous step to create a new DataFrame called `type_summary`.

This new DataFrame should show school performance based on the "School Type".



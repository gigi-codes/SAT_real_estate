# Project 1: Standardized Test Analysis

## Problem Statements
1. What are California's average SAT and ACT scores? How is California doing in standardized test scores compared to other states? 
2. Should California focus more on math or reading/writing (or science)? 
3. Are test scores significantly different between counties? If so, what factors might explain the differences in test scores?
4. Should California increase or decrease standardized test participation? Why or why not? 
5. How can the scores be improved within the state of California?


## Background

### SAT
source: https://www.cde.ca.gov/ds/sp/ai/whatissat.asp

The SAT Reasoning Test is a standardized test that assesses the critical reading, mathematics, and writing skills that students need to be successful in college. Each of the three sections that comprise the SAT Reasoning Test has a possible score of 800 points. Prior to 2005, the SAT test included only two sections, the verbal section (now referred to as the critical reading section) and the math section, each having possible scores of 800 points. SAT test results represent one factor considered by many colleges and universities in making admissions decisions.

The SAT is owned, published, and developed by the College Board, a non-profit organization in the United States. The California Department of Education does not have results that identify individual students.

source: https://collegereadiness.collegeboard.org/about/scores/benchmarks

Students with an SAT Math section score that meets or exceeds the benchmark have a 75 percent chance of earning at least a C in first-semester, credit-bearing college courses in algebra, statistics, pre-calculus, or calculus.

Students with an SAT Evidence-Based Reading and Writing (ERW) section score that meets or exceeds the benchmark have a 75 percent chance of earning at least a C in first-semester, credit-bearing college courses in history, literature, social sciences, or writing classes.

**SAT College and Career Readiness Benchmarks**

Evidence-Based Reading and Writing: 480 <br/>
Math: 530 <br/>

**11th Grade Benchmarks**

Evidence-Based Reading and Writing: 460 <br/>
Math: 510 <br/>

### ACT
source: https://www.cde.ca.gov/ds/sp/ai/whatisact.asp

The ACT test is designed to assess high school students' general educational development and their ability to complete college-level work. The ACT test covers four subject areas: English, mathematics, reading, and science. Each subject area test receives a score ranging from 1 to 36. The composite score is the average of all four subject area test scores. Many colleges and universities use ACT scores as one factor in making admissions decisions.

The California Department of Education does not have results that identify individual students.

source: https://www.act.org/content/dam/act/unsecured/documents/pdfs/R1670-college-readiness-benchmarks-2017-11.pdf

The ACT College Readiness Benchmarks use a B or higher grade as the indicator of success in the course. Students who earn first-year grades of B or higher, on average, are much more likely to complete a postsecondary degree

| ACT test score | College courses       | Benchmark |
| -------------- | -------------------   | --------- |
| English        | English Composition I | 18        |
| Mathematics    | College Algebra       | 22        |
| Reading        | American History, Other History, Psychology, Sociology, Political Science, Economics | 22 |
| Science        | Biology               | 23        |
| STEM           | Calculus, Chemistry, Biology, Physics, Engineering | 26 |
| ELA            | English Composition I, American History, Other History, Psychology, Sociology, Political Science, Economics | 20 |


## List of Used Datasets:
1. `act_2017.csv`
2. `act_2018.csv`
3. `act_2019.csv`
4. `act_2017_ca.csv`
5. `sat_2017.csv`
6. `sat_2018.csv`
7. `sat_2019.csv`
8. `sat_2019_ca.csv`
9. `california-counties.geojson` (source: https://github.com/codeforamerica/click_that_hood/blob/master/public/data/california-counties.geojson)

## File/Directory Descriptions

`report.ipynb` contains all the steps used to clean raw datasets, explore datasets, visualize datasets for data analysis. 

`presentation.pdf` is the presentation file.

`output` directory contains all the cleaned and merged datasets in csv format.

`assets` directory contains all the images in png format and interactive plots in html format. 

`data` directory contains all the raw datasets used in the data analysis in csv format.

## Contents inside `report.ipynb`

### Part 1
Part 1 contains the following contents:
- Problem Statements
- Background Information
- Importing libraries
- Coding challenges (creation of functions for data analysis)

### Part 2
Part 2 contains the following contents:
- Importing datasets
- Cleaning datasets
- Exporting cleaned datasets to `output` directory
- Data dictionaries
- Exploratory data analysis
- Data visualizations
- Data analysis
- Conclusions and Recommendations


## Data dictionaries (from Part 2)

Datasets:

SAT/ACT: `sat_2017.csv`, `sat_2018.csv`, `sat_2019.csv`, `act_2017.csv`, `act_2018.csv`, `act_2019.csv` <br/>
SAT(CDE): `sat_2019_ca.csv` <br/>
ACT(CDE): `act_2019_ca.csv` <br/>

`sat_act_2017_2019` DataFrame

|Feature|DType|Datasets|Description|
|---|---|---|---|
|state|object|SAT/ACT|State name| 
|act_participation_17|float64|SAT/ACT|ACT Participation rate, 2017|
|composite_17|float64|SAT/ACT|Average ACT composite score, 2017|
|act_participation_18|float64|SAT/ACT|ACT Participation rate, 2018|
|composite_18|float64|SAT/ACT|Average ACT composite score, 2018|
|act_participation_19|float64|SAT/ACT|ACT Participation rate, 2019|
|composite_19|float64|SAT/ACT|Average ACT composite score, 2019|
|sat_participation_17|float64|SAT/ACT|SAT Participation rate, 2017|
|ebrw_17|int64|SAT/ACT|Average SAT Evidence-Based Reading and Writing score, 2017| 
|math_17|int64|SAT/ACT|Average SAT math score, 2017| 
|total_17|int64|SAT/ACT|Average SAT total score, 2017|
|sat_participation_18|float64|SAT/ACT|SAT Participation rate, 2018|
|ebrw_18|int64|SAT/ACT|Average SAT Evidence-Based Reading and Writing score, 2018| 
|math_18|int64|SAT/ACT|Average SAT math score, 2018| 
|total_18|int64|SAT/ACT|Average SAT total score, 2018|
|sat_participation_19|float64|SAT/ACT|SAT Participation rate, 2019|
|ebrw_19|int64|SAT/ACT|Average SAT Evidence-Based Reading and Writing score, 2019| 
|math_19|int64|SAT/ACT|Average SAT math score, 2019| 
|total_19|int64|SAT/ACT|Average SAT total score, 2019|


`sat_2019_ca` DataFrame (source: https://www.cde.ca.gov/ds/sp/ai/reclayoutsat19.asp)

|Feature|DType|Datasets|Description|
|---|---|---|---|
|cds|float64 |SAT(CDE)| County/District/School Code|
|ccode| float64 | SAT(CDE) | County Code|
|cdcode| float64 | SAT(CDE) | District Code|
|scode| float64 | SAT(CDE) | School Code|
|rtype| object | SAT(CDE)| Record Type: C=County, D=District, S=School, X=State|
|sanme| object | SAT(CDE)| School Name, N/A = County or District Level Record|
|danme| object | SAT(CDE)| District/LEA Name, N/A = County Level Record|
|cname| object | SAT(CDE)| County Name| 
|enroll12| float64 | SAT(CDE) | Enrollment of Grade 12|
|numtsttakr12| float64 | SAT(CDE) | Number of Test Takers Grade 12|
|numerwbenchmark12| float64 | SAT(CDE) | The number meeting the Evidence-Based Reading & Writing (ERW) benchmark established by the College Board based on the New 2016 SAT test format as of March 2016 for Grade 12. |
|pcterwbenchmark12| float64 | SAT(CDE) | The percent of students who met or exceeded the benchmark for Evidence-Based Reading & Writing (ERW) test for Grade 12.|
|nummathbenchmark12| float64 | SAT(CDE) | The number of students who met or exceeded the benchmark for the New SAT Math test format as of March 2016 for Grade 12.|
|pctmathbenchmark12| float64 | SAT(CDE) | The percent of students who met or exceeded the benchmark for SAT Math test for Grade 12.|
|enroll11| float64 | SAT(CDE) | Enrollment of Grade 11|
|numtsttakr11| float64 | SAT(CDE) | Number of Test Takers Grade 11|
|numerwbenchmark11| float64 | SAT(CDE) | The number meeting the Evidence-Based Reading & Writing (ERW) benchmark established by the College Board based on the New 2016 SAT test format as of March 2016 for Grade 11.|
|pcterwbenchmark11| float64 | SAT(CDE) | The percent of students who met or exceeded the benchmark for Evidence-Based Reading & Writing (ERW) test for Grade 11.|
|nummathbenchmark11| float64 | SAT(CDE) | The number of students who met or exceeded the benchmark for the New SAT Math test format as of March 2016 for Grade 11.|
|pctmathbenchmark11| float64 | SAT(CDE) | The percent of students who met or exceeded the benchmark for SAT Math test for Grade 11.|
|totnumbothbenchmark12 |float64 | SAT(CDE) | The total number of students who met the benchmark of both Evidence-Based Reading & Writing (ERW) and Math Grade 12.|
|pctbothbenchmark12| float64 | SAT(CDE) | The percent of students who met the benchmark of both Evidence-Based Reading & Writing (ERW) and Math Grade 12.|
|totnumbothbenchmark11| float64 | SAT(CDE) | The total number of students who met the benchmark of both Evidence-Based Reading & Writing (ERW) and Math Grade 11.|
|pctbothbenchmark11| float64 | SAT(CDE) | The percent of students who met the benchmark of both Evidence-Based Reading & Writing (ERW) and Math Grade 11.|
|year| object | SAT(CDE)| The SAT test administration year: 2018-19|


`act_2019_ca` DataFrame (source: https://www.cde.ca.gov/ds/sp/ai/reclayoutact19.asp)

| Feature    | DType     | Datasets | Description |
| ---------- | --------- | ----- |----- |
| cds        | float64 |ACT(CDE) | County/District/School code |
| rtype      | object | ACT(CDE)| Record Type: C=County, D=District, S=School, X=State |
| sname      | object | ACT(CDE)| School Name, N/A = County or District Level Record |
| danme      | object | ACT(CDE)| District Name, N/A = County Level Record |
| cname      | object | ACT(CDE)| County Name |
| enroll12   | float64 |ACT(CDE) | Enrollment of Grade 12 |
| numtsttakr | float64 |ACT(CDE) | Number of Test Takers |
| avgscreng  | float64 |ACT(CDE) | Average ACT  English Score |
| avgscrread | float64 |ACT(CDE) | Average ACT Reading Score |
| avgscrmath | float64 |ACT(CDE) | Average ACT Math Score |
| acgscrsci  | float64 |ACT(CDE) | Average ACT Science Score |
| numge21    | float64 |ACT(CDE) | Number of Test Takers Whose ACT Composite Scores Are Greater or Equal to 21 |
| pctge21    | float64 |ACT(CDE) | Percent of Test Takers Whose ACT Composite Scores Are Greater or Equal to 21 |
| year       | object | ACT(CDE)| The ACT test administration year: 2018-19 |
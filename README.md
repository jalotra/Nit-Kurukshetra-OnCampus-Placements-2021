 ## Objective

 This repo contains the data and maybe some Stats of On-Campus Placements in Nit Kurukshetra of 2021 Batch.
 I have stitched this repo to serve some purposes:

 1. So that Juniors can take informed decisions while preparing for placements.
 2. To make the Placement-data Public so that people can run numbers.
 3. To learn what it takes to gather the data.
 4. Run some numbers myself and find some interesting things from the data.

 ## How did I collected data?

 1. I used the Gmail API to scrap the emails that have the invariant that they have `placement` or `recruitment` or `drive` in them.
 2. Then I automated collecting some data points like JobLocation, CompanyName and MinCgpa etc.
 3. One more long day went into structuring the data.

 ### About Data

 1. The data in `data.csv` have these different data-columns.
 2. `CompanyName`, `JobProfile`, `JobLocation`, `EligibleBranches`, `MinCgpa`, `IIITAllowed`.
 3. And data in `data_with_ctc.csv` adds just one more column to above columns.
 4. The column name is `Ctc`.

 Explanation:

 `CompanyName`: Name of the company, Example: Oneplus

 `JobProfile`: What will you be doing, Example: Software Developer, Analyst etc

 `EligibleBranches`: What all branches were allowed to sit for the (first) exam or (first online round), Example: cs, it

 `MinCgpa`: What is the minimum CGPA required by the company. Example 7.5

 `IIITAllowed`: 1 if IIIT was Allowed, 0 if IIIT was not allowed, 0.5 if I couldn't figure it out.

 `CTC`: What's the Ctc that the company offered initially (in the first mail that I received), this might have changed down the line. Al
 (for juniors): Ctc != What you will get in your bank accounts.

 ## RESULTS

 ##### Note: Please read data_explore.ipynb for detailed explanation.
 ##### Note: The data is of BTech students also, I have omitted all the details of MTech and MBA due to lack of resources.
 ##### * means that the as per data collected till March 1st, 2021. It will change in the future.

 1. Total Companies that came are: 114*.
 2. Total Different Profiles that students are placed in: 79*.
 3. Total Different Job Locations that students will go to in India: 49*.
 4. Branch wise distribution of Companies, or in simpler terms => Out of total companies that visited campus. How many companies allowed
 particular branch?

     4a) CSE: 86

     4b) IT: 81

     4c) ECE: 82

     4d) EE: 65

     4e) MECH: 47

     4f) PIE: 38

     4g) CIVIL: 29

 5. Cgpa Requirements

     5a) 8 for 100 percentile (It means if you are eligible and your CGPA is 8 you can sit for >=100% of the companies)

     5b) 7 for 75 percentile (It means if you are eligible and your CGPA is 7 you can sit for >= 75% of the companies)

 ### A Little Appreciation

 1. I would like to thanks all the `TnP` and individual `Placement-Coordinators` for working so hard in getting companies.
 2. Finally some of my friend for the the `~support` they gave.

 ## Caution

 1. I am the sole author of this data. I have scraped the data from my emails using GMAIL API.
 2. I have no affiliation with any school, organization.
 3. The data will surely have discrepancy.
 4. Read or use at your own will.

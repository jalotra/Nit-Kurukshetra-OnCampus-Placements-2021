## Objective
This repo contains the data and maybe some Stats of On-Campus Placements in Nit Kurukshetra of 2021 Batch. 
I have stitched this repo to serve some purposes : <br />
1. So that Juniors can take informed decisions while preparing for placements. 
2. To make the Placement-data Public so that people can run numbers. 
3. To learn what it takes to gather the data. 
4. Run some numbers myself and find some interesting things from the data.     
 
## How did I collected data ? 
1. I used the Gmail Api to scrap the emails that have the invariant that they have `placement` or `recruitment` or `drive` in them. 
2. Then I automated collecting some data points like JobLocation, CompanyName and MinCgpa etc. 
3. One more long day went into structuring the data.  

### About Data 
1. The data in `data.csv` have these different data-columns.
2. `CompanyName`, `JobProfile`, `JobLocation`, `EligibleBranches`, `MinCgpa`, `IIITAllowed`. 

Explanation: <br />
`CompanyName` : `Name of the company, Example : Oneplus` <br />
`JobProfile` : `What will you be doing, Example : Software Developer, Analyst etc` <br />
`EligibleBranches` : `What all branches were allowed to sit for the (first)exam or (first online round), Example : cs, it` <br />
`MinCgpa` : `What is the minimum CGPA required by the company. Example 7.5` <br />
`IIITAllowed` `1 if IIIT was Allowed, 0 if IIIT was not allowed, 0.5 if I couldn't figure it out.`<br />


## RESULTS
##### Note : Please read data_explore.ipynb for detailed explanation. 
##### * means that the as per data collected till March 1st, 2021. It will change in the future. 
1. Total Companies that came are : 114* . <br />
2. Total Different Profiles that students are placed in : 79*
3. Total Different Job Locations that students will go to in India : 49*
4. Branch Wise Distribution of Companies. <br />
    4a) CSE : 86 <br />
    4b) IT : 81 <br />
    4c) ECE : 82 <br />
    4d) EE : 65 <br />
    4e) MECH : 47 <br />
    4f) PIE : 38 <br />
    4g) CIVIL : 29 <br />

5. Cgpa Requirements <br />
    5a) 8 for 100 percentile. (It means if you are eligible and your CGPA is 8 you can sit for >=100% of the companies) <br />
    5b) 7 for 75 percentile. (It means if you are eligible and your CGPA is 7 you can sit for >= 75% of the companies) <br />

### A Little Appreciation 
1. I would like to thanks all the `TnP` and individual `Placement-Coordinators` for working so hard in  getting companies. <p />   
2. Finally some of my friend for the the `~support` they gave.

## Caution 
1. I am the sole author of this data. I have scraped the data from my emails using GMAIL API. 
2. I have no affiliation with any school, organisation. 
3. The data will surely have discrepancy.
4. Read or use at your own will. 
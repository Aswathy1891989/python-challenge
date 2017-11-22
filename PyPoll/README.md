
 PyPoll

![Vote-Counting](Images/Vote_counting.jpg)
The task is to help a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

Two sets of poll data (`election_data_1.csv` and `election_data_2.csv`) is given. Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. The task is to create a Python script that analyzes the votes and calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

As an example, the analysis should looks similar to the one below:

```
Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
-------------------------
```

The final script must be able to handle any such similarly-structured dataset in the future and the final script  prints the analysis to the terminal and exports a text file with the results.

